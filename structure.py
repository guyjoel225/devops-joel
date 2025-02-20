liste = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q"]

liste2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

liste3 = [21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]

inv = liste.reverse()

desc = [x for x in liste]

#print(desc)

liste.sort()

asc = [x for x in liste]

#print(asc)

#compréhension de liste

couple = [(x,y) for x in desc for y in asc if x != y] # on forme des couples d'éléments distincts

#print(couple)

print()
coupleB = [(x,y) for x in desc for y in asc if x == y] # couple d'éléments égaux


nmbre_pair = [(x,y) for x in liste2 for y in liste3 if x % 2 == y % 2 == 0] # on forme des couple d'élement paire

#print(nmbre_pair)

nmbre_impair = [(x,y) for x in liste2 for y in liste3 if x % 2 == y % 2 != 0] # on forme des couple d'élement impaire

#print(nmbre_impair)

#print(coupleB)


#liste imbriquée, qui permettent de créer des matrix

matrix = [
    [1,5,10,15],
    [2,4,6,8],
    [3,6,9,12]
]   # nous avons une matrix de 3 lignes et de 4 colonnes


#print(matrix) #une  facon d'afficher les éléments de la liste imbiquée



#for i in matrix:
#    print(i, end='') # une autre encore

"""

for x in matrix:

    for y in x:

        print(y, end=' ')
    print("\n") # une autre facon 

print("ceci est la transposé de la matrix")
max_T = [[ligne[i] for ligne in matrix] for i in range(len(matrix)+ 1)]


for x in max_T:

    for y in x:
         print(y, end=" ")
    
    print()


max_T2 =  list(zip(*matrix))



for x in max_T2:

    for y  in x:

        print(y, end=" ")
    
    print()
    """

# les tuples

index = 1,2,3,4,5,6,7,5



listes = [1,2,3,4,5,6,7,8,9,10]

tuples = tuple(listes)
print(tuples)
ensble1 = set(['marc','john','kouassi',"mike","dane","ulrich","dani"])

print(ensble1)

ensble2 = {"joel","guy","marcus","casimi","carime","john","marc","dane","kouassi","paul"}


print(ensble2)


dif_ensble = ensble1 - ensble2
print(dif_ensble)

avoir_ou_ne_pas = ensble2 | ensble1

ensbles1 = ensble1 & ensble2
enbles2 = ensble1 ^ ensble2
print(ensbles1)
print(enbles2)
print(type(avoir_ou_ne_pas))
print(avoir_ou_ne_pas)