import random

def f_YES (a):
    print(f"YES ({a}) = {a}")
    return a

def f_NOT (a):
    if a == 0:
        print(f"NOT ({a}) = 1")
        return 1
    else:
        print(f"NOT ({a}) = 0")
        return 0

def f_AND (a, b):
    if a==1 and b==1:
        print(f"{a} AND {b} = 1")
        return 1
    else:
        print(f"{a} AND {b} = 0")
        return 0

def f_OR (a, b):
    if a==0 and b==0:
        print(f"{a} OR {b} = 0")
        return 0
    else:
        print(f"{a} OR {b} = 1")
        return 1
    
def f_XOR (a, b):
    if a==0 and b==0:
        print(f"{a} XOR {b} = 0")
        return 0
    elif a==1 and b==1:
        print(f"{a} XOR {b} = 0")
        return 0
    else:
        print(f"{a} XOR {b} = 0")
        return 1

def f_NAND (a, b):
    return f_NOT(f_AND(a, b))

def f_NOR (a, b):
    return f_NOT(f_OR(a, b))

def add_1bit (a,b):
    s=f_XOR(a,b)
    c=f_AND(a,b)
    print(f"{a} + {b} = {c}{s}")
    return s,c

def add_capsule (a,b,Cin):
    S=f_XOR(f_XOR(a,b),Cin)
    Cout=f_OR(f_AND(a,b),f_AND(f_XOR(a,b),Cin))
    return S,Cout


def add_n_bits (bitsA,bitsB):
    A=[]
    B=[]
    Cin=0
    C=[]
    for i in range(len(bitsA)-2):
        A.append(int(bitsA[len(bitsA)-(i+1)]))
        B.append(int(bitsB[len(bitsB)-(i+1)]))
    for x in range(len(bitsA)-2):
        c,R=add_capsule(A[x],B[x],Cin)
        Cin=R
        C.insert(0,str(c))
    if R==1:
        C.insert(0,str(R))
    return C

def get_int():
    rep=int(input("entre un nombre compris entre 0 et 255 :"))
    return str(bin(rep)),rep

def prog_add():
    A,a=get_int()
    B,b=get_int()
    result="".join(add_n_bits(A,B))
    print(f"{A} ({a}) + {B} ({b}) = {result} ({a+b})")

prog_add()