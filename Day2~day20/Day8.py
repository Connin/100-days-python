# def greet(name):
#     print(f"ss {name}")

# greet(123)

# #name = "parameter"
# #123 = {argument}

# def calculate_love_score(name1, name2):
#     name1 = name1.upper()
#     name2 = name2.upper()
#     truescore = (name1.count("T") + name2.count("T") +
#     name1.count("R") +
#     name2.count("R") +
#     name1.count("U") +
#     name2.count("U") +
#     name1.count("E") +
#     name2.count("E"))

#     lovescore = (name1.count("L") + name2.count("L") +
#     name1.count("O") +
#     name2.count("O") +
#     name1.count("V") +
#     name2.count("V") +
#     name1.count("E") +
#     name2.count("E"))
#     print(f"answer is {truescore *10 + lovescore}")
# calculate_love_score("Kanye West", "Kim Kardashian")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def ceaser():
  direction = " "
  while direction != "encode" and direction != "decode":
    direction = input("type decode or encode")
    #print("wrong input")

  msg = input("Type ur message\n")
  msg = msg.lower()
  shift = int(input("Type shift number"))

  listmsg = []
  encodemsg = []
  decodemsg = []
  messaged = ""
  x = 0

  def encode(msg, shift):
    listmsg[:] = list(msg)
    #for char in listmsg:
    for i in range(len(listmsg)):
      if listmsg[i] != ' ':
        if listmsg[i] in letters:
          x = letters.index(listmsg[i])
          encodemsg.append(letters[(x+shift) % len(letters)])
        elif listmsg[i] not in letters:
          encodemsg.append(listmsg[i])
      else:
        encodemsg.append(" ")
    messaged = "".join(encodemsg)
    print(f"{messaged}")
  # encode(msg, shift)

  def decode(msg, shift):
    listmsg[:] = list(msg)
    for i in range(len(listmsg)):
      if listmsg[i] != ' ':
        if listmsg[i] in letters:
          x = letters.index(listmsg[i])
          decodemsg.append(letters[(x-shift) % len(letters)])
        elif listmsg[i] not in letters:
          decodemsg.append(listmsg[i])
      else:
        decodemsg.append(" ")
    messaged = "".join(decodemsg)
    print(f"{messaged}")

  if direction == "encode":
    encode(msg, shift)
  elif direction == "decode":
    decode(msg, shift)

ceaser()

    