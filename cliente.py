from socket import *

servidor = 'localhost'

porta = 3333

varSock = socket(AF_INET, SOCK_STREAM)
varSock.connect((servidor, porta))

while True:
	mensagem = 'SD é muito interessante!'
	varSock.send(mensagem.encode())
	data = varSock.recv(1024)
	print(data.decode())

	varSock.close()
