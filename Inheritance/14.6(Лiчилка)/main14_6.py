from collections import deque


def create_circle():
    """
    Creates circle of enumerated players.
    """
    _players = deque()
    _n = int(input('Amount of players, n: '))
    for num in range(1, _n + 1):
        _players.append(num)
    return _players


def game():
    """
    Simulate
    """
    players = create_circle()  # all players
    panel = []  # list of gone players (in order)
    m = int(input("Deleting step, m: "))
    while len(players) > 0:
        for i in range(m - 1):
            players.append(players.popleft())
        panel.append(players.popleft())  # deleting the m-th

    print(" -> ".join(list(map(str, panel))))


if __name__ == "__main__":
    game()
