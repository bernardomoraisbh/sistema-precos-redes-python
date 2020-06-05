import socket
import _thread
import os
import re

list = []
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

############################################################## CLASSES
class Posto:
    
    msg_type   = None
    msg_id     = None
    fuel_type  = None   # combustivel 0 - diesel, 1 - álcool, 2 - gasolina
    fuel_price = None
    latitude   = None
    longitude  = None
    
    def __init__(self, type, id, fuel_type, price, lat, long):
        self.msg_type    = type
        self.msg_id      = id
        self.fuel_type   = fuel_type
        
        int_price = int(re.sub('[^\d]','', price))
        if int_price < 10:
            int_price = int_price * 1000
        elif int_price < 100:
            int_price = int_price * 100
        elif int_price < 1000:
            int_price = int_price * 10
        
        self.fuel_price  = int_price
        
        self.latitude    = lat
        self.longitude   = long
    
    def getString(self):
        return str(self.msg_type + " " + self.msg_id + " " + self.fuel_type + " " + str(self.fuel_price) + " " + self.latitude  + " " + self.longitude + "\n")
    
    def saveToFile(self):
        #directory = os.getcwd() # Pegar diretorio atual para criar "banco de dados"
        posto_file = open('postos.txt', 'a', encoding='utf-8') # Criar banco
        posto_file.write(self.getString())
        posto_file.close()

##############################################################


############################################################## CONFIGURACOES DO SERVIDOR ( IP / PORTA )
print ('Para começar digite: \nservidor <porta>\n')

server_info = input().split(' ')
if server_info[0] != "servidor" and len(server_info) != 2 and server_info[1].isdigit():
    sys.exit()

#Dados para conexao
HOST = ''
PORT = int(server_info[1])

udp.bind((HOST, PORT))
##############################################################

# Ler postos de arquivo
if os.path.isfile("postos.txt") :
    file = open("postos.txt", "r")
    for line in file:
        if line:
            valores = line.replace("\n","").split(' ')
            list.append ( Posto(valores[0], valores[1], valores[2], valores[3], valores[4], valores[5]) )
        else:
            break
    file.close()

# Funcao de busca
def search(tipo, raio, latitude, longitude):
    resposta = None
    preco = 5555
    for posto in list:
        if posto.fuel_price <= preco and posto.fuel_type == tipo and (float(latitude)-float(raio) <= float(posto.latitude) <= float(latitude)+float(raio)) and (float(longitude)-float(raio) <= float(posto.longitude) <= float(longitude)+float(raio)):
            resposta = posto
            preco = posto.fuel_price
    return resposta

while True:
    msg, cliente = udp.recvfrom(1024)
    msg = msg.decode('UTF-8')
    print (cliente, msg)
    
    valores = msg.split(' ')
    
    if (len(valores) == 6 and valores[0] == 'D'): #Checar se chegaramm 6 atributos
        posto = Posto(valores[0], valores[1], valores[2], valores[3], valores[4], valores[5])
        posto.saveToFile()
        list.append(posto)
        print("Posto inserido no banco de dados!" )
        udp.sendto ("Resposta do servidor: dados recebidos".encode('UTF-8'), cliente)
    elif (len(valores) == 6 and valores[0] == 'P'):
        print("Buscando dados..." )
        resposta = search(valores[2], valores[3], valores[4], valores[5])
        if resposta != None:
            resp = "Resposta do servidor: dados encontrados / R$ " + str(resposta.fuel_price/1000)
            print("Posto localizado..." )
        else:
            resp = "Resposta do servidor: dados nao encontrados"
            print("Nenhum posto localizado..." )
        udp.sendto (resp.encode('UTF-8'), cliente)
    else:
        print("Dados invalidos")
        udp.sendto ("Resposta do servidor: dados invalidos".encode('UTF-8'), cliente)
    
udp.close()