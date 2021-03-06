EVENT_CODES = {
    1024: 'attack',
    1025: 'corner',
    1026: 'dangerous_attack',
    1027: 'dangerous_free_kick',
    1028: 'free_kick',
    1029: 'goal',
    1030: 'cancel_goal',
    1031: 'penalty',
    1032: 'red_card',
    1034: 'yellow_card',
    1039: 'shot_on_target',
    1040: 'shot_off_target',
    1041: 'shot_off_woodwork',
    1042: 'foul',
    1043: 'offside',
    1044: 'kickoff',
    1045: 'yellowred_card',
    1046: 'cancel_yellowred_card',
    1047: 'cancel_red_card',
    1048: 'cancel_yellow_card',
    1049: 'cancel_penalty',
    1050: 'cancel_corner',
    1051: 'safe',
    1052: 'danger',
    1053: 'goal_kick',
    1054: 'throw_in',
    1055: 'substitution',
    1057: 'save',
    1058: 'block',
    1059: 'retake_penalty',
    1060: 'missed_penalty',
    1062: 'possible_penalty',
    1064: 'breakaway',
    1065: 'confirm_goal',
    1066: 'possible_corner',
    1067: 'no_corner',
    1068: 'confirm_yellow_card',
    1069: 'confirm_yellowred_card',
    1070: 'confirm_red_card',
    1071: 'possible_free_kick',
    1072: 'penalty_shootout_turn',
    1073: 'possible_throw_in',
    1074: 'safe_ball_position',
    1075: 'attack_ball_position',
    1076: 'danger_ball_position',
    1077: 'breakaway_ball_position',
    1078: 'expected_goal',
    1079: 'expected_goal_update',
    1080: 'player_injured',
}

def identify_team_event(event_code):
    if event_code >= 1024 and event_code < 2048 and event_code in EVENT_CODES.keys():
        return {'team': 'home', 'event_type': EVENT_CODES[event_code]}
    elif event_code >= 2048 and event_code < 3072 and event_code - 1024 in EVENT_CODES.keys():
        return {'team': 'away', 'event_type': EVENT_CODES[event_code - 1024]}
    return None
