dataset = list()

with open("C:\Users\DELL\Downloads\diabetes_prediction_dataset.csv","r") as csv:
    csv.readline()
    for line in csv:
        dataset.append(line.split(" , "))


def distribuicao_genero(lista):
    mulher = 0
    homem = 0
    for i in lista:
        if i[3]:
            if i[0] == "mulher":
                mulher = mulher + 1
            else:
                homem = homem + 1
    print (mulher)
    print(homem)
    soma = mulher + homem
    homem = (homem/soma)*100
    mulher = (mulher/soma)*100

    print(f"homem : {homem: .0f}%, mulher: {mulher: .0f}%")


def distribuicao_idades(lista):
    idades = list()
    for i in lista:
        if i[3]:
            idades.append(int(float(i[1])))
    
    range_idades = [[0,10],[11,24]]

    i = 25
    while i <= 80:
        range_idades.append([i, i + 4])
        i = i + 5
    
    distribuicao = dict()
    for j in range (len(range_idades)):
        distribuicao[j] = 0

    for j in idades:
        for l in range_idades:
            if j in range(l[0],l[1] + 1):
                distribuicao[range_idades.index(1)] = distribuicao[range_idades.index(1)] + 1
                break

    print ("Distribuição de idade\n")

    for j,k in zip(range_idades, distribuicao.values()):
        print(f"{j} : {(k/len(idades))*100: .2f}%\n")


def distribuicao_glicose(lista):
    niveis_glicose = list()
    for i in lista:
        niveis_glicose.append(int(i[7]))

    print(max(niveis_glicose))

    distribuicao_glicose = dict()
    i = 0
    while (i <= max(niveis_glicose)):
        distribuicao_glicose[i] = 0
        i = i + 10

    for i in niveis_glicose:
        for j in distribuicao_glicose.keys():
            if i > j:
                continue
            else:
                distribuicao_glicose[j] = distribuicao_glicose[j] + 1
                break

    print(f"Nível sanguíneo de glicose\n")

    for i in distribuicao_glicose.keys():
        print(f"{i} :{(distribuicao_glicose[i]/len(niveis_glicose))*100: .2f}%\n")
        
        