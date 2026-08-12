"""This is **LeetCode 743 — Network Delay Time**.

The best approach here is **Dijkstra's Algorithm**, because the edge weights (`w`) are positive.

### Python3 solution
"""
import heapq

class Solution:
    def networkDelayTime(self, times, n, k):
        # Create adjacency list
        graph = [[] for _ in range(n + 1)]

        for u, v, w in times:
            graph[u].append((v, w))

        # Min-heap: (time, node)
        heap = [(0, k)]

        # Shortest time to reach each node
        dist = [float('inf')] * (n + 1)
        dist[k] = 0

        while heap:
            time, node = heapq.heappop(heap)

            # Skip outdated information
            if time > dist[node]:
                continue

            for neighbor, weight in graph[node]:
                new_time = time + weight

                if new_time < dist[neighbor]:
                    dist[neighbor] = new_time
                    heapq.heappush(heap, (new_time, neighbor))

        # Ignore index 0
        max_time = max(dist[1:])

        if max_time == float('inf'):
            return -1

        return max_time


"""### Understand the example

```text
times = [[2,1,1], [2,3,1], [3,4,1]]
n = 4
k = 2
```

Starting from node `2`:

```text
2 → 1 = 1
2 → 3 = 1
2 → 3 → 4 = 2
```

So:

```text
Node 1 → 1
Node 2 → 0
Node 3 → 1
Node 4 → 2
```

The **maximum** time is `2`.

Therefore:

```text
Output = 2
```

### Short interview explanation

> Build a graph using an adjacency list. Start from node `k` with time `0` and use a min-heap to always process the node with the smallest known travel time. Whenever we find a shorter path to a neighbor, we update its distance. At the end, the maximum shortest distance is the time required for all nodes to receive the signal. If any node is unreachable, return `-1`.

**Time Complexity:** `O((V + E) log V)`
**Space Complexity:** `O(V + E)`
"""