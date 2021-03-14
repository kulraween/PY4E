name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

hour_count = dict()

for line in handle:
    line = line.rstrip()
    if line.startswith("From "):
        word = line.split()
        time = word[5]
        timesplit = time.split(":")
        hour = timesplit[0]
        hour_count.setdefault(hour, 0)
        hour_count[hour] += 1
    else:
        continue

hour_list = list(hour_count.items())
hour_list.sort()

for hour, count in hour_list:
    print(hour, count)        
