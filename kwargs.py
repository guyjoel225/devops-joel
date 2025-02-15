def nom_age(**kwagrs):
        print("nom--------------------------------age".upper().center(20))
        print()
        for key in kwagrs:
                
                #print(kwagrs)
                
                print("{0}    --------------------------------  {1}".format(key,kwagrs.get(key)))

                
info_perso = {"Ange":14, "mike":23, "Gerard":29,"Malik":14,"Dane":20, "Donalde":21,"Anne":17, "Grace":19,"Chrys":22,"Anick":16}


nom_age(**info_perso)


#lambda 

add = lambda x, y: x + y

print(add(10,20))

sous  = lambda x, y: x - y

print(sous(12,20))


mul = lambda x, y: x * y

print(mul(10,5))

div = lambda x, y : x / y

print(div(20,6))

div_ent = lambda x,y: x // y

print(div_ent(20,6))


mod = lambda x , y: x % y

print(mod(10, 4))


def adition():
        
        
        return lambda x, y: x + y

def sosutration():
        
        return lambda x, y: x - y


def produit():
        
        return lambda x , y: x * y


def division():
        
        return lambda x, y: x / y


def div_entier():
        
        return lambda x, y: x // y


def modulo():
        
        return lambda x, y: x % y


print(adition()(15,16))

print(sosutration()(20,14))

print(produit()(10,16))

print(division()(100,17))

print(div_entier()(100,17))

print(modulo()(165,10))