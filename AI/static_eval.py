def static_eval(state):
    #TODO: make better static evals
    return basic_eval(state)

def basic_eval(state):
    value = 0
    for i in range(6):
        if state.state[i] == 0:
            value += 1
    for i in range(7,13):
        if state.state[i] == 0:
            value -= 1

    return value