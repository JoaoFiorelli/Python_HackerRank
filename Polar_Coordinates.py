# Task
# You are given a complex z. Your task is to convert it to polar coordinates.

# Input Format
# A single line containing the complex number z. Note: complex() function can be used in python to convert the input as a complex number.

# Constraints
# Given number is a valid complex number

# Output Format
# Output two lines:
# The first line should contain the value of r.
# The second line should contain the value of phi.

# Sample Input
#  1+2j

# Sample Output
# 2.23606797749979 
# 1.1071487177940904

# Note: The output should be correct up to 3 decimal places.


import cmath

z = complex(input("Digite um número complexo: ")) #Em python j é o símbolo da parte imaginária e não i.
r = cmath.sqrt((z.real**2) + (z.imag**2))
phi = cmath.phase(z)
print(r.real)
print(phi)
