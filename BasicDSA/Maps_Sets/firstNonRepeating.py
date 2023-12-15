from collections import *

def firstNonRepeatingCharacter(s):
    myDict = OrderedDict()
    for i in range(len(s)):
        value = myDict.get(s[i], 0)
        if value > 0:
            value += 1
            myDict[s[i]] = value
        else:
            myDict[s[i]] = 1
  
    for i in myDict:
        if myDict[i] == 1:
            return i
    return s[0]

if __name__ == "__main__":

    s = "AabBcC"
    ans = firstNonRepeatingCharacter(s)
    print(ans)

