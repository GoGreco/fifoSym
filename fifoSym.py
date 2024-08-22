p1 = ['p1', 0, 1]
p2 = ['p2', 0, 2]
p3 = ['p3', 1, 1]
p4 = ['p4', 0, 15]
p5 = ['p5', 2, 10]

#definindo fila
fila = [p1, p2, p3, p4, p5]

#organizar a fila
fila = sorted(fila, key= lambda x : x[1])

#definindo um tempo
tempo = 0
overhead = 1

#criar uma flag
processosCompletos = 0

#tempos de resposta, retorno espera
'''
tempo de resposta (inicio de exec - chegada)
tempo de retorno (final de execução - chegada)
tempo de espera (tempo de retorno - tempo de resposta)
'''
tempoResposta = []
tempoRetorno = []
tempoEspera = []


#criar o loop de execução
n = 0

while processosCompletos != 5:

    #adicionando o nome do processo atualmente no registrador
    #e também o tempo atual antes de quaisquer alterações, menos o tempo de chegada do processo na fila

    tempoResposta.append([fila[n][0], tempo - fila[n][1]])

    #como o processo, ficará no registrador até ser completo, simplesmente vou somar o tempo de execução no tempo cronológico do processo, e tornar o tempo de execução restante 0
    tempo += fila[n][2]
    fila[n][2] = 0
    processosCompletos += 1
    
    #adicionando o nome do processo que acabou de terminar seu tempo no processador
    #e também o tempo atual após as mudanças causadas pelo processo meno o tempo de chegada do mesmo
    tempoRetorno.append([fila[n][0], tempo - fila[n][1]])

    #após a execução do processo, os barramentos trocam quem está na cpu, e gera-se overhead
    tempo += overhead
    n+=1


somaReposta = 0
somaRetorno = 0
for n in range(len(tempoResposta)):
    tempoEspera.append([fila[n][0], tempoRetorno[n][1]-tempoResposta[n][1]])

    somaReposta+=tempoResposta[n][1] 
    somaRetorno+=tempoRetorno[n][1]


mediaResposta = somaReposta/len(tempoResposta) 
mediaRetorno = somaRetorno/len(tempoResposta)

print("p1->p2->p4->p3->p5")

print(f'''Tempo de resposta: {tempoResposta}''')
print(f'''Tempo de retorno: {tempoRetorno}''')
print(f'''Tempo de espera: {tempoEspera}''')
print(f'''A media do tempo de resposta é: {mediaResposta}''')
print(f'''A media do tempo de retorno é: {mediaRetorno}''')
