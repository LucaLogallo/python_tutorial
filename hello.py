msg = "ciao dio merda"
print(msg)

print(msg.capitalize())


# dir mostra una lunga lista di funzioni che fanno parte dell'oggetto/variabile/funzione sulla quale lo stiamo facendo
dir(5)

print(msg.__len__())  # lunghezza della variabile
# controlla se l'intera stringa è tutta in minuscola e restituisce true se è vero altrimenti false
print(msg.islower())

# replace sostituisce il primo elemento inserito nella funzione  con il secondo valore inserito
msg1 = "abc".replace("a", "cazzo")
print(msg1)


# CLASSI E OGGETTI IN PYTHON #

type("a")
# <class 'str'>
type(1)
# <class 'int'>
type(True)
# <class 'bool'>

# / creare una classe e oggetti in python


class Car:  # dichiarazione diella classe con class Nome_classe :
    # dichiariamo i dati della classe e ogni istanza della classe potrà accedervi tranquillamente
    speed = 0
    started = False

    def start(self):
        self.started = True
        print("La macchina è partita, vedi di camminare")

    def increase_speed(self, delta):
        if self.started:
            self.speed = self.speed + delta
            print("Vrooooooooom!!!!!", self.speed)
        else:
            print("Ndo cazzo vai senza accendere la macchina , Coglione")

    def stop(self):
        if(self.speed > 0):
            a = True  # quando dichiaro variabili nelle istanze della classe le altre istanze non potranno accedervi
            while a:  # fin quando a è true lui fa il calcolo di quando frena
                self.speed = self.speed - 10
                print("frenando", self.speed)
                if self.speed == 0:  # se la velocità diventa uguale a 0 allora setto la variabile a = False
                    a = False  # così il while non entrerà più
        else:
            if(self.speed < 0):
                print("stai andando in retromarcia")

            print("sei fermo. cazzo ti freni")


# abbiamo dichiarato la classe con i propri attributi e i metodi di quella classe che modificano gli attributi della classe
# adesso però dobbiamo creare una variabile del tipo della classe che abbiamo creato


car = Car()
car.increase_speed(10)
# >>Ndo cazzo vai senza accendere la macchina , Coglione
car.start()
# >>La macchina è partita, vedi di camminare
car.increase_speed(100)
# >>Vrooooooooom!!!!! 100
car.stop()
# Vrooooooooom!!!!! 100
# frenando 90
# frenando 80
# frenando 70
# frenando 60
# frenando 50
# frenando 40
# frenando 30
# frenando 20
# frenando 10
# frenando 0


# un oggetto in python è comunque una istanza della classe. Una classe può avere più istanze.
# ovviamente si possono dichiarare più variabili di tipo classe

# Basic data type

# integers // immutable
# floating point numbers // immutable
# complex numbers // immutable
# booleans  // immutable
# Strings // immutable


# tuples  // immutable
# -- le tuple possono contenere più valori in una singola variabile
# -- sono ordinate: l'ordine degli item è preservato
# -- può contenere valori duplicati
# -- è indicizzato quindi posso accedere agli items attraverso l'indice
# -- può essere di lunghezza arbitraria

# my_numbers = (1, 2, 3)
# the_same = 1, 2, 3
# my_string = ("ciao", "polpetta")
# my_mixed_tuple = ("ciao", 123, True)

tuple([0, 1, 2])
# >> (0,1,2)
# se proviamo a fare una tupla con un solo carattere python lo trasformerà nel formato di una tupla ovvero tuple(0) => tuple(0,)

# si possono avere tuple di array
11 = [1, 2, 3]
12 = [4, 5, 6]
t = (*11, *12)
# >> (1, 2, 3, 4, 5, 6)

# si possono avere molteplici assegnazioni
person = ("luca", 23, True)
name, age, registered = person
# name >> luca
# age >> 23
# registered >> true

mixed_tuple = "ciao", 123, True
#mixed_tuple[1] >> 123
#mixed_tuple[0] >> "ciao"
t1 = (1, 2, 3)
t = (*t1, "extra", "items", 4, 5, 6)
#t >> (1, 2, 3, "extra", "items", 4, 5, 6)

# len funziona sulle tuple
# un a volta dichiarata la tupla non può cambiare la lunghezza
# a differenza del set le tuple possono avere duplicati
# può essere un buon metodo per eliminare i duplicati

# >> tupla to list
t = 1, 2, 3
list(t)
# >>[1, 2, 3] tupla in lista

t = 1, 2, 3
l = [*t]
# >>[1, 2, 3]
l = [*t, 4, 5, 6]
# >>[1, 2, 3, 4, 5, 6] altro modo per trasformare la tupla in una lista

# >> tupla to set
t = (1, 2, 3, 3)
s = set(t)
# >>s{1, 2, 3}

s = {*t}
# >>s{1, 2, 3} metodo con unpacking per trasformare la tupla in set

# >> tupla to string
t = (1, 2, 3)
print(t)
# >> (1, 2, 3)
# >> str(t)'(1, 2, 3)'


# lists // è uguale alle tuple solo che è mutable mentre le tuple no
# ranges  // mutables
# dictionaries // mutables
# creare e usare i dizionari in python
phone_numbers = {
    "luca": "000-0000000001",
    "giovanni": "000-000000002"
}

my_empty_dict = {}

phone_numbers["luca"]
# >> 000-000000001

phone_numbers["antonio"] = "000-000000003"
del(phone_numbers["luca"])
# >> phone_numbers {"giovanni":"000-000000002", "antonio":"000-000000003"}

a = {"sub_dict": {"b": True},
     "mylist": [100, 200, 300]
     }
a["sub_dict"]["b"]
# >> True
a["mylist"][2]
# >> 300

# valid dictionary key

crazy_dictionary = {int: 1, float: 2, dict: 3}
crazy_dictionary[dict]
# >> 3

runners = {1000: "luca", 1001: "giovanni", 1002: "antonio"}
runners[1001]
# >> "giovanni"

# nuovi modi per creare il dizionario
dict([('Jack', '070-02222748'),
      ('Pete', '010-2488634'),
      ('Eric', '06-10101010')])
#  {'Jack': '070-02222748', 'Pete': '010-2488634', 'Eric': '06-10101010'}


# sets  // mutables
