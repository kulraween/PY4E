name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

email = dict()

for line in handle:
    line = line.rstrip()
    if line.startswith("From "):
        word = line.split()
        address = word[1]
        email.setdefault(address, 0)
        email[address] += 1
    else:
        continue
        
maximum = max(dict.values(email))
address_max = max(email, key=email.get)

print(address_max + " " + str(maximum))
