def estacionamento_ok(K, instantes):
    s = []
    resultado = "nao"
    for i in range(0, len(instantes)):
        if instantes[i] > 0:
            s.append(instantes[i])
            if (len(s)) > K:
                return "nao"

        if instantes[i] < 0 and (instantes[i] * -1) == s[-1]:
            s.pop()

        if len(s) == 0:
            return "sim"

    return resultado


print(estacionamento_ok(3,[1,2,-2,3,-3,-1]))