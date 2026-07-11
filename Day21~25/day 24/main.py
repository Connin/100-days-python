import os

print(os.getcwd())

with open("../../sample.txt") as file:
    contents = file.read()
    print(repr(contents))