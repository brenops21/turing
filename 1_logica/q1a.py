# Remover os prefixos comuns entre os emails

def conta_economia(emails):
    size_email = len(emails[0])
    size_list = len(emails)
    counter = 0

    # A seguinte rotina checa se a letra de posição [j] de um email coincide com com a letra de posição [j] do
    # próximo email
    for i in range(size_list - 1):
        for j in range(size_email):
            if (emails[i][j] == emails[i+1][j]):
                counter += 1
            if (emails[i][j] != emails[i+1][j]):
                break

    print(counter)


conta_economia(["camila.lobianco@usp.br",
                "camilalala.topp@usp.br",
                "azank.pistolado@usp.br"])



