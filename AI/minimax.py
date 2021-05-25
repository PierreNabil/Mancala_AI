from .static_eval import static_eval

pinf = float("inf")
ninf = float("-inf")


def minimax(state, depth):
    if depth == 0 or state.is_terminal():
        return static_eval(state)

    if state.player_turn == 0: # maximizer
        value = ninf
        for child in state.children():
            value = max(value, minimax(child, depth-1))
        return value

    else: # player 1: minimizer
        value = pinf
        for child in state.children():
            value = min(value, minimax(child, depth-1))
        return value



def minimax_alpha_beta(state, depth, alpha=ninf, beta=pinf):
    if depth == 0 or state.is_terminal():
        return static_eval(state)

    if state.player_turn == 0: # maximizer
        value = ninf
        for child in state.children():
            value = max(value, minimax_alpha_beta(child, depth-1, alpha, beta))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value

    else: # player 1: minimizer
        value = pinf
        for child in state.children():
            value = min(value, minimax_alpha_beta(child, depth-1, alpha, beta))
            beta = min(beta, value)
            if beta <= alpha:
                break
        return value