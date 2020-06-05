import socket
import _thread
import time
import sys
import ipaddress

stored_exception=None

#UDP DATA
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def testar_ip(ip):
    try:
        ip = ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

print ('Para sair use CTRL+C\n')
print ('Para começar digite: \ncliente <ip> <porta>\n')

server_info = None
while True:
    server_info = input().split(' ')
    if server_info[0] == "cliente" and len(server_info) == 3 and testar_ip(server_info[1]):
        break
    print("Dados inválidos")
    
#Dados para conexao
HOST = str(server_info[1])
PORT = int(server_info[2])

dest = (HOST, PORT)
print("Digite D para cadastrar posto ou P para pesquisar posto")
#Start Client loop until CTRL-C
while True:
    try:
        entrada = input()
        msg = (entrada.encode('utf-8'))
        
        udp.sendto (msg, dest)
        
        #Receive confirmation
        udp.settimeout(5.0)
        msg, cliente = udp.recvfrom(1024)
        if msg:
            print(msg.decode('UTF-8'))

    except KeyboardInterrupt:
        stored_exception = sys.exc_info()
        break;
        
#Say Goodbye
print("Bye")

#Raise Exceptions
if stored_exception:
    for exception in stored_exception:
        raise exception
    
udp.close()