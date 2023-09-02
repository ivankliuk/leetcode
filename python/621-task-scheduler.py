"""
621. Task Scheduler
===================
You are given an array of CPU tasks, each represented by letters A to Z, and a cooling time, n. Each cycle or interval
allows the completion of one task. Tasks can be completed in any order, but there's a constraint: identical tasks
must be separated by at least n intervals due to cooling time.

Return the minimum number of intervals required to complete all tasks.

Example 1:
----------
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.
After completing task A, you must wait two cycles before doing A again. The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. By the 4th cycle, you can do A again as 2 intervals have passed.

Example 2:
----------
Input: tasks = ["A","C","A","B","D","B"], n = 1
Output: 6
Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.
With a cooling interval of 1, you can repeat a task after just one other task.

Example 3:
----------
Input: tasks = ["A","A","A", "B","B","B"], n = 3
Output: 10
Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.
There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads to idling twice
between repetitions of these tasks.

Constraints:
------------
1 <= tasks.length <= 10^4
tasks[i] is an uppercase English letter.
0 <= n <= 100
"""
from collections import Counter
from typing import List


class Solution:
    """
    Algorithm
    ---------
    Obviously, the input order doesn't matter. We schedule tasks with the biggest amount first.

    Tasks = A A A B B B, n = 2
    Max frequency is A which occurs 3 times.
    A _ _ A _ _ A
    B occurs 3 times as well:
    A B _ A B _ A (One B remains unscheduled)
    So we need one more intervals to schedule B:
    A B _ A B _ A B
    Total intervals: 8

    Tasks = A C A B A D, A, D, n = 3
    Max frequency is A which occurs 4 times.
    A _ _ _ A _ _ _ A _ _ _ A
    A B _ _ A _ _ _ A _ _ _ A
    A B C _ A _ _ _ A _ _ _ A
    A B C D A _ _ _ A _ _ _ A
    A B C D A _ _ D A _ _ _ A
    Total intervals: 13

    Tasks = A A A A B B B B C C C C D D D E E F, n = 3
    Max frequency is A which occurs 4 times.
    A _ _ _ A _ _ _ A _ _ _ A
    B occurs 4 times as well:
    A B _ _ A B _ _ A B _ _ A (One B remains unscheduled)
    Counter occurs 4 times to:
    A B C _ A B C _ A B C _ A (One C remains unscheduled)
    So we need two more intervals to schedule B and C:
    A B C _ A B C _ A B C _ A B C
    A B C D A B C D A B C D A B C
    A B C D A B C D A B C D A B C E
    Now we are safe insert tasks between groups due to distance between As, Bs, Cs or Ds
    increases by 1, and we do care about only being greater or equals to 3:
    A B C D E A B C D F A B C D A B C E
    Total intervals: 18 which is the task list length.

    Complexity Analysis
    -------------------
    Time complexity O(n * log(n)).
    Space complexity O(n). Because sorting in place takes additional space.
    """

    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequencies = sorted(Counter(tasks).values(), reverse=True)
        max_freq = frequencies[0]

        counter = 0
        i = 0
        while i <= len(frequencies) - 1 and max_freq == frequencies[i]:
            counter += 1
            i += 1

        intervals = (max_freq - 1) * (n + 1) + counter
        return max(intervals, len(tasks))
