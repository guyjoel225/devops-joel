
print("bonjour tout le mon de ")


ages = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]


auto = [x for x in ages if x >= 15]

print(auto)

age = int(input("entrez votre age"))

if age >= 15:

    auto.append(age)

print(auto) 
