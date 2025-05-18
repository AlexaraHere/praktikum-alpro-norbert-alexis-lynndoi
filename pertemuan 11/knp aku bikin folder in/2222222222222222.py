katakata = "heksakosioiheksekontaheksafobia"
a = dict()
for i in katakata:
    if i not in a:
        a[i] = 1
    else:
        a[i] = a[i] + 1

print(a)