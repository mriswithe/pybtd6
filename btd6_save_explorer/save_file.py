import json
import struct
import zlib
from pathlib import Path
import hashlib
import hmac
from Crypto.Cipher import AES

FILE_PIECES = tuple[bytes, int, bytes, bytes]


class Save:
    # Some constants
    _PASSWORD_INDEX_LENGTH = 8
    _PASSWORD_INDEX = 2
    _DUMMY_HEADER_LENGTH = 44
    _SALT_LENGTH = 24
    _KEY_LENGTH = 16
    _IV_LENGTH = 16
    _HASH_ITERATIONS = 10
    _DEFAULT_PASSWORD = b"11"

    _file_contents: bytes

    def __init__(self, file: Path | str):
        if not isinstance(file, Path):
            file = Path(file)
        (
            self._dummy_header,
            self._password_index,
            self._salt,
            self._encrypted_save,
        ) = self._read_file(file)
        self._cipher = None

    @property
    def dummy_header(self) -> bytes:
        return self._dummy_header

    @property
    def password_index(self) -> int:
        return self._password_index

    @property
    def salt(self) -> bytes:
        return self._salt

    @property
    def derived_key(self):
        return hashlib.pbkdf2_hmac(
            "SHA1",
            self._DEFAULT_PASSWORD,
            self.salt,
            self._HASH_ITERATIONS,
            self.dklen,
        )

    @property
    def dklen(self):
        return self._IV_LENGTH + self._KEY_LENGTH

    @property
    def key(self) -> bytes:
        return self.derived_key[16:]

    @property
    def init_vector(self) -> bytes:
        return self.derived_key[:16]

    def make_json(self, out: Path | str, indent: int = 2):
        if not isinstance(out, Path):
            out = Path(out)
        out.write_text(json.dumps(self.save_data, indent=indent))

    @property
    def save_data(self):
        return json.loads(self._uncompressed_save())

    @property
    def cipher(self):
        if not self._cipher:
            self._cipher = self._make_cipher()
        return self._cipher

    def _make_cipher(self):
        return AES.new(self.key, AES.MODE_CBC, iv=self.init_vector)

    def _uncompressed_save(self) -> bytes:
        return zlib.decompress(self.decrypted_save())

    def decrypted_save(self) -> bytes:
        return self.cipher.decrypt(self.encrypted_save)

    @property
    def encrypted_save(self) -> bytes:
        return self._encrypted_save

    def _read_file(self, file: Path) -> FILE_PIECES:
        with file.open("rb") as fp:
            # Unpack a char[44]
            header = struct.unpack("44s", fp.read(self._DUMMY_HEADER_LENGTH))[0]
            # Unpack a uint64
            password_index = struct.unpack("Q", fp.read(self._PASSWORD_INDEX_LENGTH))[0]
            # Unpack a char[24]
            salt = struct.unpack("24s", fp.read(self._SALT_LENGTH))[0]
            # The rest is encrypted data, just read the rest
            encrypted_save = fp.read()
        return header, password_index, salt, encrypted_save
