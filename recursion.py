'''
Rekurencja to koncepcja, w której funkcja wywołuje samą siebie w trakcie swojego wykonywania.
Proces ten może powtarzać się wielokrotnie, aż do spełnienia pewnego warunku zakończenia, który zapobiega
 nieskończonej rekurencji. '''
from time import sleep

''' jak zmienna attempts jest zainicjowana wewnątrz funkcji connect_to_internet() i zawsze ustawiana na 0 przy każdym 
wywołaniu funkcji. Z tego powodu wartość attempts zawsze będzie 1, ponieważ zmienna jest tworzona na nowo przy każdym 
wywołaniu funkcji rekurencyjnej.
Aby naprawić ten problem, możesz przenieść zmienną attempts poza funkcję, tak aby zachować jej wartość między różnymi 
wywołaniami funkcj a wewnatrz zadeklarowac ja jako global'''

attempts = 0

def connect_to_internet():
    global attempts

    if attempts <3:
        attempts +=1
        print("Trying to connect: ", attempts)
        sleep(2)
        print("connection failed ... Trying again!")
        sleep(1)
        print('DDD',attempts)
        connect_to_internet()
    else:
        print("...")
        sleep(1)
        print("...")
        sleep(1)
        print("Successfully connected")


connect_to_internet()