import re, sys
from collections import deque

def flagSuspiciousRequests(restrictedKeys, accessRequests):
    compiled = [re.compile('^' + re.escape(p).replace(r'\*', '.*') + '$') for p in restrictedKeys]
    recent, flagged = {}, [0] * len(accessRequests)
    
    for i, key in enumerate(accessRequests):
        if any(rgx.match(key) for rgx in compiled):
            flagged[i] = 1
            continue
        dq = recent.setdefault(key, deque())
        while dq and i - dq[0] >= 5:
            dq.popleft()
        if dq:
            flagged[i] = 1
        else:
            dq.append(i)
    
    return flagged


# ------------------------
# Sample Case 0
restrictedKeys0 = ["111.*.255", "12."]
accessRequests0 = [
    "121.3.5.255",
    "12.13.5.255",
    "111.3.5.255",
    "121.3.5.255"
]
print(flagSuspiciousRequests(restrictedKeys0, accessRequests0))
# Expected Output: [0, 0, 1, 0]

# ------------------------
# Sample Case 1
restrictedKeys1 = ["111.111.1.1"]
accessRequests1 = ["111.111.1.1"]
print(flagSuspiciousRequests(restrictedKeys1, accessRequests1))
# Expected Output: [1]