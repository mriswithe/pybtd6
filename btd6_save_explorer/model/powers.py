from __future__ import annotations

from pydantic import BaseModel, Field


class Power(BaseModel):
    quantity: float
    is_new: bool = Field(..., alias="isNew")


class PowersData(BaseModel):
    cash_drop: Power = Field(..., alias="CashDrop")
    road_spikes: Power = Field(..., alias="RoadSpikes")
    monkey_boost: Power = Field(..., alias="MonkeyBoost")
    banana_farmer: Power = Field(..., alias="BananaFarmer")
    moab_mine: Power = Field(..., alias="MoabMine")
    portable_lake: Power = Field(..., alias="PortableLake")
    super_monkey_storm: Power = Field(..., alias="SuperMonkeyStorm")
    energising_totem: Power = Field(..., alias="EnergisingTotem")
    pontoon: Power = Field(..., alias="Pontoon")
    camo_trap: Power = Field(..., alias="CamoTrap")
    thrive: Power = Field(..., alias="Thrive")
    dart_time: Power = Field(..., alias="DartTime")
    glue_trap: Power = Field(..., alias="GlueTrap")
    tech_bot: Power = Field(..., alias="TechBot")
