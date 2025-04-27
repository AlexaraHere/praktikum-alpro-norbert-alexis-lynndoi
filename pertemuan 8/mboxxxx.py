import re
handle = open("pertemuan 8\\mbox-short.txt")
count = 0
for line in handle:
    line=line.rstrip()
    if re.search('From:', line):
        count += 1
        print(line)
        print("Count: ",count)

