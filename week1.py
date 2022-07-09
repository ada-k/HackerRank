# plusMinus

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    pos = [i for i in arr if i > 0]
    neg = [i for i in arr if i < 0]
    zeros = [i for i in arr if i == 0]
    
    print(round(len(pos)/len(arr), 6))
    print(round(len(neg)/len(arr), 6))
    print(round(len(zeros)/len(arr), 6))
    

    

        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)


## minmax sum
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    print(sum(sorted(arr)[:4]), sum(sorted(arr)[1:]))
    # print(sorted(arr)[:4])
    
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

# time conversion
#!/bin/python3

import math
import os
import random
import re
import sys
import datetime
from datetime import timedelta

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    if "AM" in s:
        if s[:2] == "12": 
            string = (datetime.datetime.strptime(s[:-2], '%H:%M:%S') - timedelta(hours=12)).time()
            
        else:
            string = s[:-2]
    
    elif "PM" in s:
        if s[:2] == "12": 
            string = s[:-2]
            
        else:
            string = (datetime.datetime.strptime(s[:-2], '%H:%M:%S') + timedelta(hours=12)).time()
        
    return str(string)

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()


# findMedian
#
# Complete the 'findMedian' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def findMedian(arr):
    # Write your code here
    # sorted = sorted(arr)
    return(sorted(arr)[int(((len(arr)/2) + 0.5) - 1)])


# lonelyInteger
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    for i,j in zip(Counter(a).values(), Counter(a).keys()):
        if i != 2:
            loner = j
    return j

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()


# diagonalDifference
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    n = len(arr[0])
    # diag1 = [arr[i][i] for i in range(n)]
    # diag2 = [arr[n-1-i][i] for i in range(n-1, -1, -1)]
    
    return abs(sum([arr[i][i] for i in range(n)]) - sum([arr[n-1-i][i] for i in range(n-1, -1, -1)]))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()


# countingsort
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    # Write your code here
    n = 100
    res = [0] * n
    for i in arr:
        res[i] += 1
        
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()


# flippingMatrix
#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def flippingMatrix(matrix):
    # Write your code here
    
    # q=no of matrices
    for i in range(q):
#         a = [[0 for j in range(2*n) for x in range(2*n)]]
        
        for w in range(2*n):
            pass
        
        v = 0
        for i in range(n):
            for j in range(n):
                l = []
                l.append(matrix[i][j])
                l.append(matrix[2*n-1-i][j])
                l.append(matrix[i][2*n-1-j])
                l.append(matrix[2*n-1-i][2*n-1-j])
                
                maxv = max(l)

                v += maxv
                
        return v

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + '\n')

    fptr.close()


# zigzag sequence
def findZigZagSequence(a, n):
    a.sort()
    mid = int((n + 1)/2) - 1
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    ed = n - 2
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return

test_cases = int(input())
for cs in range (test_cases):
    n = int(input())
    a = list(map(int, input().split()))
    findZigZagSequence(a, n)


# towerBreakers
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def towerBreakers(n, m):
    # Write your code here
    if m == 1:
        return 2
    else:
        return 1 if n%2 != 0 else 2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = towerBreakers(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()



# caeserCypher
#!/bin/python3

import math
import os
import random
import re
import sys
from string import ascii_letters, digits

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#


def caesarCipher(s, k):
    result = ""
 
    # traverse text
    for i in range(len(s)):
        char = s[i]
        if char in ascii_letters:
            # Encrypt uppercase characters
            if (char.isupper()):
                result += chr((ord(char) + k-65) % 26 + 65)
    
            # Encrypt lowercase characters
            else:
                result += chr((ord(char) + k - 97) % 26 + 97)
        else:
            result += char
        
    return result

                      
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()



# palindrome
def solve(s): 
    p=0

    while p<=len(s)//2:
        q = len(s) - p - 1
        if s[p] != s[~p]:
            if s[p+1:q+1] == s[q:p:-1]:
                return p
            elif s[p:q] == s[p:q][::-1]:
                return q
            else:
                return -1
        p+=1
    return -1


# gridChallenge
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#
def gridChallenge(grid):
    arr=grid
    for i in range(n):
        arr[i]=sorted(arr[i])
    for i in range(len(arr[0])):  #if you use length as n, you will get error.
        for j in range(1,len(arr[0])):
            if(arr[j-1][i]>arr[j][i]):
                return 'NO'
    return 'YES'
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()




