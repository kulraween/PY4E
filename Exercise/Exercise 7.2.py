# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
total_conf = 0
conf = []
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        conf.append(line[line.find("0"):])
        total_conf += float(line[line.find("0"):])
        
avg_conf = total_conf / len(conf)
print("Average spam confidence:", str(avg_conf))
