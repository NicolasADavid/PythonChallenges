'''
❓ PROMPT
Check whether the string s is a balanced chemical equation. The equation represents a chemical reaction that changes matter from one form to another,
and since matter cannot be destroyed, valid equations must be balanced. Matter is made of molecules, and molecules are made of atoms. A balanced equation means that both sides have the same number of every atom.

An atom is a string that starts with an uppercase English letter followed by some or no lowercase English letters. For example, "A" and "Abc" are 1 atom each, but "FG" is 2 atoms, "F" and "G", and "hello" is invalid. 

A molecule is one or more atoms next to each other with no spaces between. HO is a molecule consisting of a single hydrogen and single oxygen atom. An atom in a molecule may be followed by a 
number which indicates the number of times that atom occurs in the molecule, so H2O is two hydrogens and one oxygen.

In an equation, a molecule can optionally be prefixed with a molecule coefficient that indicates the number of those molecules available. So 2H2O means two molecules, so a total of 4 hydrogen and one oxygen.

The chemical equation itself is then is a string in the following format: molecule (+ molecule)* = molecule (+ molecule)*, where " * " means it repeats 0+ times.

For example, "A = B", "A = B + C", and "A + B + C = D + E + F" are chemical equations but "X + Y = ", "X = + Z" are not.

Example(s)
For s = "2H2 + O2 = 2H2O", the output is True.
Left side: 4 * "H" and "2 * O"
Right side: 4 * "H" and "2 * O"

For s = "1000H2O = Au + Ag", the output is False.
Left side: 2000 * "H" and "1000 * O"
Right side: 1 * "Ag" and "1 * Au"
 

🔎 EXPLORE
List your assumptions & discoveries:
 

Insightful & revealing test cases:
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
Time: O()
Space: O()
 

📆 PLAN
Outline of algorithm #: 
 

🛠️ IMPLEMENT
is_balanced(s: str) -> bool:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''



def isBalanced(s: str) -> bool:

    first, second = s.replace(" ", "").split("=")

    def helper(input):
        # print(input)

        molecules = input.split("+")

        parsed = {}
        
        for molecule in molecules:

            prefix = 1

            if not molecule[0].isalpha():

                # Find end index of prefix
                idx = 0
                while not molecule[idx].isalpha():
                    idx += 1

                prefix = int(molecule[0:idx])

                # Remove prefix from molecule
                molecule = molecule[idx:]

            elements = [] # (atom, suffix)
            
            for c in molecule:

                if c.islower():
                    # Long atom name
                    elements[-1] = (elements[-1][0] + c, 1)
                elif not c.isalpha():
                    # Suffix
                    elements[-1] = (elements[-1][0], int(c))
                else:
                    # New atom
                    elements.append((c, 1))

            for element in elements:
                parsed[element[0]] = prefix * element[1]

        # for item in parsed.items():
        #     print(item)

        return parsed

    fk = helper(first)
    sk = helper(second)

    return fk == sk

print(isBalanced(s = "2H2 + O2 = 2H2O")) # True
print(isBalanced(s = "1000H2O = Au + Ag")) # False