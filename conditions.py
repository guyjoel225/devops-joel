print("nous allons travailler les conditions")


"""
ce projet va consister à travailler sur les conditions 
---------if
---------elif
---------else
travaillons sur un mini projet de gestion de gestion dd'achart dans un magasin
"""


code = ""

prix_unit =  0

tax = 18

quantite = 0
prix_htc = 0

prix_tc = 0


fruits = {"mg":200, "py":150, "md":300,"goyv":250, "poire":500, "org":100, "pstq":350,"rais":175,"kw":600,"citron":75}



def calcule(code_fruit):

        global fruits, prix_unit, prix_htc , quantite


        for key in fruits:
             
             if key == code_fruit:
                  
                  prix_unit = fruits.get(key)
                  
                  prix_unit = int(prix_unit)

                  quantite = int(input("Entrez la quantite: "))

                  prix_htc += prix_unit * quantite
              
             else:
                  print(" ce fruit n'est pas disponible dans le stocke")
        print(prix_htc)


                  

code_ffruit = input("entrez le code du fruit svp: ")


calcule(code_ffruit)