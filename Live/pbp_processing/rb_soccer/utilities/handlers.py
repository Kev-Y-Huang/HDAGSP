def increase_counts(running_stats, team, stats_to_update):
    for stat in stats_to_update:
        running_stats[team][stat] += 1
    return running_stats

def decrease_counts(running_stats, team, stats_to_update):
    for stat in stats_to_update:
        running_stats[team][stat] -= 1
    return running_stats

def handle_attack(stats, team):
    return increase_counts(stats, team, ['attacks'])

def handle_goal(stats, team):
    return increase_counts(stats, team, ['goals'])

def handle_cancel_goal(stats, team):
    return decrease_counts(stats, team, ['goals'])

def handle_shot_on_target(stats, team):
    return increase_counts(stats, team, ['shots_on_target'])

def handle_shot_off_target(stats, team):
    return increase_counts(stats, team, ['shots_off_target'])

def handle_shot_off_woodwork(stats, team):
    return increase_counts(stats, team, ['shots_off_woodwork'])

def handle_corner(stats, team):
    return increase_counts(stats, team, ['corners'])

def handle_cancel_corner(stats, team):
    return decrease_counts(stats, team, ['corners'])

def handle_free_kick(stats, team):
    return increase_counts(stats, team, ['free_kicks'])

def handle_dangerous_free_kick(stats, team):
    return increase_counts(stats, team, ['dangerous_free_kicks'])

def handle_dangerous_attack(stats, team):
    return increase_counts(stats, team, ['dangerous_attacks'])

def handle_yellow_card(stats, team):
    return increase_counts(stats, team, ['yellow_cards'])

def handle_cancel_yellow_card(stats, team):
    return decrease_counts(stats, team, ['yellow_cards'])

def handle_red_card(stats, team):
    return increase_counts(stats, team, ['red_cards'])

def handle_cancel_red_card(stats, team):
    return decrease_counts(stats, team, ['red_cards'])

def handle_yellowred_card(stats, team):
    return increase_counts(stats, team, ['yellowred_cards'])

def handle_cancel_yellowred_card(stats, team):
    return decrease_counts(stats, team, ['yellowred_cards'])

def handle_foul(stats, team):
    return increase_counts(stats, team, ['fouls'])

def handle_penalty(stats, team):
    return increase_counts(stats, team, ['penalties'])

def handle_cancel_penalty(stats, team):
    return decrease_counts(stats, team, ['penalties'])

def handle_offside(stats, team):
    return increase_counts(stats, team, ['offsides'])

def handle_throw_in(stats, team):
    return increase_counts(stats, team, ['throw_ins'])

def handle_substitution(stats, team):
    return increase_counts(stats, team, ['substitutions'])

def handle_save(stats, team):
    return increase_counts(stats, team, ['saves'])

def handle_block(stats, team):
    return increase_counts(stats, team, ['blocks'])

def handle_breakaway(stats, team):
    return increase_counts(stats, team, ['breakaways'])

def handle_goal_kick(stats, team):
    return increase_counts(stats, team, ['goal_kicks'])
