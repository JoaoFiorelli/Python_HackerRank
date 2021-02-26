# Task
# Read a given string, change the character at a given index and then print the modified string.

# Input Format
# The first line contains a string, S.
# The next line contains an integer i, denoting the index location and a character c separated by a space.

# Output Format
# Using any of the methods explained above, replace the character at index i with character c.


def mutate_string(word, position, character):
    lista = list(word)
    lista[position] = character
    word = "".join(lista)
    return word


word = input("Digite uma palavra: ")
position = int(input("Digite a posição em que a letra deve ser mudada: "))
character = input("Digite a letra para ser trocada: ")
word_new = mutate_string(word, position, character)
print(word_new)
