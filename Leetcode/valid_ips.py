
'''
Given a string of digits, generate all possible valid IP address combinations.

IP addresses must follow the format A.B.C.D, where A, B, C, and D are numbers between 0 and 255. Zero-prefixed numbers, such as 01 and 065, are not allowed, except for 0 itself.
 

EXAMPLE(S)
For example, given "2542540123", you should return ['254.25.40.123', '254.254.0.123'].
 

FUNCTION SIGNATURE
func validIPs(input: String) -> [String]


"0540123", you should return ['0.5.40.123', '0.54.0.123', ...]. '0.54.0.123'

"0.54.0.123'



check path / answer
    have I used all the digits, add answer

choose number or period, build path

choose period
    are there already 3 periods, continue
    if path length is 0, continue
    add . to path
    track last period idx
    track num periods
    proceed with choice (period)

choose digit
    cannot choose a number if preceded by "0"
    test if number with new digit exceeds 255 (num from last index to end of path), if so, continue
    if spaces since last period equals (length of path - index of last period equals 4)
    proceed with choice (digit)
    track number of periods and index of last period

'''

from typing import List

def valid_ips(s: str) -> List[str]:

    answers = []
    n_x = 0

    def helper(path: str, idx_last_p: int, num_p: int, idx_next: int):
        nonlocal n_x
        n_x += 1
        # Check path
        if idx_next == len(s):
            if num_p == 3:
                answers.append(path)
            return

        # Choose period
        if not (num_p == 3 or idx_next == 0 or (path[-1] == ".")):
            helper(path + ".", len(path), num_p + 1, idx_next)

        # Choose digit
        if not (
            len(path) - idx_last_p == 4 or 
            (len(path) and path[-1] == "0") or
            (idx_last_p == -1 and (int(path + s[idx_next]) > 255)) or 
            int(path[idx_last_p+1:] + s[idx_next]) > 255):
            
            helper(path + s[idx_next], idx_last_p, num_p, idx_next + 1)

    helper("", -1, 0, 0)

    print("Total recursive calls:", n_x)
    return answers

def generate_valid_ips(s):
  
  def is_valid(s):
    if s[0] == '0' and len(s) > 1:
        return False
    if int(s) > 255:
        return False
    return True
  
  if len(s) < 4:
    return []
  result = []

  for i in range(1, min(4, len(s))):
    a = s[:i]

    if not is_valid(a):
      continue
    
    
    for j in range(1, min(4, len(s[i:]))):
      b = s[i:i+j]
      if not is_valid(b):
        continue
      for k in range(1, min(4, len(s[i+j:]))):
        c = s[i+j:i+j+k]
        if not is_valid(c):
          continue
        d = s[i+j+k:]
        if not is_valid(d):
          continue
        result.append('{}.{}.{}.{}'.format(a, b, c, d))
  return result

# For example, given "2542540123", you should return ['254.25.40.123', '254.254.0.123'].
print(valid_ips("2542540123"))
print(generate_valid_ips("2542540123"))

# "0540123", you should return ['0.5.40.123', '0.54.0.123', ...]. '0.54.0.123'
print(valid_ips("0540123"))
print(generate_valid_ips("0540123"))

# 0123456
# 123.123

# idx_last_p = 3
# len(path) = 7
# 7 - 3 == 4

# int(path[idx_last_p:] + s[idx_next]) > 255





