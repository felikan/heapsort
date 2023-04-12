import os

def heapify(heap, length, parentPos):
    while True:
        #Position des linken und1 3 rechten Kindknoten bestimmen+
        parentPos = int(parentPos)
        leftChildPos = parentPos * 2 + 1
        rightChildPos = parentPos * 2 + 2

        #Elternknoten wird vorläufig als größter Wert festgelegt
        largestPos = parentPos

        #Wenn der linke Kindknoten innerhalb des heaps ist
        #UND größer als der Elternknoten ist, wird er zum neuen größten Wert
        if leftChildPos < length and heap[leftChildPos] > heap[largestPos]:
            largestPos = leftChildPos

        #Selbiges wird für rechten Kindknoten geprüft
        if rightChildPos < length and heap[rightChildPos] > heap[largestPos]:
            largestPos = rightChildPos

        #Wenn der größte Wert immer noch dem Elternknoten entspricht, wird die Funktion beendet
        if largestPos == parentPos:
            break

        #Falls nicht, werden Positionen des größten Wertes und des Elternknotens getauscht
        (heap[parentPos], heap[largestPos]) = (heap[largestPos], heap[parentPos])

        #größter Wert wird neuer Elternknoten, Funktion wird wiederholt
        parentPos = largestPos


#ruft für jeden Elternknoten heapify() auf
def buildheap(arr):
    #letzten Elternknoten finden
    lastParentNode = len(arr) / 2 - 1

    #beginned beim letzten Elternknoten heapify() aufrufen
    i = lastParentNode
    while i >= 0:
        heapify(arr, len(arr), i)
        i -= 1
    return arr

#durchsuchen eines Max Heaps nach Schlüssel
def search(key, heap):
    #rekursive Hilfsfunktion
    def search_helper(arr, key, index):
        print(f"\nUntersuche Index {index} nach Schlüssel {key}")
        input("Drücken Sie Enter um fortzufahren...")
        #index muss im array liegen - Wenn der zu suchende Schlüssel größer als der Wurzelknoten ist, liegt Schlüssel nicht im Heap
        if index >= len(arr) or arr[index] < key:
            print(f"\nSchlüssel {key} nicht gefunden im Teilbaum mit Wurzel an Index {index}")
            input("Drücken Sie Enter um fortzufahren...")
            return -1

        #überpuft ob der Schlüssel gleich dem derzeitigen Knoten ist
        if arr[index] == key:
            return index

        #aufruf der Hilfsfunktion auf linken und rechten Kindknoten
        #Wenn Schlüssel im linken oder rechten Teilbaum liegt, soll der index zurückgegeben werden
        left_child = search_helper(arr, key, index * 2 + 1)
        if left_child != -1:
            return left_child

        right_child = search_helper(arr, key, index * 2 + 2)
        if right_child != -1:
            return right_child

        #Wenn der Schlüssel weder im rechten, noch im linken Teilbaum gefunden wird, liegt er nicht im Heap
        return -1

    # Hilfsfunktion beginnend an Wurzelknoten aufrufen
    return search_helper(heap, key, 0)

def sort(arr):
    #heap aufbauen
    buildheap(arr)

    #iteriert rückwärts vom letzten zum zweiten Element des arrays
    switchPos = len(arr) - 1
    while switchPos > 0:
        #erstes Element mit Element an switchPos tauschen
        (arr[0], arr[switchPos]) = (arr[switchPos], arr[0])

        #heapify auf Sub-Array bis switchPos aufrufen
        heapify(arr, switchPos, 0)
        switchPos -= 1
    print("\nDie sortierte Zahlenfolge:")
    print(arr)

#Funktion zum leeren der Kommandozeile
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


cls()
#input nehmen und in array von Zahlen umwandeln
print("Bitte geben Sie die zu sortierende Zahlenfolge per Leertaste getrennt ein. (z.B. 1 3 45 2)")
Folge = input().split(" ")
Folge = [int(numeric_string) for numeric_string in Folge]
cls()

#input nehmen, ob gesucht oder sortiert werden soll
print("Möchten Sie in der gegebenen Zahlenfolge nach einem Schlüssel suchen, oder soll sie sortiert werden? (1 oder 2 eingeben)")
print("1 - Suche nach Schlüssel")
print("2 - Sortieren der Zahlenfolge")
choice = input()

if choice == "1":
    cls()
    heap = buildheap(Folge)
    print("Die eingegebene Zahlenfolge ist: " + str(Folge))
    print("Umgewandelt in einen Max Heap ist die Folge: " + str(heap))
    print("\nNach welchem Schlüssel wollen sie suchen?")
    key = int(input())
    index = search(key, heap)
    if index == -1:
        print("\nSchlüssel liegt nicht im Heap")
    else:
        print(f"\nSchlüssel an {index + 1}. Stelle (Index {index}) im Heap gefunden.")

elif choice == "2":
    cls()
    print("Die eingegebene Zahlenfolge ist: " + str(Folge))
    sort(Folge)
