from functools import partial

from stats.pbp_processing.rb_soccer.utilities.handlers import (
    handle_attack,
    handle_goal,
    handle_cancel_goal,
    handle_shot_on_target,
    handle_shot_off_target,
    handle_shot_off_woodwork,
    handle_corner,
    handle_cancel_corner,
    handle_free_kick,
    handle_dangerous_free_kick,
    handle_dangerous_attack,
    handle_yellow_card,
    handle_cancel_yellow_card,
    handle_red_card,
    handle_cancel_red_card,
    handle_yellowred_card,
    handle_cancel_yellowred_card,
    handle_foul,
    handle_penalty,
    handle_cancel_penalty,
    handle_offside,
    handle_throw_in,
    handle_substitution,
    handle_save,
    handle_block,
    handle_breakaway,
    handle_goal_kick,
    handle_save,
)
from stats.pbp_processing.rb_soccer.utilities.identifiers import identify_team_event


HANDLERS = {
    'attack': handle_attack,
    'goal': handle_goal,
    'cancel_goal': handle_cancel_goal,
    'shot_on_target': handle_shot_on_target,
    'shot_off_target': handle_shot_off_target,
    'shot_off_woodwork': handle_shot_off_woodwork,
    'corner': handle_corner,
    'cancel_corner': handle_cancel_corner,
    'free_kick': handle_free_kick,
    'dangerous_free_kick': handle_dangerous_free_kick,
    'dangerous_attack': handle_dangerous_attack,
    'yellow_card': handle_yellow_card,
    'cancel_yellow_card': handle_cancel_yellow_card,
    'red_card': handle_red_card,
    'cancel_red_card': handle_cancel_red_card,
    'yellowred_card': handle_yellowred_card,
    'cancel_yellowred_card': handle_cancel_yellowred_card,
    'foul': handle_foul,
    'penalty': handle_penalty,
    'cancel_penalty': handle_cancel_penalty,
    'offside': handle_offside,
    'throw_in': handle_throw_in,
    'substitution': handle_substitution,
    'save': handle_save,
    'block': handle_block,
    'breakaway': handle_breakaway,
    'goal_kick': handle_goal_kick,
    'save': handle_save,
}

def handle_team_event(stats, event_code):
    event_info = identify_team_event(event_code)
    if event_info and event_info['event_type'] in HANDLERS.keys():
        return HANDLERS[event_info['event_type']](stats, event_info['team'])
    return stats
