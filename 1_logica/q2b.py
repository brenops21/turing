from queue import Queue

# A função abaixo foi utilizada para inverter a fila do estacionamento, pois considerei a saida "para cima", enquanto
# o enunciado do problema pede para "baixo"
def reversequeue(queue):
    Stack = []
    while (not queue.empty()):
        Stack.append(queue.queue[0])
        queue.get()
    while (len(Stack) != 0):
        queue.put(Stack[-1])
        Stack.pop()


def estado_atual(K, horarios, T):
    q = Queue()
    carros = {}
    str_final = []

    for i in range(len(horarios)): # Cria um dict
        carros[horarios[i]] = i + 1  # instante : carro

    for n in range(K):
        q.put(0)

    for x in range(T + 1): # A seguinte rotina checa se há carros entrando no instante x, caso haja adiciona-os
        if x in horarios:
            q.put(carros.get(x))
            q.get()
        else:
            q.put(0)
            q.get()

    reversequeue(q)
    for j in q.queue:
        str_final.append(j)

    print(str_final)


estado_atual(5, [3, 6, 12, 9, 4, 15, 16], 7)
