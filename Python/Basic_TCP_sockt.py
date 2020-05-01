from socket import socket, SOCK_STREAM, AF_INET
from pip._vendor.six import b


class TCP_Connection:

    def pocket_receiver(self, src_adr, src_prt):
        Scr_prt = src_prt
        Src_ard = src_adr
        s = socket(AF_INET, SOCK_STREAM)
        s.connect((Src_ard, int(Scr_prt)))
        s.listen(5)
        counter = 0
        while True:
            if counter == 10:
                s.close()
                break
            msg = s.recv(1024)
            print("Receiving pockets " + msg)
            counter = +1

    def pocket_sender(self, src_adr, src_prt):
        Src_adr = src_adr
        Src_prt = src_prt
        s = socket(AF_INET, SOCK_STREAM)
        s.connect((Src_adr, int(Src_prt)))
        s.send(b, "Sender")


def main(self):
    print("########################################")
    print("# Welcome to Socket Software using TCP #")
    print("#      sending pockets network         #")
    print("########################################")
    option = input('Would you like to send or receive pockets s/S = send  r/R = Receive \n')
    Network = TCP_Connection
    if option == "r" or option == 'R':
        src_adr = input("please enter the address to receiver pockets from \n :")
        src_port = input("please enter the port you would like to use [Default] 5000 \n :")
        Network.pocket_receiver(self, src_adr, int(src_port))
    if option == "s" or option == "S":
        src_adr = input("please enter the address you want to send the pockets to \n :")
        src_port = input("please enter the port number [Default] 5000 \n :")
        Network.pocket_sender(self, src_adr, int(src_port))
    else:
        print("******thank you******")
    # print("# Thank you  operation completed successfully")


if __name__ == "__main__":
    main("")
