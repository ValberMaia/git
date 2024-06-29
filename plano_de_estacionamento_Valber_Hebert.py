#Dupla: Valber Maia de Alencar, Hebert Lavoisier Raulino

def calculo(n, lista):
    lista_qualquer = [] #vai armazenar os 'V_i' das pessoas q estacionaram
    vagas = n #impedir que tenha mais pessoas estacionadas doque numero de vagas livres
    cont = True
    while (cont == True) and (vagas > 0):
        for i in range(len(lista)):
            v_lista = lista[i] #vai pegar o 'V_i'
            verificar = True

            while v_lista != 0 and verificar == True: #vai verificar se o numero da vaga equivalente ao 'V_i' já está ocupada ou n
                if v_lista not in lista_qualquer: #se não tiver, vai ocupar
                    lista_qualquer.append(v_lista)
                    vagas -= 1
                    verificar = False
                else: #se já estiver ocupado, vai tentar achar uma vaga de numero menor para tentar ocupar
                    v_lista -= 1
            if v_lista == 0: #se acontecer de não achar nenhuma vaga livre dentro do range de 1 até V_i, o serviço de estacionamento vai parar de funcionar
                break
        cont = False
    return len(lista_qualquer) #O tamanho da lista é a quantidade máxima de gente que vai consegui estácionar

print("Dupla: Valber Maia de Alencar, Hebert Lavoisier Raulino")

n = int(input("Numero de vagas: "))
m = int(input("Numero esperado de clientes: "))
v_i = []
for i in range(m): #faz que a quantidade de 'V_i' seja a mesma que a de numero esperado de clientes
    v_i.append(int(input("v_i: ")))

print(calculo(n, v_i))