from pydantic import BaseModel, conint, conlist, Field


class InstaMonkey(BaseModel):
    tiers: conlist(conint(ge=0, le=5), min_items=3, max_items=3)
    quantity: float
    is_new: bool = Field(..., alias="isNew")


class InstaTowers(BaseModel):
    spike_factory: list[InstaMonkey] = Field(..., alias="SpikeFactory")
    alchemist: list[InstaMonkey] = Field(..., alias="Alchemist")
    wizard_monkey: list[InstaMonkey] = Field(..., alias="WizardMonkey")
    dart_monkey: list[InstaMonkey] = Field(..., alias="DartMonkey")
    monkey_ace: list[InstaMonkey] = Field(..., alias="MonkeyAce")
    druid: list[InstaMonkey] = Field(..., alias="Druid")
    glue_gunner: list[InstaMonkey] = Field(..., alias="GlueGunner")
    ice_monkey: list[InstaMonkey] = Field(..., alias="IceMonkey")
    tack_shooter: list[InstaMonkey] = Field(..., alias="TackShooter")
    ninja_monkey: list[InstaMonkey] = Field(..., alias="NinjaMonkey")
    monkey_sub: list[InstaMonkey] = Field(..., alias="MonkeySub")
    engineer_monkey: list[InstaMonkey] = Field(..., alias="EngineerMonkey")
    monkey_buccaneer: list[InstaMonkey] = Field(..., alias="MonkeyBuccaneer")
    heli_pilot: list[InstaMonkey] = Field(..., alias="HeliPilot")
    bomb_shooter: list[InstaMonkey] = Field(..., alias="BombShooter")
    sniper_monkey: list[InstaMonkey] = Field(..., alias="SniperMonkey")
    banana_farm: list[InstaMonkey] = Field(..., alias="BananaFarm")
    dartling_gunner: list[InstaMonkey] = Field(..., alias="DartlingGunner")
    boomerang_monkey: list[InstaMonkey] = Field(..., alias="BoomerangMonkey")
    monkey_village: list[InstaMonkey] = Field(..., alias="MonkeyVillage")
    mortar_monkey: list[InstaMonkey] = Field(..., alias="MortarMonkey")
    super_monkey: list[InstaMonkey] = Field(..., alias="SuperMonkey")
