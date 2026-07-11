import os
print(os.getcwd())
names = []
new_letter = []
with open("Names/invited_names.txt", ) as file:
    contents = file.readlines()
    for i in contents:
        names.append(i.strip())
    print(names)

with open("Letters/starting_letter.txt") as file:
    letter_content = file.read()
    for i in range(len(names)):
        new_letter = letter_content.replace('[name]', names[i])
        with open(f"Letters/{names[i]}_letter.txt", "w") as f:
            f.write(new_letter)