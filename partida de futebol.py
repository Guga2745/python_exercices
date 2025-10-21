equipa1 = int(input("Digite os golos do Sporting : "))
equipa2 = int(input("Digite os golos do Benfica : "))

diferença_golos = equipa1 - equipa2

print("Diferença : {}" .format(diferença_golos) )

if diferença_golos == 0 :
    print("Empate")
elif diferença_golos in [1,2,3,4]:
 print("Partida normal")
else:
   print("Goleada")