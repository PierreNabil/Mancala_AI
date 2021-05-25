from .static_eval import static_eval

pinf = float("inf")
ninf = float("-inf")

def minimax(state, depth):
    if depth <= 0 or state.is_terminal():
        return None, static_eval(state)

    if state.player_turn == 0: # maximizer
        value = ninf
        best_move = None

        for move, child in state.children():
            _, child_value = minimax(child, depth-1)
            if child_value > value:
                value = child_value
                best_move = move
        return best_move, value

    else: # player 1: minimizer
        value = pinf
        best_move = None

        for move, child in state.children():
            _, child_value = minimax(child, depth-1)
            if child_value < value:
                value = child_value
                best_move = move
        return best_move, value


def minimax_alpha_beta(state, depth, alpha=ninf, beta=pinf):
    if depth == 0 or state.is_terminal():
        return None, static_eval(state)

    if state.player_turn == 0: # maximizer
        value = ninf
        best_move = None

        for move, child in state.children():
            _, child_value = minimax_alpha_beta(child, depth-1, alpha, beta)
            if child_value > value:
                value = child_value
                best_move = move
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return best_move, value

    else: # player 1: minimizer
        value = pinf
        best_move = None

        for move, child in state.children():
            _, child_value = minimax_alpha_beta(child, depth-1, alpha, beta)
            if child_value < value:
                value = child_value
                best_move = move
            beta = min(beta, value)
            if beta <= alpha:
                break
        return best_move, value