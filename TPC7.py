import numpy as np
import matplotlib.pyplot as plt

def load_polinomios(file):
    polinomios = list()
    with open(file, "r") as file:
        for i in file:
            polinomios.extend(i.split("|"))

    return polinomios

def divide_polinomios(polinomio):

    splited = polinomio.split(" ")
    for j in range(len(splited)):
        if splited[j] == "-" or splited[j] == "+":
            splited[j + 1] = splited[j] + splited[j + 1]

    for k in splited:
        if k == "+" or k == "-":
            splited.pop(splited.index(k))
    
    dividedpol = dict()

    for i in splited:
        if "^" in i:
            dividedpol[i.split("^")[0]] = i.split("^")[1]
        else:
            if "x" in i:
                dividedpol[i] = 1
            else: dividedpol[i] = 0

    return dividedpol

def calcula_polinomio(polinomio,x):
    dividedpol = divide_polinomios(polinomio)
    soma = 0 
    for i in dividedpol[i].keys():
        if dividedpol[i] != 0:
            if i[:i.index("x")] == "":
                soma += (1*x)**int(dividedpol[i])
            else:
                soma += (float(i[:i.index("x")])) * (x)** int(dividedpol[i])
        else: 
            soma += float(i)

        return soma
    
def soma_polinomio(polinomio,polinomio1):
    dividedpol = divide_polinomios(polinomio)
    dividedpol1 = divide_polinomios(polinomio1)
    newpol = dict()

    for i in dividedpol.keys():
        for j in dividedpol1.keys():
            if(dividedpol[i] == dividedpol1[j]):
                if (dividedpol != 0 and dividedpol1[j] != 0): 
                    if i[:i.index("x")] == "" and j[:j.index("x")] == "":
                        newpol["2"] = str(dividedpol[i])
                    elif i[:i.index("x")] == "" and j[:j.index("x")] != "":
                        newpol[str(1 + float(j[:j.index("x")]))] = str(dividedpol[i])
                    elif j[:j.index("x")] == "" and i[:i.index("x")] != "":
                        newpol[str(1 + float(i[:i.index("x")]))] = str(dividedpol[i])
                    else:
                        newpol[str(float(i[:i.index("x")])) + float(j[:j.index("x")])] = str(dividedpol[i])
            else:
                newpol[str(float(i) + float(j))] = 0 

    pol = ""

    for i in newpol.keys():
        if float(i) > 0:
            pol += "+ " + str(i) + "x^" + str(newpol[i]) + " "
        else:
            pol  += str(i) + "x^" + str(newpol[i]) + " "

    if pol[0] == "+":
        return pol[2:-4]
    else:
        return pol[:-4]
    
def derivada_polinomio(polinomio):
    dividepol = divide_polinomios(polinomio)
    derivada = ""
    for i in dividepol.keys():
        if dividepol[i] != 0:
            if i[:i.index("x")] == "":
                derivada += dividepol[i] + "x^" + str(int(dividepol[i]) - 1) + " "
            else: 
                derivada += str((float(i[:i.index("x")]) * float(dividepol[i]))) + "x^" + str(int(dividepol[i]) - 1) + " "

    print(derivada)

def grafico_polinomial(polinomio):
    dividedpol = divide_polinomios(polinomio)
    coefs = list()
    max = 0 
    policoefs = list()
    xs = np.linspace(0,9,10)
    for i in dividedpol.values():
        policoefs.append(int(i))

    for i in dividedpol.values():
        if int(i) > max:
            max = int(i)

    for i in range(max + 1):
        if i in policoefs:
            for j in dividedpol.keys():
                if int(dividedpol[j]) == i:
                    if dividedpol[j] == 0:
                        coefs.append(float(j))
                    elif j[:j.index("x")] == "":
                        coefs.append(float(1))
                    else: 
                        coefs.append(float(j[:j.index("x")]))
    else:
        coefs.append(0)

    order = len(coefs)

    ys = np.zeros(len(xs))

    for i in range(order):
        ys += coefs[i] * xs ** i

    plt.plot(xs,ys)
    plt.axhline(y = 0, color = "b")
    plt.axvline(x = 0, color = "b")
    plt.show()


def encontra_grau(polinomio):
    dividedpol = divide_polinomios(polinomio)
    max = 0
    for i in dividedpol.values():
        if int(i) > max:
            max = int(i)

    return max

def main():
    polinomios = load_polinomios("C:/utilizadores/DELL/Ambiente de trabalho")
    print ("Polinomios", end = " " * 20)
    print ("Grau")
    for i in polinomios:
        print (i, end = " " * (33 - len(i)))
        print (encontra_grau(i))


        
main()