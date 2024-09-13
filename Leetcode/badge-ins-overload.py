'''

You are in charge of a display advertising program. Your ads are displayed on websites all over the internet. You have some CSV input data that counts how many times that users have clicked on an ad on each individual domain. Every line consists of a click count and a domain name, like this:


counts = [ "900,google.com",
    "60,mail.yahoo.com",
    "10,mobile.sports.yahoo.com",
    "40,sports.yahoo.com",
    "300,yahoo.com",
    "10,stackoverflow.com",
    "20,overflow.com",
    "5,com.com",
    "2,en.wikipedia.org",
    "1,m.wikipedia.org",
    "1,mobile.sports",
    "1,google.co.uk"]


Write a function that takes this input as a parameter and returns a data structure containing the number of clicks that were recorded on each domain AND each subdomain under it. For example, a click on "mail.yahoo.com" counts toward the totals for "mail.yahoo.com", "yahoo.com", and "com". (Subdomains are added to the left of their parent domain. So "mail" and "mail.yahoo" are not valid domains. Note that "mobile.sports" appears as a separate domain near the bottom of the input.)


Sample output (in any order/format):


calculateClicksByDomain(counts) =>
com:                     1345
google.com:              900
stackoverflow.com:       10
overflow.com:            20
yahoo.com:               410
mail.yahoo.com:          60
mobile.sports.yahoo.com: 10
sports.yahoo.com:        50
com.com:                 5
org:                     3
wikipedia.org:           3
en.wikipedia.org:        2
m.wikipedia.org:         1
mobile.sports:           1
sports:                  1
uk:                      1
co.uk:                   1
google.co.uk:            1


n: number of domains in the input
(individual domains and subdomains have a constant upper length)


'''
from typing import List
from collections import defaultdict
def calculateClicksByDomain(counts: List[str]) -> dict:

    countdict = defaultdict(int)

    for count in counts:

        clickcount, domain = count.split(",")
        domainElements = domain.split(".")

        for i in range(len(domainElements)):
            key = ".".join(domainElements[i:])
            countdict[key] += int(clickcount)
    
    return countdict

d = calculateClicksByDomain(counts = [ "900,google.com",
    "60,mail.yahoo.com",
    "10,mobile.sports.yahoo.com",
    "40,sports.yahoo.com",
    "300,yahoo.com",
    "10,stackoverflow.com",
    "20,overflow.com",
    "5,com.com",
    "2,en.wikipedia.org",
    "1,m.wikipedia.org",
    "1,mobile.sports",
    "1,google.co.uk"])

# for key in d.keys():
#     print("key: ", key)
#     print("count: ", d[key])

# print("length: ", len(d.keys()))



'''

You are a developer for a university. Your current project is to develop a system for students to find courses they share with friends. The university has a system for querying courses students are enrolled in, returned as a list of (ID, course) pairs.
Write a function that takes in a list of (student ID number, course name) pairs and returns, for every pair of students, a list of all courses they share.

Sample Input:

student_course_pairs_1 = [
  ["58", "Software Design"],
  ["58", "Linear Algebra"],
  ["94", "Art History"],
  ["94", "Operating Systems"],
  ["17", "Software Design"],
  ["58", "Mechanics"],
  ["58", "Economics"],
  ["17", "Linear Algebra"],
  ["17", "Political Science"],
  ["94", "Economics"],
  ["25", "Economics"],
]

Sample Output (pseudocode, in any order):

find_pairs(student_course_pairs_1) =>
{
  [58, 17]: ["Software Design", "Linear Algebra"]
  [58, 94]: ["Economics"]
  [58, 25]: ["Economics"]
  [94, 25]: ["Economics"]
  [17, 94]: []
  [17, 25]: []
}

Additional test cases:

Sample Input:

student_course_pairs_2 = [
  ["42", "Software Design"],
  ["0", "Advanced Mechanics"],
  ["9", "Art History"],
]

Sample output:

find_pairs(student_course_pairs_2) =>
{
  [0, 42]: []
  [0, 9]: []
  [9, 42]: []
}

'''

