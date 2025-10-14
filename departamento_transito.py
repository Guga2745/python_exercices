ano_atual = int(input("Digite o ano atual : "))
ano_nasc = int(input("Digite o ano de nascimento : "))

idade = ano_atual - ano_nasc
print("o ano atual é {} e o ano de nascimento é {} A sua idade é {} anos ".format(ano_atual,ano_nasc,idade))
if idade >= 18 :
    print("estás apto para conduzir.")

else:
    print("ATENÇÃO!!! Não apto para conduzir")    

    