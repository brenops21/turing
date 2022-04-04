def estacionamento_ok(K, instantes):
    s = []
    resultado = "nao"
    for i in range(0, len(instantes)):
        if instantes[i] > 0: # Se a entrada for > 0 adiciona-a ao estacionamento
            s.append(instantes[i])
            if (len(s)) > K: # Checa se o estacionamento lotou
                return "nao"

        if instantes[i] < 0 and (instantes[i] * -1) == s[-1]: # Caso a entrada seja negativa e válida, remove o carro
            s.pop()

        if len(s) == 0:
            return "sim"

    return resultado


print(estacionamento_ok(3,[1,2,-2,3,-3,-1]))