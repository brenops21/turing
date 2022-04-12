# A função abaixo inverte cada metade de cada item da entrada
def inversion(string):
    str_reversa = []
    mid = int(len(string)/2)
    i = len(string)
    j = mid

    while j > 0:
        str_reversa += string[j-1]
        j = j-1

    while i > mid:
        str_reversa += string[i-1]
        i = i-1
    return "".join(str_reversa)



def corrige_emails(emails):
    dominio = "@usp.br"
    lista = []

    for k in range(len(emails)):
        str_correct = inversion(emails[k])
        if dominio not in str_correct:
            str_correct = "ERRO"
        lista.append(str_correct)

    print(lista, end=" ")





corrige_emails(["ibol.alimacrb.psu@ocna", "t.alalalimacrb.repsu@ppo", ".orbmem_ovonrb.psu@gnirut"])