from __future__ import with_statement #for python 2.5
import platform
import socket
import psutil
import os
import sys


#install psutils

message = "Server"


# msg_split = message.split()[0]
while message != "kill":

    server_socket = socket.socket()
    server_socket.bind(("0.0.0.0", 65432))

    print(f"L'OS : {platform.system()}")
    print(f"L'Hostname : {socket.gethostname()}")
    print(f"L'IP : {server_socket.getsockname()[0]}")

    server_socket.listen(1)
    print('Serveur en attente de connexion')
    while message != "kill" and message != "reset":
        message = ""

        try :
            conn, addr = server_socket.accept()
            print(addr)
        except ConnectionError:
            print("erreur de connection")
            break
        else:
            while message != "kill" and message != "reset" and message != "disconnect":
                message = conn.recv(1024).decode()
                try:
                    msg_split = message.split()[0]
                    msg_split1 = message.split(':')[1]
                except:
                    pass

                if message == "name":
                    host = socket.gethostname()
                    # print(f"Le message vien de : {host}")
                    conn.send(f"le nom de l'host {host}".encode())

                if message == 'version':
                    vers = sys.version
                    # print("\n Version actuelle :\n", sys.version)
                    conn.send(str(f'\nVoici la version de python : \n {vers}').encode())

                if message == "cpu":
                    load1, load5, load15 = psutil.getloadavg()
                    Cpu_usage = (load15 / os.cpu_count()) * 100
                    # print("l'usage du CPU est  ", Cpu_usage)
                    conn.send(f"L'usage du CPU est de {str(Cpu_usage)}%".encode())


                if msg_split == ('powershell'):
                    ps_data = os.popen(message).read()
                    # print(ps_data)
                    conn.send(ps_data.encode())

                try:
                    if message == (f'DOS:{msg_split1}'):
                        ps_data1 = os.popen(msg_split1).read()
                        # print(ps_data)
                        conn.send(ps_data1.encode())
                except:
                    pass
                if message == 'ip':
                    ip = (str(server_socket.getsockname()[0]))
                    # print(f"L'IP du server est : {ip}")
                    conn.send(f"L'IP du server est : {ip}".encode())


                if message == "os":
                    # print(f"\nL'os est : {platform.system()}")
                    conn.send(f"\nL'os est : {platform.system()}".encode())


                if message == "ram":
                    # print(f"Ram :{psutil.virtual_memory()}")
                    ram = str(psutil.virtual_memory())
                    conn.send(f'Le test de la Ram aboutie à : {ram}'.encode())

                if message == 'mkdir':
                    nom = ('DossierTOP')
                    os.mkdir(nom)
                    conn.send(f'\n Le fichier /{nom}/ est crée'.encode())
                    # print(f'\n Le fichier {nom} à été crée !')

                if message == "dir":
                    com = os.popen('dir').read()
                    # print(f'\nVoici la commande dir \n{com}')
                    conn.send(f'\nVoici la commande dir \n {com}'.encode())

                if message == 'ping':
                    ip = "8.8.8.8"
                    ping = os.popen(f"ping {ip}").read()
                    # print(f'\nVoici le ping : \n{ping}')
                    conn.send(f'\nVoici le ping : \n {ping}'.encode())

                if message == 'get-process':
                    process = os.popen('wmic process get description, processid').read()
                    conn.send(process.encode())

            conn.close()

    print("Connection fini")
    server_socket.close()
    print("Server fermer")
