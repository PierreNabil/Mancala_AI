
def static_eval(game_state):
    if game_state.is_terminal():
        if game_state.state[6] > game_state.state[13]:
            value = 100
        elif game_state.state[6] == game_state.state[13]:
            value = 0
        else:
            value = -100        
    else:
        value = game_state.state[6] - game_state.state[13]
    return value