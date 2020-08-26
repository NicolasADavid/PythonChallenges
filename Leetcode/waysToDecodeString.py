class Solution:
    def countDecodes(self, input) -> int:
        if not input:
            return 1

        newWays = 0

        if(self.canTakeOne(input)):
            newWays += self.countDecodes(input[1:])
        if(self.canTakeTwo(input)):
            newWays += self.countDecodes(input[2:])
        
        return newWays

    def canTakeOne(self, input) -> bool:
        if not input:
            return 0

        if input[0] not in [0]:
            return True

    def canTakeTwo(self, input) -> bool:
        if not input:
            return False

        if len(input) < 2:
            return False

        if input[0] == '1':
            return True

        if input[0] == '2':
            if input[1] not in [7, 8, 9]:
                return True
        
        return False
                
if __name__ == "__main__":
    s = Solution()

    # print(s.countDecodes("1")) #1
    # print(s.countDecodes("26")) #2
    # print(s.countDecodes("11")) #2
    print(s.countDecodes("111")) #3
    # print(s.countDecodes("112")) #3