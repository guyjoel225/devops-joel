import json
import os

repertoire = "/home/joel/Bureau"

file_name = "data"


def load_task():

        if os.path.exists(file_name):

            with open(file_name,"r") as file:

                return json.load(file)


        return []

def save_task(tasks):


        with open(file_name, "w") as file:

            json.dump(tasks, file)


x = 0

while x < 2:

    tasks = load_task()

    titre = input("Entrez un titre: ")

    descr = input("Entrez la desc: ")

    echeance = input("Echeance: ")

    task = {
        "id_task": len(tasks)+1,
        "Titre":titre,
        "Des":descr,
        "echeance":echeance
    }

    tasks.append(task)

    save_task(tasks)

    donnee = load_task()

    print(donnee)
    x += 1