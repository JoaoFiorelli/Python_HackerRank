# Task
# You are given a square matrix A with dimensions N X N. Your task is to find the determinant. 
# Note: Round the answer to 2 places after the decimal.

# Input Format
# The first line contains the integer N.
# The next N lines contains the N space separated elements of array A.

# Output Format
# Print the determinant of A.

# Sample Input
# 2
# 1.1 1.1
# 1.1 1.1

# Sample Output
# 0.0


import numpy

n = int(input())
line = []
matrix = []

for _ in range(n):
        line = input().split()
        line = [float(i) for i in line]
        matrix.append(line)

numpy.set_printoptions(legacy='1.13')
print(numpy.linalg.det(matrix))
