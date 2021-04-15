from typing import Optional, Dict, List

from .base import BaseModel


class PlayerDto(BaseModel):
    platform_id: str
    account_id: str
    summoner_name: str
    summoner_id: str
    current_platform_id: str
    current_account_id: str
    match_history_uri: str
    profile_icon: int


class ParticipantIdentityDto(BaseModel):
    participant_id: int
    player: PlayerDto


class ParticipantTimelineDto(BaseModel):
    participant_id: int
    creeps_per_min_deltas: Dict[str, int]
    xp_per_min_deltas: Dict[str, int]
    gold_per_min_deltas: Dict[str, int]
    cs_diff_per_min_deltas: Optional[Dict[str, int]]
    xp_diff_per_min_deltas: Optional[Dict[str, int]]
    damage_taken_per_min_deltas: Dict[str, int]
    damage_taken_diff_per_min_deltas: Optional[Dict[str, int]]
    role: str
    lane: str


class ParticipantStatsDto(BaseModel):
    participant_id: int
    win: bool
    item0: int
    item1: int
    item2: int
    item3: int
    item4: int
    item5: int
    item6: int
    kills: int
    deaths: int
    assists: int
    largest_killing_spree: int
    largest_multi_kill: int
    killing_sprees: int
    longest_time_spent_living: int
    double_kills: int
    triple_kills: int
    quadra_kills: int
    penta_kills: int
    unreal_kills: int
    total_damage_dealt: int
    magic_damage_dealt: int
    physical_damage_dealt: int
    true_damage_dealt: int
    largest_critical_strike: int
    total_damage_dealt_to_champions: int
    magic_damage_dealt_to_champions: int
    physical_damage_dealt_to_champions: int
    true_damage_dealt_to_champions: int
    total_heal: int
    total_units_healed: int
    damage_self_mitigated: int
    damage_dealt_to_objectives: int
    damage_dealt_to_turrets: int
    vision_score: int
    time_c_cing_others: int
    total_damage_taken: int
    magical_damage_taken: int
    physical_damage_taken: int
    true_damage_taken: int
    gold_earned: int
    gold_spent: int
    turret_kills: int
    inhibitor_kills: int
    total_minions_killed: int
    neutral_minions_killed: int
    neutral_minions_killed_team_jungle: int
    neutral_minions_killed_enemy_jungle: int
    total_time_crowd_control_dealt: int
    champ_level: int
    vision_wards_bought_in_game: int
    sight_wards_bought_in_game: int
    wards_placed: int
    wards_killed: int
    first_blood_kill: bool
    first_blood_assist: bool
    first_tower_kill: bool
    first_tower_assist: bool
    combat_player_score: int
    objective_player_score: int
    total_player_score: int
    total_score_rank: int
    player_score0: int
    player_score1: int
    player_score2: int
    player_score3: int
    player_score4: int
    player_score5: int
    player_score6: int
    player_score7: int
    player_score8: int
    player_score9: int
    perk0: int
    perk0_var1: int
    perk0_var2: int
    perk0_var3: int
    perk1: int
    perk1_var1: int
    perk1_var2: int
    perk1_var3: int
    perk2: int
    perk2_var1: int
    perk2_var2: int
    perk2_var3: int
    perk3: int
    perk3_var1: int
    perk3_var2: int
    perk3_var3: int
    perk4: int
    perk4_var1: int
    perk4_var2: int
    perk4_var3: int
    perk5: int
    perk5_var1: int
    perk5_var2: int
    perk5_var3: int
    perk_primary_style: int
    perk_sub_style: int
    stat_perk0: int
    stat_perk1: int
    stat_perk2: int


class MasteryDto(BaseModel):
    rank: int
    mastery_id: int


class ParticipantDto(BaseModel):
    participant_id: int
    team_id: int
    champion_id: int
    spell1_id: int
    spell2_id: int
    stats: ParticipantStatsDto
    timeline: ParticipantTimelineDto
    highest_achieved_season_tier: Optional[str]
    masteries: Optional[List[MasteryDto]]


class TeamBansDto(BaseModel):
    champion_id: int
    pick_turn: int


class TeamStatsDto(BaseModel):
    team_id: int
    win: str
    first_blood: bool
    first_tower: bool
    first_inhibitor: bool
    first_baron: bool
    first_dragon: bool
    first_rift_herald: bool
    tower_kills: int
    inhibitor_kills: int
    baron_kills: int
    dragon_kills: int
    vilemaw_kills: int
    rift_herald_kills: int
    dominion_victory_score: int
    bans: List[TeamBansDto]


class MatchDto(BaseModel):
    game_id: int
    platform_id: str
    game_creation: int
    game_duration: int
    queue_id: int
    map_id: int
    season_id: int
    game_version: str
    game_mode: str
    game_type: str
    teams: List[TeamStatsDto]
    participants: List[ParticipantDto]
    participant_identities: List[ParticipantIdentityDto]


class MatchPositionDto(BaseModel):
    x: int
    y: int


class MatchEventDto(BaseModel):
    lane_type: Optional[str]
    skill_slot: Optional[int]
    ascended_type: Optional[str]
    creator_id: Optional[int]
    after_id: Optional[int]
    event_type: Optional[str]
    type: str
    level_up_type: Optional[str]
    ward_type: Optional[str]
    participant_id: Optional[int]
    tower_type: Optional[str]
    item_id: Optional[int]
    before_id: Optional[int]
    point_captured: Optional[str]
    monster_type: Optional[str]
    monster_sub_type: Optional[str]
    team_id: Optional[int]
    position: Optional[MatchPositionDto]
    killer_id: Optional[int]
    timestamp: int
    assisting_participant_ids: Optional[List[int]]
    building_type: Optional[str]
    victim_id: Optional[int]


class MatchParticipantFrameDto(BaseModel):
    participant_id: int
    minions_killed: int
    team_score: int
    dominion_score: int
    total_gold: int
    level: int
    xp: int
    current_gold: int
    position: MatchPositionDto
    jungle_minions_killed: int


class MatchFrameDto(BaseModel):
    participant_frames: Dict[str, MatchParticipantFrameDto]
    events: List[MatchEventDto]
    timestamp: int


class MatchTimelineDto(BaseModel):
    frames: List[MatchFrameDto]
    frame_interval: int


class MatchReferenceDto(BaseModel):
    platform_id: str
    game_id: int
    champion: int
    queue: int
    season: int
    timestamp: int
    role: str
    lane: str


class MatchlistDto(BaseModel):
    matches: List[MatchReferenceDto]
    start_index: int
    end_index: int
    total_games: int
