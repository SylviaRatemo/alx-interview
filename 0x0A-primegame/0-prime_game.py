#!/usr/bin/python3
"""
isWinner function
    : Ben or Maria
    : Prime Game
"""


def isWinner(x, nums):
    """Prime Game
    """
    
    def is_prime(num):
        """Check if a number is prime."""
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_available_moves(numbers):
        """Get a list of available prime numbers from the given set."""
        return [num for num in numbers if is_prime(num)]

    def play_game(numbers):
        """Simulate the game and return the winner."""
        current_player = "Maria"
        while True:
            available_moves = get_available_moves(numbers)
            if not available_moves:
                return current_player  # No more moves, current player wins
            selected_move = min(available_moves)
            numbers = [num for num in numbers if num % selected_move != 0]
            current_player = "Maria" if current_player == "Ben" else "Ben"

    # Count the number of wins for each player
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_game(list(range(1, n + 1)))
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
