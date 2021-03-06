# generated by datamodel-codegen:
#   filename:  Profile.json
#   timestamp: 2021-12-19T07:57:15+00:00

from __future__ import annotations

from typing import Any, Dict, List

from pydantic import BaseModel, Field

from .instamonkey import InstaTowers
from .maps import MapInfo
from .powers import PowersData


class TowerXp(BaseModel):
    dart_monkey: float = Field(..., alias="DartMonkey")
    tack_shooter: float = Field(..., alias="TackShooter")
    glue_gunner: float = Field(..., alias="GlueGunner")
    ice_monkey: float = Field(..., alias="IceMonkey")
    bomb_shooter: float = Field(..., alias="BombShooter")
    boomerang_monkey: float = Field(..., alias="BoomerangMonkey")
    monkey_ace: float = Field(..., alias="MonkeyAce")
    mortar_monkey: float = Field(..., alias="MortarMonkey")
    sniper_monkey: float = Field(..., alias="SniperMonkey")
    super_monkey: float = Field(..., alias="SuperMonkey")
    ninja_monkey: float = Field(..., alias="NinjaMonkey")
    monkey_village: float = Field(..., alias="MonkeyVillage")
    engineer_monkey: float = Field(..., alias="EngineerMonkey")
    sentry: float = Field(..., alias="Sentry")
    spike_factory: float = Field(..., alias="SpikeFactory")
    monkey_sub: float = Field(..., alias="MonkeySub")
    wizard_monkey: float = Field(..., alias="WizardMonkey")
    banana_farm: float = Field(..., alias="BananaFarm")
    monkey_buccaneer: float = Field(..., alias="MonkeyBuccaneer")
    alchemist: float = Field(..., alias="Alchemist")
    natures_ward_totem: float = Field(..., alias="NaturesWardTotem")
    phoenix: float = Field(..., alias="Phoenix")
    heli_pilot: float = Field(..., alias="HeliPilot")
    dartling_gunner: float = Field(..., alias="DartlingGunner")
    druid: float = Field(..., alias="Druid")
    buccaneer_lesser_plane: float = Field(..., alias="BuccaneerLesserPlane")
    banana_farmer: float = Field(..., alias="BananaFarmer")
    sentry_crushing: float = Field(..., alias="SentryCrushing")
    sentry_cold: float = Field(..., alias="SentryCold")
    sentry_energy: float = Field(..., alias="SentryEnergy")
    sentry_boom: float = Field(..., alias="SentryBoom")
    buccaneer_greater_plane: float = Field(..., alias="BuccaneerGreaterPlane")
    sentry_paragon: float = Field(..., alias="SentryParagon")
    cave_monkey: float = Field(..., alias="CaveMonkey")
    buccaneer_lesser_plane_camo: float = Field(..., alias="BuccaneerLesserPlaneCamo")
    sun_avatar_mini: float = Field(..., alias="SunAvatarMini")
    spectre_va: float = Field(..., alias="SpectreVA")
    perma_phoenix: float = Field(..., alias="PermaPhoenix")
    marine: float = Field(..., alias="Marine")
    _: float
    lord_phoenix: float = Field(..., alias="LordPhoenix")
    tech_bot: float = Field(..., alias="TechBot")
    spectre_vc: float = Field(..., alias="SpectreVC")
    true_sun_avatar_mini: float = Field(..., alias="TrueSunAvatarMini")
    drone: float = Field(..., alias="Drone")
    uav: float = Field(..., alias="UAV")
    ucav: float = Field(..., alias="UCAV")
    sacrificial_totem: float = Field(..., alias="SacrificialTotem")
    pontoon: float = Field(..., alias="Pontoon")
    ball_of_light__tower: float = Field(..., alias="BallOfLight-Tower")
    portable_lake: float = Field(..., alias="PortableLake")
    buccaneer_paragon_plane: float = Field(..., alias="BuccaneerParagonPlane")


