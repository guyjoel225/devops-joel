def nom_age(**kwagrs):
        print("nom--------------------------------age".upper().center(20))
        print()
        for key in kwagrs:
                
                #print(kwagrs)
                
                print("{0}    --------------------------------  {1}".format(key,kwagrs.get(key)))

                
info_perso = {"Ange":14, "mike":23, "Gerard":29,"Malik":14,"Dane":20, "Donalde":21,"Anne":17, "Grace":19,"Chrys":22,"Anick":16}


nom_age(**info_perso)



