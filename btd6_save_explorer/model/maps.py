from __future__ import annotations

from pydantic import BaseModel, Field


class DifficultyData(BaseModel):
    seen: bool
    seen_completed: bool = Field(..., alias="seenCompleted")
    seen_medal: bool = Field(..., alias="seenMedal")
    best_round: int = Field(..., alias="bestRound")
    times_completed: int = Field(..., alias="timesCompleted")
    daily_challenge_times_completed: int = Field(
        ..., alias="dailyChallengeTimesCompleted"
    )
    completed_without_loading_save: bool = Field(
        ..., alias="completedWithoutLoadingSave"
    )


class EasyModes(BaseModel):
    deflation: DifficultyData = Field(..., alias="Deflation")
    standard: DifficultyData = Field(..., alias="Standard")
    primary_only: DifficultyData = Field(..., alias="PrimaryOnly")
    clicks: DifficultyData = Field(..., alias="Clicks")
    sandbox: DifficultyData = Field(..., alias="Sandbox")
    super_chimps: DifficultyData = Field(..., alias="SuperChimps")


class MediumModes(BaseModel):
    standard: DifficultyData = Field(..., alias="Standard")
    military_only: DifficultyData = Field(..., alias="MilitaryOnly")
    apopalypse: DifficultyData = Field(..., alias="Apopalypse")
    reverse: DifficultyData = Field(..., alias="Reverse")


class HardModes(BaseModel):
    standard: DifficultyData = Field(..., alias="Standard")
    magic_only: DifficultyData = Field(..., alias="MagicOnly")
    half_cash: DifficultyData = Field(..., alias="HalfCash")
    double_moab_health: DifficultyData = Field(..., alias="DoubleMoabHealth")
    alternate_bloons_rounds: DifficultyData = Field(..., alias="AlternateBloonsRounds")
    impoppable: DifficultyData = Field(..., alias="Impoppable")
    clicks: DifficultyData = Field(..., alias="Clicks")


class EasyDifficulty(BaseModel):
    modes: EasyModes
    coop_modes: EasyModes


class MediumDifficulty(BaseModel):
    modes: MediumModes
    coop_modes: MediumModes


class HardDifficulty(BaseModel):
    modes: HardModes
    coop_modes: HardModes


class MapData(BaseModel):
    seen: bool
    seen_new: bool = Field(..., alias="seenNew")
    seen_new_difficulty: bool = Field(..., alias="seenNewDifficulty")
    completed: bool
    difficult: DifficultyData


class MapStats(BaseModel):
    tutorial: MapData = Field(..., alias="Tutorial")
    tree_stump: MapData = Field(..., alias="TreeStump")
    town_centre: MapData = Field(..., alias="TownCentre")
    winter_park: MapData = Field(..., alias="WinterPark")
    carved: MapData = Field(..., alias="Carved")
    park_path: MapData = Field(..., alias="ParkPath")
    alpine_run: MapData = Field(..., alias="AlpineRun")
    frozen_over: MapData = Field(..., alias="FrozenOver")
    in_the_loop: MapData = Field(..., alias="InTheLoop")
    cubism: MapData = Field(..., alias="Cubism")
    four_circles: MapData = Field(..., alias="FourCircles")
    hedge: MapData = Field(..., alias="Hedge")
    end_of_the_road: MapData = Field(..., alias="EndOfTheRoad")
    logs: MapData = Field(..., alias="Logs")
    adoras_temple: MapData = Field(..., alias="AdorasTemple")
    spring_spring: MapData = Field(..., alias="SpringSpring")
    karts_n_darts: MapData = Field(..., alias="KartsNDarts")
    moon_landing: MapData = Field(..., alias="MoonLanding")
    haunted: MapData = Field(..., alias="Haunted")
    downstream: MapData = Field(..., alias="Downstream")
    firing_range: MapData = Field(..., alias="FiringRange")
    cracked: MapData = Field(..., alias="Cracked")
    streambed: MapData = Field(..., alias="Streambed")
    chutes: MapData = Field(..., alias="Chutes")
    rake: MapData = Field(..., alias="Rake")
    spice_islands: MapData = Field(..., alias="SpiceIslands")
    spillway: MapData = Field(..., alias="Spillway")
    cargo: MapData = Field(..., alias="Cargo")
    pats_pond: MapData = Field(..., alias="PatsPond")
    peninsula: MapData = Field(..., alias="Peninsula")
    high_finance: MapData = Field(..., alias="HighFinance")
    another_brick: MapData = Field(..., alias="AnotherBrick")
    off_the_coast: MapData = Field(..., alias="OffTheCoast")
    cornfield: MapData = Field(..., alias="Cornfield")
    underground: MapData = Field(..., alias="Underground")
    infernal: MapData = Field(..., alias="Infernal")
    bloody_puddles: MapData = Field(..., alias="BloodyPuddles")
    workshop: MapData = Field(..., alias="Workshop")
    quad: MapData = Field(..., alias="Quad")
    dark_castle: MapData = Field(..., alias="DarkCastle")
    muddy_puddles: MapData = Field(..., alias="MuddyPuddles")
    ouch: MapData = Field(..., alias="#ouch")
    resort: MapData = Field(..., alias="Resort")
    skates: MapData = Field(..., alias="Skates")
    lotus_island: MapData = Field(..., alias="LotusIsland")
    candy_falls: MapData = Field(..., alias="CandyFalls")
    blons: MapData = Field(..., alias="Blons")
    bloonarius_prime: MapData = Field(..., alias="BloonariusPrime")
    balance: MapData = Field(..., alias="Balance")
    encrypted: MapData = Field(..., alias="Encrypted")
    bazaar: MapData = Field(..., alias="Bazaar")
    x_factor: MapData = Field(..., alias="XFactor")
    mesa: MapData = Field(..., alias="Mesa")
    geared: MapData = Field(..., alias="Geared")
    sanctuary: MapData = Field(..., alias="Sanctuary")
    ravine: MapData = Field(..., alias="Ravine")
    flooded_valley: MapData = Field(..., alias="FloodedValley")
    the_cabin: MapData = Field(..., alias="TheCabin")
    quiet_street: MapData = Field(..., alias="QuietStreet")


class MapInfo(BaseModel):
    maps: MapStats
