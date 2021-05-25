
def static_eval(game_state):
    #TODO: make better static evals
    return basic_eval(game_state)



def basic_eval(game_state):
    if game_state.is_terminal():
        value = 100 if game_state.state[6] > game_state.state[13] else -100
    else:
        value = game_state.state[6] - game_state.state[13]
    return value