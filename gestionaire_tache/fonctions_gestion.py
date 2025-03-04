import os
import json

directory = "/home/joel/Bureau/.data_app"


file_name = "taks_data"

"""
 
Fonctionnalités à implémenter :
1. Ajouter une tâche: Nom, description, échéance, statut (à faire/en cours/terminée).  
2. Afficher les tâches : Filtrer par statut, trier par échéance.  
3. Mettre à jour une tâche: Modifier la description, le statut, l’échéance.  
4. Supprimer une tâche.  
5. Sauvegarde et chargement : Stockage des tâches dans un fichier .  

Technos & Concepts appliqués : 
✔️ Listes & Dictionnaires pour stocker les tâches.  
✔️ Fichiers pour sauvegarder et recharger les données.  
✔️ Manipulation des entrées utilisateur pour une interface en ligne de commande simple.  
✔️ Utilisation des fonctions Python pour organiser le code proprement.  

Tu veux un exemple de code de départ pour ce projet ? 🚀

"""
def task_load():

    global file_name, directory

    os.chdir(directory)

    if os.path.exists(file_name):

        with open(file_name, "r") as file:
              
                return json.load(file)


    return []



def task_save(tasks):

        global file_name, directory

        os.chdir(directory)
        
       
        with open(file_name, "w") as file:

                json.dump(tasks, file)
            


def add_task(titre, description, echeance, status):

            tasks = task_load()
            task = {"task_id":len(tasks)+1,
            "Titre":titre,
            "description":description,
            "echeance":echeance,
            "status":status}
            tasks.append(task)
            return tasks


def afficher(valeur):
       
        tasks = task_load()

        sorti = 0

        for task in tasks:
              
              for vlue in task.values():
                     
                     if vlue == valeur:
                            
                            sorti = 1
                            print(f"{task["task_id"]}\t{task["Titre"]}\t{task["description"]}\t{task["echeance"]}\t{task["status"]}")
                     
        if sorti == 0:
               
               print("La valeur recherchée ne correspond à aucun enregistrement!!")






def supprimer(retirer):
       
    tasks = task_load()

    tuples = [task for task in tasks  if task["task_id"] != retirer]

    tasks = list(tuples)

    return tasks

def update_task():
       
       tasks = task_load()

       print("\n")

       id_task = input("ENtrez l'Id de la tache à modifier: ")

       id_task = int(id_task)

       for task in tasks:
              
              for key in task.keys():
                     if task["task_id"] == id_task:
                            
                            taches = task
        
       print("\n")
       
    
       print("Entrez: (Titre/description/echeance/status) pour modifier.")

       print("\n")

       elt = input("Entez l'élément à modifier ici: ")

       for key in taches.keys():
           
           if key == elt:
                
                print(f"Entrez la nouvelle valeur de ({key}) actuellement ({taches[key]})")

                new = input("ici: ")

                taches[key] = new
                
                for task in tasks:
                       
                       for cle in task:
                              
                              if cle == key:
                                     
                                     task = taches
              
       print("\n")
       save = input("Voulez-vous enregisterer cette modification (o/n) avec o pour oui et n pour non: ")
       print("\n")
       if save.lower() == "o":
            
            task_save(tasks)
            print(taches)
            
            print("\n")
            
            print("enregistrement, OK!")
            
       elif save.lower() == "n":              
            
            print("nous quittons sans enregistrer!!")



