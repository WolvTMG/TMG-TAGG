import random
import os
import sys
import time


def again():

    ui12 = input("Would you like to play again? Y / N: ").upper()
    if ui12 == 'Y':
        choice()
    elif ui12 == 'N':
        sys.exit()
    else:
        again()


def QIX():

    ui11 = input("Is your animal yellow or orange").upper()

    if ui11 == 'Y':
        print("Is it a tiger?")
    elif ui11 == 'N':
        print("Oops, I don't know")
    else:
        QIX()

def con9():

    con9 = input("Y / N: ").upper()

    if con9 == 'Y':
        print("I got it correct!")
    elif con9 == 'N':
        print("Oops, I don't know")
    else:
        con9()


def QVIII():

    ui10 = input("Is your animal small?").upper()

    if ui10 == 'Y':
        print("Is it a rat?")
        again()
    elif ui10 == 'N':
        QIX()
    else:
        QVIII()

def con8():

    con8 = input("Y / N: ").upper()

    if con8 == 'Y':
        print("I got it correct!")
        again()
    elif con8 == 'N':
        QIX()
    else:
        con8()


def QVII():

    ui9 = input("Does your animal have 2 colorus? Y / N: ").upper()

    if ui9 == 'Y':
        print("I got it correct!")
        again()
    elif ui9 == 'N':
        QVIII()
    else:
        QVII()

def con7():

    con7 = input("Y / N: ").upper()

    if con7 == 'Y':
        print("I got it correct!")
        again()
    elif con7 == 'N':
        QVIII()
    else:
        con7()


def QVI():

    ui8 = input("Does your animal have a lot of pressure on his or her bite Y / N: ").upper()

    if ui8 == 'Y':
        print("Is it a crocodile")
    elif ui8 == 'N':
        QVII()
    else:
        QVI()

def con6():

    con6 = input("Y / N: ").upper()

    if con6 == 'Y':
        print("I got it correct!")
        again()
    elif con6 == 'N':
        QVII()
    else:
        con6()


def QV():

    ui7 = input("Does your animal have nails to scratch things?").upper()

    if ui7 == 'Y':
        print("Is it a cat?")
        con5()
    elif ui7 == 'N':
        print("Oops, sorry I don't know")
    else:
        QV()

def con5():

    con5 = input("Y / N: ").upper()
    if con5 == 'Y':
        print("I got it correct!")
        again()
    elif con5 == 'N':
        print("Oops, sorry I don't know")

def QIV():

    ui6 = input("Does your animal live underwater? Y / N: ").upper()
    if ui6 == 'Y':
        print("Is it a crocodile?")
        con4()
    elif ui6 == 'N':
        QV()
    else:
        QIV()

def con4():

    con4 = input("Y / N: ").upper()

    if con4 == 'Y':
        print("I got it correct!")
        again()
    elif con4 == 'N':
        QV()
    else:
        con4()


def QIII():

    ui5 = input("Does your animal have many breeds? Y / N: ").upper()
    if ui5 == 'Y':
        print("Is it a dog?")
        con3()
    elif ui5 == 'N':
        QIV()
    else:
        QIII()

def con3():

    con3 = input("Y / N: ").upper()

    if con3 == 'Y':
        print("I got it correct!")
        again()
    elif con3 == 'N':
        QIV()
    else:
        con3()


def QII():

    ui4 = input("Does your animal weigh a lot? Y / N: ").upper()
    if ui4 == 'Y':
        print("Is it an elephant?")
        con2()
    elif ui4 == 'N':
        QIII()
    else:
        QII()

def con2():

    con2 = input("Y / N: ").upper()

    if con2 == 'Y':
        print("I got it correct!")
        again()
    elif con2 == 'N':
        QIII()
    else:
        con2()

def QI():

    ui3 = input("Can your animal fly? Y / N: ").upper()

    if ui3 == 'Y':
        print("Is it a bird?")
        con()
    elif ui3 == 'N':
        QII()
    else:
        QI()

def con():

    con = input("Y / N: ").upper()

    if con == 'Y':
        print("I got it correct!")
        again()
    elif con == 'N':
        QII()
    else:
        con()


def choice():

    print("""Choose an animal from this list and remember it:
Dog      Elephant
Cat      Rat
Tiger    Crocodile
Bird     Panada
""")

    time.sleep(5)
    print("Good, now answer these questions accuratly")
    QI()


def game():

    ui = input("Welcome to TAGG, would you like to start? Y / N: ").upper()

    if ui == 'Y':
        print("Very well, let's begin")
        choice()
    elif ui == 'N':
        print("Have a great day!")
        sys.exit()
    else:
        game()

game()
