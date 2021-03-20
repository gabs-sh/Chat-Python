from socket import *

host = 'localhost'

port = 3333

RECEIVED_MESSAGES = 0

varSock = socket(AF_INET, SOCK_STREAM)

varSock.bind((host,port))

varSock.listen(100)

while True:
	print('Aguardando conexão...')
	conexao, end = varSock.accept()
	print("Conexão estabelecida pelo endereço IP:", end[0])
	print("Porta do cliente: ", end[1])

	while True:

		data = conexao.recv(1024)

		if not data: break

		RECEIVED_MESSAGES = RECEIVED_MESSAGES + 1

		print('Mensagem do cliente: ' + data.decode())

		resposta = 'Mensagem ' + data.decode() + ' recebida com sucesso!'

		conexao.send(resposta.encode())

	conexao.close()

	print('Total de mensagens recebidas: ', RECEIVED_MESSAGES)
