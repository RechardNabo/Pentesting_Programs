from socket import socket, SOCK_DGRAM, AF_INET


class UDP_Connection:

    def Pocket_sender(self, src_adr, port):
        Src_adr = src_adr
        Src_prt = port
        data = '1024'
        s = socket(AF_INET, SOCK_DGRAM)
        s.sendto(data.encode(), (Src_adr, Src_prt))
        print("pocket sent successfully")

    def Pocket_receiver(self, src_adr, src_port):
        Src_adr = src_adr
        Src_port = src_port
        s = socket(AF_INET, SOCK_DGRAM)
        s.bind((Src_adr, int(Src_port)))
        while True:
            msg = s.recv(1024)
            print("Receiving pockets from :" + str(msg))


def main(self):
    print("########################################")
    print("# Welcome to Socket Software using UDP #")
    print("#      sending pockets network         #")
    print("########################################")
    option = input('Would you like to send or receive pockets s/S = send  r/R = Receive \n')
    Network = UDP_Connection
    if option == "r" or option == 'R':
        src_adr = input("please enter the address to receiver pockets from \n :")
        src_port = input("please enter the port you would like to use [Default] 6667 \n :")
        Network.Pocket_receiver(self, src_adr, int(src_port))
    if option == "s" or option == "S":
        src_adr = input("please enter the address you want to send the pockets to \n :")
        src_port = input("please enter the port number [Default] 6667 \n :")
        Network.Pocket_sender(self, src_adr, int(src_port))
    else:
        print("******thank you******")
    # print("# Thank you  operation completed successfully")


if __name__ == "__main__":
    main("")
