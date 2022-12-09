f = open("chorna_rada.txt","r", encoding="utf-8")
n = input("Введіть слово: ")
sep = ''
k = f.readlines()
for z in k:
    q = z.split()
    if n in q or n+"." in q or n +"," in q:
        print(z)
