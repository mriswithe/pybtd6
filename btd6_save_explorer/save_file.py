import hashlib
from pathlib import Path
from pprint import pprint
import struct
import zlib
import json
import hmac

FILE_PIECES = tuple[bytes, int, bytes, bytes]


class Save:
    # Some constants
    _PASSWORD_INDEX_LENGTH = 8
    _PASSWORD_INDEX = 2
    _DUMMY_HEADER_LENGTH = 44
    _SALT_LENGTH = 24
    _KEY_LENGTH = 16
    _IV_LENGTH = 16
    _DERIVE_ITERATIONS = 10
    _DEFAULT_PASSWORD = b"11"

    _file_contents: bytes

    def __init__(self, file: Path | str):
        if not isinstance(file, Path):
            file = Path(file)
        (
            self._dummy_header,
            self._password_index,
            self._salt,
            self._payload,
        ) = self._read_file(file)

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
    def derived_key(self) -> bytes:
        args = dict(
            hash_name="SHA1",
            password=self._DEFAULT_PASSWORD,
            salt=self.salt,
            iterations=self._DERIVE_ITERATIONS,
            dklen=self._IV_LENGTH + self._KEY_LENGTH,
        )

        resp = hashlib.pbkdf2_hmac(**args)
        args["resp"] = resp
        args["resp_len"] = len(resp)
        args["resp_hex"] = resp.hex()
        pprint(args)
        return resp

    def make_json(self, out: Path | str):
        if not isinstance(out, Path):
            out = Path(out)
        out.write_text(json.dumps(self.save_data))

    @property
    def save_data(self):
        return json.loads(self._uncompressed_save())

    def _uncompressed_save(self) -> bytes:
        return zlib.decompress(self._decrypted_save())

    def _decrypted_save(self) -> bytes:
        return hmac.digest(
            self.derived_key + bytes(self._IV_LENGTH), self._payload, "SHA1"
        )

    def _read_file(self, file: Path) -> FILE_PIECES:
        with file.open("rb") as fp:
            # Unpack a char[44]
            header = struct.unpack("44s", fp.read(self._DUMMY_HEADER_LENGTH))[0]
            # Unpack a uint64
            password_index = struct.unpack("Q", fp.read(self._PASSWORD_INDEX_LENGTH))[0]
            # Unpack a char[24]
            salt = struct.unpack("24s", fp.read(self._SALT_LENGTH))[0]
            # The rest is encrypted data, just read the rest
            payload = fp.read()
        return header, password_index, salt, payload