def find_pairs(student_course_pairs: List[List[str]]):

    student_ids = set()
    student_course = defaultdict(set)

    for student_course_pair in student_course_pairs:
        student_id = student_course_pair[0]
        course = student_course_pair[1]

        student_ids.add(student_id)
        student_course[student_id].add(course)
    
    student_id_pairs = [(i, j) for i in student_ids for j in student_ids if i != j and i < j]

    output = defaultdict(list)

    for student_id_pair in student_id_pairs:

        # Ensure k/v initialized for every pair
        output[student_id_pair]

        # Every course student 1 attends
        for course in student_course[student_id_pair[0]]:

            # If student 2 attends as well, collect
            if course in student_course[student_id_pair[1]]:
                output[student_id_pair].append(course)

    return output

# T: O(N^2)
# S: O(N^2 * C)

student_course_pairs_1 = [
  ["58", "Software Design"],
  ["58", "Linear Algebra"],
  ["94", "Art History"],
  ["94", "Operating Systems"],
  ["17", "Software Design"],
  ["58", "Mechanics"],
  ["58", "Economics"],
  ["17", "Linear Algebra"],
  ["17", "Political Science"],
  ["94", "Economics"],
  ["25", "Economics"],
]

c = find_pairs(student_course_pairs_1)

for key in c.keys():
    print("key: ", key)
    print("val: ", c[key])

print("Len: ", len(c.keys()))



'''


We are working on a security system for a badged-access room in our company's building.
We want to find employees who badged into our secured room unusually often. We have an unordered list of names and entry times over a single day. Access times are given as numbers up to four digits in length using 24-hour time, such as "800" or "2250".
Write a function that finds anyone who badged into the room three or more times in a one-hour period. Your function should return each of the employees who fit that criteria, plus the times that they badged in during the one-hour period. If there are multiple one-hour periods where this was true for an employee, just return the earliest one for that employee.


badge_times = [
["Paul", "1355"],
["Jennifer", "1910"],
["John", "835"],
["John", "830"],
["Paul", "1315"],
["John", "1615"],
["John", "1640"],
["Paul", "1405"],
["John", "855"],
["John", "930"],
["John", "915"],
["John", "730"],
["John", "940"],
["Jennifer", "1335"],
["Jennifer", "730"],
["John", "1630"],
["Jennifer", "5"]
]
Expected output (in any order)
John: 830 835 855 915 930
Paul: 1315 1355 1405
n: length of the badge records array


Make a list of all times an employee badged in
Sort that list

Slide a window through that list
Keep adding times to the list
Remove earlier times if difference t[-1] - t[0] >= 60
If len(window) == 3, set flag
If window len will shorten after flag set, capture window at that point

'''


def badge_times_overload(badge_times) -> List[str]:

    employee_badge_times = defaultdict(list)
    for [employee, badge_time] in badge_times:
        # Populate dictionary employee -> List[badge_times]
        employee_badge_times[employee].append(int(badge_time))

    # Sort the lists
    for key in employee_badge_times.keys():
        employee_badge_times[key] = sorted(employee_badge_times[key])

    output = []

    for key in employee_badge_times.keys():

        badge_times_sorted = employee_badge_times[key]

        start = 0
        end = -1

        flag = False
        answered = False

        while end < len(badge_times_sorted) and not answered:

            # Expand
            end += 1

            if end - start == 2:
                # Have a window that is valid, continue collecting all badge-ins that are part of this window
                flag = True

            def addOutput():
                nonlocal answered
                output.append([key, badge_times_sorted[start: end+1]])
                answered = True

            # Reached end of input
            if end == len(badge_times_sorted):
                if flag:
                    addOutput()
                break
                    

            # Contract
            while start != end and badge_times_sorted[end] - badge_times_sorted[start] >= 100:

                # Check flag. Want earliest window with 3+ badge check ins. Want as many check-ins as possible.
                if flag:
                    addOutput()
                    break
                
                start += 1

    return output

badge_times = [
["Paul", "1355"],
["Jennifer", "1910"],
["John", "835"],
["John", "830"],
["Paul", "1315"],
["John", "1615"],
["John", "1640"],
["Paul", "1405"],
["John", "855"],
["John", "930"],
["John", "915"],
["John", "730"],
["John", "940"],
["Jennifer", "1335"],
["Jennifer", "730"],
["John", "1630"],
["Jennifer", "5"]
]
print(badge_times_overload(badge_times))



