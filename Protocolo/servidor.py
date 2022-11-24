# protocolo de aplicação
# programa SERVIDOR

from socket import *

# define a porta que será monitorada
porta = 12000

# cria o socket para o programa do servidor
socketServidor = socket(AF_INET, SOCK_STREAM)

# liga o socket na porta
socketServidor.bind( ('', porta) )

# começa a monitorar (escutar) a porta
socketServidor.listen(True)

print("Servidor escutando a porta ", porta)

while True:
    cliente, endereco = socketServidor.accept()

    mensagemRecebida = cliente.recv(1024)
    mensagemRecebida = mensagemRecebida.decode()

    print("Recebido",mensagemRecebida,". De ",endereco)

    # aqui é onde de fato o protocolo é resolvio
    if(mensagemRecebida == "oi"):
        retorno = "eae"
    elif (mensagemRecebida == "tudo certo?"):
        retorno = "tamo indo né"
    elif (mensagemRecebida == "quais as novidades?"):
        retorno = "o novo pokemon lancou!"
    elif (mensagemRecebida == "serio?"):
        retorno = "aham"
    else:
        retorno = "q q se disse? Não entendi"
    
    retorno = retorno.encode()
    cliente.send(retorno)

    cliente.close()