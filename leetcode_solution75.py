class Solution:
    def mergeAlternately(self, word1, word2):
     self.word1 = word1
     self.word2 = word2
     i, j = 0, 0
     a = [] 
     while i < len(word1) and j < len(word2):
        a.append(word1[i])
        a.append(word2[j])
        i += 1
        j += 1    
     a.extend(word1[i:])
     a.extend(word2[j:])      
     return "".join(a)
    
if __name__ == '__main__':
    solution = Solution()
    print(solution.mergeAlternately("abc","pqr"))
