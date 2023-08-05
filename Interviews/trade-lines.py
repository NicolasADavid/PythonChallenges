# // A Credit Report contains a list of tradelines (essentially a list of any loan or an available line of credit that a person has). Each tradeline has a code and subcode which describes the type of liability. For example, all credit cards have a code of '12', a conventional mortgage has a code of '10' and a subcode of '12'. Each tradeline also has a monthly payment and a current balance. Some tradelines may not carry a balance - for example, a fully paid off credit card.

# // Sample of tradelines in a credit report:

# // reported-date code subcode monthly-payment current-balance
# // 2015-10-10    10       12  $1470.31        $659218.00
# // 2015-10-10     5        1  $431.98         $51028.00
# // 2015-10-09     8       15  $340.12         $21223.20
# // 2015-10-10    10       15  $930.12         $120413.00
# // 2015-10-09    12        5  $150.50         $6421.21
import asyncio
# // Part 1: Calculate the total of credit card payments made in October 2015?

input = [["2015-10-10", "10", "12", "$1470.31", "$659218.00"],
["2015-10-10", "5", "1", "$431.98", "$51028.00"],
["2015-10-09", "8", "15", "$340.12", "$21223.20"],
["2015-10-10", "10", "15", "$930.12", "$120413.00"],
["2015-10-09", "12", "5", "$150.50", "$6421.21"],
["2015-10-09", "12", "5", "$150.50", "$6421.21"],
["2015-10-09", "12", "5", "$150.50", "$6421.21"]]

from typing import List

def getTotalPayments(tradeLines: List[List[str]], filterCode: str, filterSubcode: List[str], filterYear: str, filterMonth: str = "", filterDay: str = "") -> float:

    total = 0

    for tradeLine in tradeLines:
        date, code, subcode, monthly, balance = tradeLine
        year, month, day = date.split("-")

        # filter by date
        # year
        # month
        # day

        # filter by code

        # filter by subcode(s)

        if code == filterCode and year == filterYear and month == filterMonth:
            total = total + float(monthly.replace("$", ""))

    return total

def getYearlyHousingExpense(tradelines: List[List[str]], filterCode: str, filterSubcodes: List[str], filterYear: str, default: float = 0) -> float:

    monthsSeen = set()

    total = 0

    for tradeLine in tradelines:
        date, code, subcode, monthly, _ = tradeLine
        year, month, _ = date.split("-")

        if code == filterCode and subcode in filterSubcodes and year == filterYear:
            total = total + float(monthly.replace("$", ""))
            monthsSeen.add(month)

    for i in range(1, 13):
        if str(i) not in monthsSeen:
            total = total + default

    return total

def getMaxMonthlyHousingExpense(tradelines: List[List[str]], filterCode: str, filterSubcodes: List[str], filterYear: str, default: float = 0) -> float:

    best = 0

    for tradeLine in tradelines:
        date, code, subcode, monthly, _ = tradeLine
        year, month, _ = date.split("-")

        if code == filterCode and subcode in filterSubcodes and year == filterYear:
            best = max(best, float(monthly.replace("$", "")))

    return max(best, default)


#print(getTotalPayments(input, "12", [], "2015", "10"))

# provide just a year -> caclulate total including all months. Use default for months with no data.
# provide multiple subcodes

# // What is the total housing expense in 2015?
#print(getYearlyHousingExpense(input, "10", ["12", "15"], "2015", 1061))

# // Housing Expense is the sum of monthly payments for all mortgage tradelines, where a mortgage tradeline has a code of 10 and a subcode of 12 or 15. If the credit report contains no mortgage tradelines, then the program should assume a housing expense of $1061 (the national average monthly rent).

#print(getMaxMonthlyHousingExpense(input, "10", ["12", "15"], "2015", 1061))
# // Implement the logic to calculate the highest monthly housing expense in 2015?

# To make working with trade-in classifications easier, a new API was developed that could take a code or a code and a subcode and return an array of strings describing all categories that it belongs to.

# For example, passing a code of 12 will return ['credit_card'] while passing a code of 10 and a submode of 15 will return ['housing', 'mortgage'] (both the category and specific tradeline type)

# Use the below mock API using the previously discussed code classifications to allow your previous solutions to specify 'credit_card' or 'mortgage' as inputs, rather than the codes and subcodes

def getTotalYearlyCreditPayments():
    pass

async def getMaxMonthlyExpenseByType(tradeLines, filterType: str, filterYear: str, default: float):

    apicache = {}

    best = 0

    for tradeLine in tradeLines:
        date, code, subcode, monthly, _ = tradeLine
        year, _, _ = date.split("-")

        if (code, subcode) in apicache:
            print('cache hit for ' + str(code) + ', ' + str(subcode))
            tradeLineType = apicache[(code, subcode)]
        else:
            tradeLineType = await api(int(code), int(subcode))
            apicache[(code, subcode)] = tradeLineType

        print(tradeLineType)

        if filterType in tradeLineType and year == filterYear:
            best = max(best, float(monthly.replace("$", "")))

    return max(best, default)

async def api(code, subcode = None):
    print('cache miss for ' + str(code) + ', ' + str(subcode))
    if code == 12:
        return ['credit_card']
    elif code == 10 and (subcode == 12 or subcode == 15):
        return ['housing','mortgage']
    else:
        return ['other']

print(asyncio.run(getMaxMonthlyExpenseByType(input, "housing", "2015", 1061)))


# from typing import List

# # import os
# # ld = os.listdir()
# # print(ld)

# File_object = open(r"Interviews/trade-lines.txt","r")
# filelines = File_object.readlines()
# File_object.close()

# tradeLines = []

# def sumLinesBalance(tradeLines: List[str]):
#     return sum(float(currentbalance.replace("$", "")) for reporteddate, code, subcode, monthlypayment, currentbalance in tradeLines)


# for fileline in filelines:
#     tokens = fileline.replace("\n", "").split(" ")
#     [reporteddate, code, subcode, monthlypayment, currentbalance] = tokens
#     tradeLines.append((reporteddate, code, subcode, monthlypayment, currentbalance))

# creditLines = []
# mortgageLines = []
# otherLines = []

# for tradeLine in tradeLines:
#     if tradeLine[1] == "12":
#         creditLines.append(tradeLine)
#     elif tradeLine[1] == "10" and tradeLine[2] == "12":
#         mortgageLines.append(tradeLine)
#     else:
#         otherLines.append(tradeLine)

# def printHeaders():
#     print("reporteddate \t code \t subcode \t monthlypayment \t currentbalance \t"),
#     print("\n")


# print("creditLines: ")
# printHeaders()
# for line in creditLines:
#     print(line)
#     # for token in line:
#     #     print(token, "\t"),
# print("total: ", sumLinesBalance(creditLines))
# print("\n")

# print("mortgageLines: ")
# printHeaders()
# for line in mortgageLines:
#     print(line)
#     # for token in line:
#     #     print(token, "\t"),
# print("total: ", sumLinesBalance(mortgageLines))
# print("\n")

# print("otherLines: ")
# printHeaders()
# for line in otherLines:
#     print(line)
#     # for token in line:
#     #     print(token, "\t"),
# print("total: ", sumLinesBalance(otherLines))
# print("\n")

# print("")