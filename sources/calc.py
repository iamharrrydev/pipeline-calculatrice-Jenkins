"""
La librairie calc permet de faire les opérations basiques de calcul entre deux entiers.
"""

def add(arg1,arg2):
    try:
        return int(arg1)+int(arg2)
    except ValueError: 
        print("One of the arguments is not an integer.") 

def sous(arg1,arg2):
    try:
        return int(arg1)-int(arg2)
    except ValueError: 
        print("One of the arguments is not an integer.") 


def mult(arg1,arg2):
    try:
        return int(arg1)*int(arg2)
    except ValueError: 
        print("One of the arguments is not an integer.") 

def div(arg1,arg2):
    try:
        return int(arg1)/int(arg2)
    except ValueError: 
        print("One of the arguments is not an integer.") 
    except ZeroDivisionError:
        print("Vous divisez par 0.")

def ope(operateur,arg1,arg2):   
    if operateur=='+':
        return add(arg1,arg2)        
    elif operateur=="-":
        return sous(arg1,arg2)
    elif operateur=="x":
        return mult(arg1,arg2)
    elif operateur=="/":
        return div(arg1,arg2)
    else:
        print("The operator {} n'est pas reconnu.".format(operateur))