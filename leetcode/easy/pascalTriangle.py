class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        n = numRows
        l = []
        for i in range(1,n+1):

            if i >2:
                ar = [None for _ in range(i)]
                ar[0],ar[-1] = 1,1
                k = 1
                while ar[k]!=1:
                    ar[k] = l[i-2][k] + l[i-2][k-1]
                    k+=1
                l.append(ar)

            elif i==1:
                l.append([i])
                continue
            elif i==2:
                l.append([1,1])
                continue
        return l
