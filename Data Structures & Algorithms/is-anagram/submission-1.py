class Solution:
        def isAnagram(self, s: str, t: str) -> bool:
                test = {}
                test1 = {}
                for i in s:
                    if i not in test:
                        test[i] = 1
                    else:
                        test[i] += 1

                for i in t:
                    if i not in test1:
                        test1[i] =1 
                    else:
                        test1[i] +=1
                return test == test1
        