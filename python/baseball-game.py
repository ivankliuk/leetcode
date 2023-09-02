from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        i = 0
        record = []

        while i <= len(operations) - 1:
            if operations[i] == "+":
                record.append(record[-1] + record[-2])
            elif operations[i] == "D":
                record.append(record[-1] * 2)
            elif operations[i] == "C":
                record.pop()
            else:
                record.append(int(operations[i]))

            i += 1

        result = sum(record)
        return result
