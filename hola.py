# %%

a = [18, 20, 21, 21, 19, 22, 24, 17]
sum = int()
for x in a:
    sum = sum + x
    promedio = int(sum/len(a))



b = sorted(a)

moda = int
i = 0
modai = 0
for x in b:
    if x == b[i-1]:
        modai = modai + 1
        moda = x
    else:
        modai = 0

print(moda)
print(b[len(b)//2])
print(promedio)