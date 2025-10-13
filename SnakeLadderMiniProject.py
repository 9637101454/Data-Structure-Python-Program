import random
import time
from collections import deque

snakes = {99: 5, 70: 24, 55: 23}
ladders = {6: 25, 11: 45, 60: 84, 46: 90}

def apply_snake_or_ladder(pos):
    if pos in snakes:
        return snakes[pos], 'snake'
    elif pos in ladders:
        return ladders[pos], 'ladder'
    return pos, None

def bfs_min_path():
    visited = [False] * 101
    parent = [-1] * 101
    queue = deque()

    queue.append((1, 0)) 
    visited[1] = True

    while queue:
        pos, throws = queue.popleft()

        if pos == 100:
            path = []
            while pos != -1:
                path.append(pos)
                pos = parent[pos]
            path.reverse()
            return throws, path

        for dice in range(1, 7):
            next_pos = pos + dice
            if next_pos <= 100:
                final_pos, _ = apply_snake_or_ladder(next_pos)
                if not visited[final_pos]:
                    visited[final_pos] = True
                    parent[final_pos] = pos
                    queue.append((final_pos, throws + 1))

    return -1, []

def play_game():
    print(" Welcome to Snakes & Ladders!")
    print("-----------------------------------")
    print("Goal: Reach 100 before the snakes bite! \n")
    print("Press [Enter] to roll the dice | Type 'q' to quit.\n")

    curr_pos = 1
    time.sleep(1)

    while curr_pos < 100:
        user_input = input(" Your move -> ").strip().lower()
        if user_input == 'q':
            print("Game ended! Final position:", curr_pos)
            return

        roll = random.randint(1, 6)
        print(f" You rolled a {roll}!")

        next_pos = curr_pos + roll
        if next_pos > 100:
            print(" Roll too high, you stay at the same position.")
            continue

        final_pos, event = apply_snake_or_ladder(next_pos)

        if event == 'ladder':
            print(f" Ladder! You climbed from {next_pos} to {final_pos}.")
        elif event == 'snake':
            print(f" Snake! You slid down from {next_pos} to {final_pos}.")
        else:
            print(f"You move to {final_pos}.")

        curr_pos = final_pos

        print(f" Current Position: {curr_pos}\n")
        time.sleep(0.7)

    print("\n Congratulations! You reached 100!")

    throws, path = bfs_min_path()
    print("\n According to BFS:")
    print(f" Minimum dice throws possible: {throws}")
    print(f" Shortest path: {' → '.join(map(str, path))}")

if __name__ == "__main__":
    play_game()