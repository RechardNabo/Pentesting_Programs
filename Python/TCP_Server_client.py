import sys
from socket import *


class Socket_Server:

    def Server(self, src_adr, src_prt):
        try:
            print("[+] starting server . . .")
            Src_adr = src_adr
            Src_prt = src_prt
            s = socket(AF_INET, SOCK_STREAM)
            s.bind((Src_adr, int(Src_prt)))
            s.listen(5)
        except OSError:
            print("Unable to start the server check the IP Address or the port ID")
            sys.exit()

        print("[+] server listening . . .")
        while True:
            connection, ip_Address = s.accept()
            data_buffer = connection.recv(64)
            if len(data_buffer) > 0:
                print("[+] connection successfully " + str(data_buffer) + "\n[+]Client IP Address :" + str(connection.getpeername()) +
                      "\n" + str(connection.getsockname() +
                                 "\n[+]Your server service running on :" + str(connection.getsockopt())))

    def Client(self, src_adr, src_prt, data):
        Src_adr = src_adr
        Src_prt = src_prt
        Data = data
        s = socket(AF_INET, SOCK_STREAM)
        s.connect((Src_adr, int(Src_prt)))
        s.send(Data.encode())
        print("Connection successfully requested")


def main(self):
    print("#####################################")
    print("#  Welcome to TCP SERVER / CLIENT   #")
    print("#####################################")
    option = input("would you like to start a server or connect as a client to server\n s/S server or c/C client "
                   "connection \n :")

    if option == "s" or option == "S":
        server_ip = input("please enter IP address for server \n :")
        port_id = input("please enter the port ID \n :")
        tcp_server = Socket_Server
        tcp_server.Server(self, server_ip, port_id)
    if option == "c" or option == "C":
        tcp_server = Socket_Server
        src_adr = input("please enter the address of the server you want to connect to \n :")
        src_prt = input("please  enter the port you would like to use  [default] 5000 \n :")
        data = input("please enter the data to send \n :")
        tcp_server.Client(self, src_adr, src_prt, data)


if __name__ == "__main__":
    main("")
