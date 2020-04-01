from copy import deepcopy
from stats.pbp_processing.rb_soccer.team_stats import TeamBoxScoreBuilder
from  stats.pbp_processing import event_utilities


class PbpBuilder():

    def __init__(self, pbp_df):
        self.pbp = pbp_df
        self.team_box_score_builder = TeamBoxScoreBuilder(pbp_df)

    def build_pbp(self, max_play_id=float('inf')):
        estimated_box_score = self.team_box_score_builder.build_team_stats(max_play_id=max_play_id)
        new_pbp = deepcopy(self.pbp)
        new_event = event_utilities.event_from_payload(new_pbp)
        for i, box_score in enumerate(new_event['boxscores']):
            team_id = box_score['teamId']
            new_event['boxscores'][i] = estimated_box_score[team_id]
        actions = new_event['pbpDetails']
        new_actions = []
        action = actions[0]
        index = 0
        while index < len(actions) and index < max_play_index and action['playId'] < max_play_id:
            action = actions[index]
            new_actions.append(action)
            index = index + 1
        new_event['pbpDetails'] = new_actions
        if 'event' in new_pbp:
            new_pbp['event'] = new_event
        else:
            new_pbp['league']['season']['eventType'][0]['events'][0] = new_event
        return new_pbp
