from socket import *

servidor = 'localhost'

porta = 50007

varSock = socket(AF_INET, SOCK_STREAM)
varSock.connect((servidor, porta))

while True:
	mensagem = input('Você: ')
	varSock.send(mensagem.encode())
	data = varSock.recv(1024)
	print('Ele: '+ data.decode())

varSock.close()
