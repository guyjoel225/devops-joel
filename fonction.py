# dans cette parti, nous verrons les fonctions , les *args, les exceptions et les **kwargs 

# creons nos fonctions add, sous , mul, div, mod, div_ent
sum = 0
def add(*args: int) -> int:     # cette fonction permettra de faire les additions des nombres entier, l'utilisateur entre un nombre indefinie de valeurs
        global sum

        if len(args) == 0:

                sum = None
                
        args = list(args) # ici nous convertissons le tuple en liste

        for i in args:  # on fait ici, pour i (chaque elmnt) se trouvant dans la liste d'élement 

            try: # permet de verifier le type et la valeur d'élement contenu dans i

                    i = int(i) # ici, nous effectuons une conversion des élements en entier

            except ValueError:

                continue # si la valeur de i est differente d'un entier les actions suivante ne seron pas executées.
                
            sum += i
        return sum



def sous(*args: int) -> int:
        
        global sum
        diff = int()
        if len(args)== 0:

                diff = None
        x = 0
        args = list(args)

        for i in args:

            try:

                    i =  int(i)

            except ValueError:

                    continue
            
            

            sum = i
             
            if args.index(i) == 0:
                
                diff = sum - x 

            else:
                        diff = x - sum
            x = diff 

        return diff



def mul(*args):

        produit = int()

        if len(args) == 0:

                produit = None

        for i in args:

                try:
                        i = int(i)

                except ValueError:

                        continue

                produit *= i
        return produit





def div(*args: int) -> int:

        div = int()

        if len(args) == 0:

                div = None
        for i in args:

                try:
                        i = int(i)

                except ValueError:
                        continue
                
                if args.index(i) == 0:

                        div = i

                else:
                        try:
                                div = div / i
                        except ZeroDivisionError:
                                print("Division par zéro impossible!!")
                                print(f"nous n'avons pas pu diviser par {i}")
                                div = None
                                break

        return div



def div_ent(*args: int) -> int:

        div_ent = int()

        if len(args) == 0:

                dev_ent = None
        for i in args:
                dev_ent = int()
                try:
                        i =  int(i)

                except ValueError:
                        continue

                if args.index(i) == 0:

                        div_ent = i
                else:
                        try:
                                div_ent = div_ent // i

                        except ZeroDivisionError:
                                
                                print(f"Impossible d'effectuer une division par {i}")
                                
                                div_ent = None

                                break

        return div_ent



def mod(*args: int) -> int:

        reste = int()
        if len(args) == 0:

                reste = None
        
        for i in args:

                try:
                        i = int(i)

                except ValueError:
                        continue

                if args.index(i) == 0:

                        reste = i
                else:
                        try:

                                reste = reste % i

                        except ZeroDivisionError:

                                print(f"Impossible de diviser par {i}")

                                reste = None

                                break
        return reste

                