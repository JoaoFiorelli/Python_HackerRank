# Task
# Without using any string methods, try to print the following:
# 123...n
# Note that "..." represents the consecutive values in between.

# Example
# n = 5
# Print the string 12345.

# Input Format
# The first line contains an integer n.

# Output Format
# Print the list of integers from 1 through n as a string, without spaces.

# Sample Input 0
# 3

# Sample Output 0
# 123


N = int(input("Digite um número: "))
print(''.join([str(i) for i in range(1, N+1)]))
