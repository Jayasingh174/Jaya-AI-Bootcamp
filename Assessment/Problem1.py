"""This is the LeetCode **Student Attendance Record I** problem.

### Approach

The student is eligible only if:

1. Total `'A'` is **less than 2** → at most 1 absence.
2. There are **never 3 consecutive `'L'`**.

### Python solution
"""
class Solution:
    def checkRecord(self, s: str) -> bool:
        # More than 1 absence
        if s.count('A') >= 2:
            return False

        # 3 consecutive late days
        if 'LLL' in s:
            return False

        return True
    
"""### Example

```text
s = "PPALLP"

A count = 1
LLL present? No

Output: True
```

```text
s = "PPALLL"

A count = 1
LLL present? Yes

Output: False
```

### Short interview explanation

> Count the number of `A`. If it is 2 or more, return `False`. Then check whether `"LLL"` occurs in the string. If it does, return `False`. Otherwise, return `True`.

**Time:** `O(n)`
**Space:** `O(1)`"""
