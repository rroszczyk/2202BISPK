import threading

blokada = threading.Lock()

# funkcja z błędną blokadą
#def getDataFromFile(fileName):
#    blokada.acquire()
#
#    with open(fileName, 'r') as f:
#        f.write("Cos")
#
#    blokada.release()

def getDataFromFile(fileName):
    with blokada, open(fileName, 'r') as f:
        f.write("Cos")

try:
    getDataFromFile("jakis.txt")
except FileNotFoundError:
    print("Brakuje pliku")

blokada.acquire()
print("Plik może zostać wykorzystany")