'''
You are given a list of strings data, where each string is in the form "$device_id,$usage_in_minutes", such that $device_id contains exactly five lowercase English letters ('a'-'z') and $usage_in_minutes contains exactly four digits, representing a positive integer between 1 and 1440 (possibly with leading zeroes).

For instance, "abxyz,0010" describes $device_id = "abxyz" and $usage_in_minutes = 10 minutes.

Given data, your task is to return the $device_id with the largest value of $usage_in_minutes. You may assume that all values of $device_id and $usage_in_minutes' are both pairwise distinct in data.

Example

For

data = ["iqttt,0077",
        "obvhd,0093",
        "flohd,0075"]
the output should be solution(data) = "obvhd".

There are 3 devices:

$device_id = "iqttt" and $usage_in_minutes = 77 minutes;
$device_id = "obvhd" and $usage_in_minutes = 93 minutes;
$device_id = "flohd" and $usage_in_minutes = 75 minutes.
'''

def solution(data):

    ans = None
    best = float('-inf')
    
    for d in data:
        device, usage = d.split(",")

        while usage[0] == "0":
            usage = usage[1:]
        usage = int(usage)

        if best < usage:
            best = usage
            ans = device
    
    return ans


print(solution(data = ["iqttt,0077",
        "obvhd,0093",
        "flohd,0075"]))