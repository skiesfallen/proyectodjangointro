archivo_mod = open('modismos.txt','r', encoding="UTF-8")

dic = {}
for a in archivo_mod:
    b = a.strip().split(':')
    print(b)
    dic[a[0]] = a[1]
print(dic)

