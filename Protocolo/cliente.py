# Protocolo de Aplicação
# programa do CLIENTE

from socket import *

enderecoServidor = '127.0.0.1'
portaServidor = 12000


while True:
    # socketCliente = socket( versaoIP , protocoloTransporte  )
    # AF_INET é o IPv4, e o SOCK_STREAM é o TCP
    socketCliente = socket( AF_INET , SOCK_STREAM )

    # connect exige um tupla para endereçar as mensagens
    socketCliente.connect( (enderecoServidor,portaServidor) )
    
    # pergunta para o usuário cliente qual a mensagem a ser 
    # enviada
    mensagem  = input("Escreva a mensagem : ")

    # prepara a mensagem para envio
    mensagem = mensagem.encode()

    # envia a mensagem
    socketCliente.send(mensagem)

    # recebe o retorno/resposta da mensagem
    retorno = socketCliente.recv(1024)
    retorno = retorno.decode()

    # mostra a mensagem recebida do servidor
    print ("O servidor respondeu : ", retorno)

    print ("---------------")

    # fecha o socket (a conexao)
    socketCliente.close()
