#dans cette partie nosu verrons comment creer les fonction et les procedure


def add(*args:int) -> int:

    print(type(args))
    

def sous(*args:int) -> int:

    print(type(args))
    


def mul(*args):
    print(type(args))

def div(*args):
    print(type(args))

def mod(*args):
    print(type(args))




print("calcullatrice".upper().center(150))


nbre = input("entrez les nombres entiers naturels les separer pas des espace: ".capitalize())
print(nbre)
nbre = nbre.split( )

print(nbre)
add()

sous()

mul()

div()

mod()