class SelectedTowerSkinData(BaseModel):
    quincy: str = Field(..., alias="Quincy")
    gwendolin: str = Field(..., alias="Gwendolin")
    obyn_greenfoot: str = Field(..., alias="ObynGreenfoot")
    striker_jones: str = Field(..., alias="StrikerJones")
    captain_churchill: str = Field(..., alias="CaptainChurchill")
    benjamin: str = Field(..., alias="Benjamin")
    ezili: str = Field(..., alias="Ezili")
    pat_fusty: str = Field(..., alias="PatFusty")
    adora: str = Field(..., alias="Adora")
    admiral_brickell: str = Field(..., alias="AdmiralBrickell")
    etienne: str = Field(..., alias="Etienne")
    sauda: str = Field(..., alias="Sauda")
    psi: str = Field(..., alias="Psi")


class AnalyticsInfo(BaseModel):
    heroes_placed_by_name: Dict[str, Any] = Field(..., alias="heroesPlacedByName")
    upgrades_purchased_by_tier: Dict[str, Any] = Field(
        ..., alias="upgradesPurchasedByTier"
    )
    hero_upgrades_purchased_by_tier: Dict[str, Any] = Field(
        ..., alias="heroUpgradesPurchasedByTier"
    )
    abilities_activated_by_name: Dict[str, Any] = Field(
        ..., alias="abilitiesActivatedByName"
    )
    hero_levels_by_name: Dict[str, Any] = Field(..., alias="heroLevelsByName")
    hero_won_count: Dict[str, Any] = Field(..., alias="heroWonCount")
    power_history: Dict[str, Any] = Field(..., alias="powerHistory")
    monkey_type_wins: Dict[str, Any] = Field(..., alias="monkeyTypeWins")
    game_id: int = Field(..., alias="gameID")
    bloons_popped: int = Field(..., alias="bloonsPopped")
    moabs_popped: int = Field(..., alias="moabsPopped")
    bfbs_popped: int = Field(..., alias="bfbsPopped")
    zomgs_popped: int = Field(..., alias="zomgsPopped")
    ddts_popped: int = Field(..., alias="ddtsPopped")
    bads_popped: int = Field(..., alias="badsPopped")
    fortified_popped: int = Field(..., alias="fortifiedPopped")
    purples_popped: int = Field(..., alias="purplesPopped")
    camos_popped: int = Field(..., alias="camosPopped")
    ceramics_popped: int = Field(..., alias="ceramicsPopped")
    regrow_popped: int = Field(..., alias="regrowPopped")
    lead_popped: int = Field(..., alias="leadPopped")
    coop_cash_recieved: int = Field(..., alias="coopCashRecieved")
    coop_cash_sent: int = Field(..., alias="coopCashSent")
    total_towers_placed: int = Field(..., alias="totalTowersPlaced")
    total_towers_sold: int = Field(..., alias="totalTowersSold")
    total_powers_activated: int = Field(..., alias="totalPowersActivated")
    total_upgrades_purchased: int = Field(..., alias="totalUpgradesPurchased")
    total_abilities_activated: int = Field(..., alias="totalAbilitiesActivated")
    times_hero_placed: int = Field(..., alias="timesHeroPlaced")
    times_hero_sold: int = Field(..., alias="timesHeroSold")
    times_game_restarted: int = Field(..., alias="timesGameRestarted")
    third_level_hero_ability_used: bool = Field(..., alias="thirdLevelHeroAbilityUsed")
    tenth_level_hero_ability_used: bool = Field(..., alias="tenthLevelHeroAbilityUsed")
    reported_first_session: bool = Field(..., alias="reportedFirstSession")
    reported_first_purchase: bool = Field(..., alias="reportedFirstPurchase")


class EventData(BaseModel):
    event_id: str = Field(..., alias="eventId")
    amount_collected: float = Field(..., alias="amountCollected")
    amount_rewarded_for: float = Field(..., alias="amountRewardedFor")
    amount_last_seen: float = Field(..., alias="amountLastSeen")
    seed: float
    featured_insta_charges: List[float] = Field(..., alias="featuredInstaCharges")
    last_featured_instas_page_seen: float = Field(
        ..., alias="lastFeaturedInstasPageSeen"
    )


