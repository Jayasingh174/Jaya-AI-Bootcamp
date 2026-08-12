"""This is a **Longest Good Subarray** problem. The best approach is **Sliding Window + Hash Map**.

### Python solution
"""
class Solution:
    def maxSubarrayLength(self, nums, k):
        count = {}
        left = 0
        answer = 0

        for right in range(len(nums)):
            count[nums[right]] = count.get(nums[right], 0) + 1

            while count[nums[right]] > k:
                count[nums[left]] -= 1
                left += 1

            answer = max(answer, right - left + 1)

        return answer
"""
### How it works

For:

```text
nums = [1,2,3,1,2,3,1,2]
k = 2
```

We maintain a window:

```text
left ----------------> right
```

and a dictionary:

```python
count = {
    1: frequency,
    2: frequency,
    3: frequency
}
```

Whenever an element occurs **more than `k` times**, move `left` forward until the window becomes valid again.

For the example:

```text
[1,2,3,1,2,3]
```

frequencies are:

```text
1 → 2
2 → 2
3 → 2
```

Everything is valid, so:

```text
answer = 6
```

### Why `while` instead of `if`?

This is important:

```python
while count[nums[right]] > k:
```

We may need to remove **multiple elements** from the left before the subarray becomes valid.

### Complexity

```text
Time:  O(n)
Space: O(n)
```

Each element enters the window once and leaves the window at most once.

**Pattern to remember for interviews:**
**"Longest/maximum contiguous subarray + frequency condition" → Sliding Window + Hash Map.**
"""