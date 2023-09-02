class Solution:
    def judgeCircle(self, moves: str) -> bool:
        pos = [0, 0]

        for move in moves:
            if move == "R":
                pos[0] += 1
            elif move == "L":
                pos[0] -= 1
            elif move == "U":
                pos[1] += 1
            elif move == "D":
                pos[1] -= 1

        return pos == [0, 0]
