# 20250613
class Solution:
    def gameOfLife(self, b: List[List[int]]) -> None:
        n = len(b)
        m = len(b[0])
        a = []
        for i in range(n):
            for j in range(m):
                bval = 0
                if i-1 >= 0:
                    bval += b[i-1][j]
                    if j-1 >= 0:
                        bval += b[i-1][j-1]
                    if j+1 < m:
                        bval += b[i-1][j+1]
                if j-1 >= 0:
                    bval += b[i][j-1]
                if j+1 < m:
                    bval += b[i][j+1]
                if i+1 < n and j-1 >=0:
                    bval += b[i+1][j-1]
                if i+1 < n:
                    bval += b[i+1][j]
                    if j+1 < m:
                        bval += b[i+1][j+1]


                if b[i][j] == 1:
                    if bval < 2:
                        a.append(0)
                    elif bval > 3:
                        a.append(0)
                    else:
                        a.append(1)
                else:
                    if bval == 3:
                        a.append(1)
                    else:
                        a.append(0)
                print(bval)
        count = 0
        for i in range(n):
            for j in range(m):
                b[i][j] = a[count]
                count += 1
