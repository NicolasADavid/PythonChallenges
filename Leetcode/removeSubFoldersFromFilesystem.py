from typing import List

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        input = sorted(folder)

        slow = 0

        for fast in range(1, len(folder)):

            last = input[slow]
            curr = input[fast]

            if curr.startswith(last) and not (curr.count("/") == last.count("/")):
                continue
        
            input[slow+1] = input[fast]
            slow += 1

        return input[:slow+1]


if __name__ == "__main__":
    s = Solution()

    # input = list(["/a","/a/b","/c/d","/c/d/e","/c/f"])
    input = list(["/a/b/c","/a/b/ca","/a/b/d"])
    r = s.removeSubfolders(input)
    
    for thing in r:
        print(thing)
