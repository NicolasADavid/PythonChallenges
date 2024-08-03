from typing import List, Tuple
def calculate_tax(taxable_income: float, brackets: List[Tuple[float, float, float]]) -> float:

    if not brackets:
        return 0
    
    non_taxable = brackets[0][0]

    taxable_income -= non_taxable
    total_tax = 0

    for bracket in brackets:

        amt_applicable_bracket = bracket[1] - bracket[0]
        rate = bracket[2]

        if taxable_income > amt_applicable_bracket:
            # taxable income exceeds the upper limit of this bracket, apply full tax of bracket
            total_tax += amt_applicable_bracket * rate
            taxable_income -= amt_applicable_bracket
        else:
            #taxable income falls within limits of this bracket, apply rate to all of remaining taxable income
            total_tax += taxable_income * rate
            break

    return round(total_tax, 2)

assert calculate_tax(100000, [(0, 10000, 0.10), (10000, 30000, 0.15), (30000, 60000, 0.25), (60000, float('inf'), 0.35)]) == 25500
assert calculate_tax(0, [(0, 10000, 0.10), (10000, 30000, 0.15), (30000, 60000, 0.25), (60000, float('inf'), 0.35)]) == 0
assert calculate_tax(5000, [(0, 10000, 0.10), (10000, 30000, 0.15), (30000, 60000, 0.25), (60000, float('inf'), 0.35)]) == 500
