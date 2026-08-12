"""This is **LeetCode 14 — Longest Common Prefix**.

### Simple Python solution
"""
class Solution:
    def longestCommonPrefix(self, strs):
        prefix = strs[0]

        for word in strs[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]

                if prefix == "":
                    return ""

        return prefix
"""

### How it works

For:

```python
strs = ["flower", "flow", "flight"]
```

Start with:

```text
prefix = "flower"
```

Compare with `"flow"`:

```text
"flower" → "flowe" → "flow"
```

Now compare `"flow"` with `"flight"`:

```text
"flow" → "flo" → "fl"
```

So the answer is:

```text
"fl"
```

### Example 2

```python
strs = ["dog", "racecar", "car"]
```

First comparison gives no common starting character, so:

```text
""
```

### Short version to remember

**Start with the first word as the prefix → compare it with every word → keep removing the last character until it matches.**

**Time:** `O(n × m)`
**Space:** `O(1)`
"""