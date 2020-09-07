def read4(buf4):
    return 4

class Solution:

    def read(self, buf, n):

        count = 0

        buf4 = [0] * 4

        helpIdx = 0

        while(True):

            numChars = read4(buf4)
            if(numChars):

                appended = 0
                for i in range(numChars):
                    if(helpIdx < n):
                        buf.insert(helpIdx, buf4[i])
                        helpIdx += 1
                        appended += 1
                    else:
                        break

                count += appended                    
            else:
                break

        return count

