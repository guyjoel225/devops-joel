print("nous allons travailler les conditions")

ajouter = True

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

prix_htc = 0

prix_tc = 0

fruits_noms = {"mg":"mangue", "py":"papaye", "mgu":"mandarine","goyv":"goyave", "pre":"poire", "org":"orange", "pstq":"pasteque","rais":"raisin","kw":"kiwi","ctrn":"citron"}


fruits_prix = {"mg":200, "py":150, "mgu":300,"goyv":250, "poire":500, "org":100, "pstq":350,"rais":175,"kw":600,"citron":75}



def calcule(code_fruit):

        global fruits, prix_unit,quantite
        prix_htc = 0


        for key in fruits_prix:
             
             if key == code_fruit:
                  
                  prix_unit = fruits_prix.get(key)
                  
                  prix_unit = int(prix_unit)

                  quantite = int(input("Entrez la quantite: "))

                  prix_htc += prix_unit * quantite
                  return prix_htc, quantite
              
             else:
                  continue

                  

print("bonjour bienvenue dans le programme")

quatie_prix = {}

nom_quat = {}

while ajouter:
      
      code_fruit = input("Entrez le code du produit svp: ")
      
      pix_total , qutes = calcule(code_fruit)

      quatie_prix[code_fruit] = pix_total

      

      
      for key in fruits_prix:
           
           if key == code_fruit:
                 
                 for keys in fruits_noms:
                       
                       if key == keys:
                             
                             nom_quat[fruits_noms.get(keys)] = qutes
      


          
            
      
      quiter = input("voulez-vous quitter le programme o/n: ").lower()

      if quiter == "o" or quiter == "oui":
            
            print("vous quittez le programme!")

            ajouter = False
      else:
            ajouter  = True


# cette parti du programme va permetre d'afficher
print("liste des produits achetes".upper().center(150))
print()
print('CODE  PRODUIT                       NOMS                 QUANTITE                                         PRIX '.center(1))
print()
for cle in quatie_prix:
      
      for cles in nom_quat:
            
            
            print(f"\t{cle}---------------------------{cles}----------{nom_quat.get(cles)}---------------------------{quatie_prix.get(cle)}")