class Model(BaseModel):
    version: int
    saved_by_game_version: str = Field(..., alias="savedByGameVersion")
    tower_xp: TowerXp = Field(..., alias="towerXp")
    acquired_upgrades: List[str] = Field(..., alias="acquiredUpgrades")
    viewed_upgrades: List[str] = Field(..., alias="viewedUpgrades")
    acquired_knowledge: List[str] = Field(..., alias="acquiredKnowledge")
    paid_for_knowledge: List[str] = Field(..., alias="paidForKnowledge")
    knowledge_disabled: bool = Field(..., alias="knowledgeDisabled")
    new_knowledge_points: bool = Field(..., alias="newKnowledgePoints")
    unlocked_towers: List[str] = Field(..., alias="unlockedTowers")
    unlocked_heroes: List[str] = Field(..., alias="unlockedHeroes")
    unlocked_tower_skins: List[str] = Field(..., alias="unlockedTowerSkins")
    seen_unlocked_notification: List[str] = Field(..., alias="seenUnlockedNotification")
    seen_unlocked_heroes: List[str] = Field(..., alias="seenUnlockedHeroes")
    seen_new_hero_notification: List[str] = Field(..., alias="seenNewHeroNotification")
    seen_new_tower_skin_notification: List[str] = Field(
        ..., alias="seenNewTowerSkinNotification"
    )
    map_info: MapInfo = Field(..., alias="mapInfo")
    seen_events: List[str] = Field(..., alias="seenEvents")
    paid_user_status: float = Field(..., alias="paidUserStatus")
    rate_me_sku_version_number: str = Field(..., alias="rateMeSkuVersionNumber")
    count_games_since_sku_rate_me_change: bool = Field(
        ..., alias="countGamesSinceSkuRateMeChange"
    )
    completed_games_since_sku_rate_me_change: int = Field(
        ..., alias="completedGamesSinceSkuRateMeChange"
    )
    completed_game: int = Field(..., alias="completedGame")
    seen_pop_up_event_ids: List[str] = Field(..., alias="seenPopUpEventIds")
    selected_tower_skin_data: SelectedTowerSkinData = Field(
        ..., alias="selectedTowerSkinData"
    )
    powers: Dict[str, Any]
    powers_data: PowersData = Field(..., alias="powersData")
    insta_towers: InstaTowers = Field(..., alias="instaTowers")
    saved_maps: Dict[str, Any] = Field(..., alias="savedMaps")
    guid: str
    device_id: str = Field(..., alias="deviceID")
    owner_id: str = Field(..., alias="ownerID")
    trophies_wallet_id: str = Field(..., alias="trophiesWalletId")
    unclaimed_trophies: List = Field(..., alias="unclaimedTrophies")
    time_stamp: str = Field(..., alias="timeStamp")
    monkey_money: float = Field(..., alias="monkeyMoney")
    xp: float
    rank: float
    veteran_xp: float = Field(..., alias="veteranXp")
    veteran_rank: float = Field(..., alias="veteranRank")
    seen_veteran_rank_info: bool = Field(..., alias="seenVeteranRankInfo")
    level_cap_was: int = Field(..., alias="levelCapWas")
    trophies: float
    lifetime_trophies: float = Field(..., alias="lifetimeTrophies")
    knowledge_points: float = Field(..., alias="knowledgePoints")
    primary_hero: str = Field(..., alias="primaryHero")
    secondary_hero: Any = Field(..., alias="secondaryHero")
    achievements_progress: dict[str, float] = Field(..., alias="achievementsProgress")
    achievements_claimed: List[int] = Field(..., alias="achievementsClaimed")
    achievements_seen: List[int] = Field(..., alias="achievementsSeen")
    achievements_posted_to_x_box_live: List = Field(
        ..., alias="achievementsPostedToXBoxLive"
    )
    achievements_posted_to_google_play: List = Field(
        ..., alias="achievementsPostedToGooglePlay"
    )
    analytics_info: AnalyticsInfo = Field(..., alias="analyticsInfo")
    analytics_kon_fuze: AnalyticsKonFuze = Field(..., alias="analyticsKonFuze")
    highest_seen_round: int = Field(..., alias="highestSeenRound")
    purchase: Purchase
    gifts_received: List = Field(..., alias="giftsReceived")
    daily_reward_index: int = Field(..., alias="dailyRewardIndex")
    last_saved_utc_time: str = Field(..., alias="lastSavedUTCTime")
    next_daily_reward_date_time: str = Field(..., alias="nextDailyRewardDateTime")
    total_daily_challenges_completed: int = Field(
        ..., alias="totalDailyChallengesCompleted"
    )
    consecutive_daily_challenges_completed: int = Field(
        ..., alias="consecutiveDailyChallengesCompleted"
    )
    unique_completed_daily_challenge_ids: List = Field(
        ..., alias="uniqueCompletedDailyChallengeIds"
    )
    race_medal_data: Dict[str, Any] = Field(..., alias="raceMedalData")
    boss_badge_data: Any = Field(..., alias="bossBadgeData")
    boss_medals: BossMedals = Field(..., alias="bossMedals")
    boss_leaderboard_medals: Dict[str, Any] = Field(..., alias="bossLeaderboardMedals")
    boss_leaderboard_elite_medals: Dict[str, Any] = Field(
        ..., alias="bossLeaderboardEliteMedals"
    )
    seen_mini_race: bool = Field(..., alias="seenMiniRace")
    total_races_entered: float = Field(..., alias="totalRacesEntered")
    race_best_time_for_achievements: float = Field(
        ..., alias="raceBestTimeForAchievements"
    )
    challenge_editor_model: Any = Field(..., alias="challengeEditorModel")
    completed_created_challenge: bool = Field(..., alias="completedCreatedChallenge")
    submitted_challenge_editor_id: Any = Field(..., alias="submittedChallengeEditorID")
    submitted_odyssey_editor_id: Any = Field(..., alias="submittedOdysseyEditorID")
    seen_challenge_modified_popup: bool = Field(..., alias="seenChallengeModifiedPopup")
    last_submitted_content_time: LastSubmittedContentTime = Field(
        ..., alias="lastSubmittedContentTime"
    )
    in_game_settings: InGameSettings = Field(..., alias="inGameSettings")
    language_code: str = Field(..., alias="languageCode")
    challenges_played: float = Field(..., alias="challengesPlayed")
    challenges_shared: float = Field(..., alias="challengesShared")
    wins_with_custom_hero_skin: float = Field(..., alias="winsWithCustomHeroSkin")
    bill_greates: float = Field(..., alias="billGreates")
    a_crate_time: float = Field(..., alias="aCrateTime")
    collection_event_map_bonus_data: CollectionEventMapBonusData = Field(
        ..., alias="collectionEventMapBonusData"
    )
    odyssey_save_data: OdysseySaveData = Field(..., alias="odysseySaveData")
    odyssey_editor_save_data: Any = Field(..., alias="odysseyEditorSaveData")
    odysseys_editor_data: OdysseysEditorData = Field(..., alias="odysseysEditorData")
    embarked_odyssey_editor_dcm: Any = Field(..., alias="embarkedOdysseyEditorDcm")
    completed_odysseys: CompletedOdysseys = Field(..., alias="completedOdysseys")
    total_completed_odysseys: float = Field(..., alias="totalCompletedOdysseys")
    cancelled_facebook_friends_popup: bool = Field(
        ..., alias="cancelledFacebookFriendsPopup"
    )
    coop_quick_match_setting: int = Field(..., alias="coopQuickMatchSetting")
    coop_match_set_to_private: bool = Field(..., alias="coopMatchSetToPrivate")
    current_coop_game_details: Any = Field(..., alias="currentCoopGameDetails")
    hotkeys_data: Any = Field(..., alias="hotkeysData")
    hotkeys_data2: HotkeysData2 = Field(..., alias="hotkeysData2")
    has_seen_new_double_cash: bool = Field(..., alias="hasSeenNewDoubleCash")
    seen_big_bloons: bool = Field(..., alias="seenBigBloons")
    unlocked_big_bloons: bool = Field(..., alias="unlockedBigBloons")
    big_bloons_active: bool = Field(..., alias="bigBloonsActive")
    seen_small_bloons: bool = Field(..., alias="seenSmallBloons")
    unlocked_small_bloons: bool = Field(..., alias="unlockedSmallBloons")
    small_bloons_active: bool = Field(..., alias="smallBloonsActive")
    seen_big_towers: bool = Field(..., alias="seenBigTowers")
    unlocked_big_towers: bool = Field(..., alias="unlockedBigTowers")
    big_towers_active: bool = Field(..., alias="bigTowersActive")
    seen_small_towers: bool = Field(..., alias="seenSmallTowers")
    unlocked_small_towers: bool = Field(..., alias="unlockedSmallTowers")
    small_towers_active: bool = Field(..., alias="smallTowersActive")
    pat_wins_on10_release: int = Field(..., alias="patWinsOn10Release")
    oompa_loompad: bool = Field(..., alias="oompaLoompad")
    collection_event_data: CollectionEventData = Field(..., alias="collectionEventData")
    saved_play_list: List = Field(..., alias="savedPlayList")
    use_juke_box: bool = Field(..., alias="useJukeBox")
    trophy_store_purchased_items: TrophyStorePurchasedItems = Field(
        ..., alias="trophyStorePurchasedItems"
    )
    named_monkey_names: Dict[str, Any] = Field(..., alias="namedMonkeyNames")
    saved_stats: SavedStats = Field(..., alias="savedStats")
    profile_avatar: str = Field(..., alias="profileAvatar")
    profile_avatar_frame: Any = Field(..., alias="profileAvatarFrame")
    profile_banner: str = Field(..., alias="profileBanner")
    seen_profile_stats: bool = Field(..., alias="seenProfileStats")
    saved_named_monkey_stats: Dict[str, Any] = Field(..., alias="savedNamedMonkeyStats")
    stats_version: int = Field(..., alias="statsVersion")
    trophy_store_seen: bool = Field(..., alias="trophyStoreSeen")
    no_stone_unturned: float = Field(..., alias="noStoneUnturned")
    mo_problems: float = Field(..., alias="moProblems")
    full_speed: float = Field(..., alias="fullSpeed")
    transformic_tonic_uses_on20_release: int = Field(
        ..., alias="transformicTonicUsesOn20Release"
    )
    player_challenges: Any = Field(..., alias="playerChallenges")
    current_tower_gift_unlock_index: float = Field(
        ..., alias="currentTowerGiftUnlockIndex"
    )
    current_tower_gift_progress: float = Field(..., alias="currentTowerGiftProgress")
    trophies_spent: int = Field(..., alias="trophiesSpent")
    hosted_coop_games: int = Field(..., alias="hostedCoopGames")
    collection_event_crates_opened: int = Field(
        ..., alias="collectionEventCratesOpened"
    )
    collection_event_crates_types_opened: CollectionEventCratesTypesOpened = Field(
        ..., alias="collectionEventCratesTypesOpened"
    )
    continues_used: float = Field(..., alias="continuesUsed")
    blocked_hostnames: List = Field(..., alias="blockedHostnames")
    seen_intermediate_unlock: bool = Field(..., alias="seenIntermediateUnlock")
    seen_advanced_unlock: bool = Field(..., alias="seenAdvancedUnlock")
    seen_expert_unlock: bool = Field(..., alias="seenExpertUnlock")
    selected_content_tab: int = Field(..., alias="selectedContentTab")
    golden_bloon_data: GoldenBloonData = Field(..., alias="goldenBloonData")
    golden_bloons_popped: int = Field(..., alias="goldenBloonsPopped")
    monkey_teams_wins: int = Field(..., alias="monkeyTeamsWins")
    monkey_teams_data: MonkeyTeamsData = Field(..., alias="monkeyTeamsData")
    gifted_achievements: List = Field(..., alias="giftedAchievements")
    race_pass_count: float = Field(..., alias="racePassCount")
    unverified_race_pass_claims: List = Field(..., alias="unverifiedRacePassClaims")
    is_boss_ranked_selected: bool = Field(..., alias="isBossRankedSelected")
    is_boss_elite_selected: bool = Field(..., alias="isBossEliteSelected")
    bosses_event_data: List[BossesEventDatum] = Field(..., alias="bossesEventData")
    played_daily_challenge_ids: List = Field(..., alias="playedDailyChallengeIds")
    lost_daily_challenge_ids: List = Field(..., alias="lostDailyChallengeIds")
    won_daily_challenge_ids: List = Field(..., alias="wonDailyChallengeIds")
    has_completed_tutorial: bool = Field(..., alias="HasCompletedTutorial")
