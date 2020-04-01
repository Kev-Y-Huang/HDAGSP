def ratio(dictionary,  target, numerator, denominator, percent=True):
    scale = 100 if percent else 1
    if dictionary[denominator] > 0:
        dictionary[target] = round(dictionary[numerator]/dictionary[denominator] * scale, 1)
    else:
        dictionary[target] = 0

def increment(dictionary, key, inc=1.0):
    dictionary[key] = dictionary[key] + inc

def set_max(dictionary, key, value):
    dictionary[key] = max(dictionary[key], value)

def find_player(players, player_id, create_function=None):
    for player in players:
        if player['player']['playerId'] == player_id:
            return player
    if create_function:
        players.append(create_function(player_id))
        return players[-1]

def event_from_payload(payload):
    if 'event' in payload:
        return payload['event']
    else: 
        return payload['league']['season']['eventType'][0]['events'][0]
