import pandas as pd

from stats.pbp_processing.rb_soccer.utilities import handle_team_event

TEAM_STATS = [
    'goals',
    'corners',
    'yellow_cards',
    'red_cards',
    'penalties',
    'fouls',
    'free_kicks',
    'dangerous_free_kicks',
    'shots_on_target',
    'shots_off_target',
    'shots_off_woodwork',
    'attacks',
    'dangerous_attacks',
    'offsides',
    'yellowred_cards',      # 2nd yellow is an effective red
    'throw_ins',
    'substitutions',
    'saves',
    'blocks',
    'breakaways',
    'goal_kicks'
]

def empty_team_stats():
    return {
        'home': {stat: 0 for stat in TEAM_STATS},
        'away': {stat: 0 for stat in TEAM_STATS},
    }

def build_team_stats(events, stats=None):
    if stats is None:
        stats = empty_team_stats()
    if len(events) == 0:
        return stats
    if isinstance(events, pd.DataFrame):
        for _, event in events.iterrows():
            # when events are marked as clearedBy, don't include them in the tally!
            if pd.isna(event['clearedBy']):
                stats = handle_team_event(stats, event['EventCodeID'])
    elif isinstance(events, pd.Series):
        event = events
        if pd.isna(event['clearedBy']):
            stats = handle_team_event(stats, event['EventCodeID'])
    return stats
