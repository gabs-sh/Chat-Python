from socket import *

host = 'localhost'

porta = 50007

varSock = socket(AF_INET, SOCK_STREAM)

varSock.bind((host,porta))

varSock.listen(1)

while True:
	print('Aguardando conexão...')
	conexao, end = varSock.accept()
	print("Conexão estabelecida pelo endereço", end)
	
	while True:
		data = conexao.recv(1024)
		if not data:break
		print('Ele: ' + data.decode())
		resposta = input('Você: ')
		conexao.send(resposta.encode())

	conexao.close()


