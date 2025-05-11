handle = open('apaya.txt')
for i in handle:
    if i.startswith("keren:"):
        print(i)
