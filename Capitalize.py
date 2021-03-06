# Task
# You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.
# alison heck -> Alison Heck
# Given a full name, your task is to capitalize the name appropriately.

# Input Format
# A single line of input containing the full name, S.

# Output Format
# Print the capitalized string, S.

# Sample Input
# chris alan

# Sample Output
# Chris Alan


def solve(s):
    S_DIV = []
    s_div = s.split(" ")
    for word in s_div:
        S_DIV.append(word.capitalize())
    S = " ".join(S_DIV)
    return S

if __name__ == '__main__':
    s = input()
    print(solve(s))
