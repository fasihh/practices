import socket, pickle, sys


class Client:
    def __init__(self):
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clientSocket.connect((socket.gethostname(), 1235))

        dataTuple = self.recvObj(2048)
        self.headerLength, self.form, self.disconnectMessage = dataTuple

        option = input("1: Create new user \n2: Login \n3: Exit (type any value to exit)")

        if option == "1":
            userInfoTuple = self.UserPass()
            self.sendObj(("new", True))
            self.sendObj(userInfoTuple)
            errorMessage, status = self.recvObj(2048)

            if not status:
                    print(errorMessage)
                    sys.exit()

        elif option == "2":
            userInfoTuple = self.UserPass()
            self.sendObj(("login", True))
            self.sendObj(userInfoTuple)
            userExists = self.recvObj(16)

            while not userExists:
                print("Invalid Login")
                userInfoTuple = self.UserPass()
                self.sendObj(userInfoTuple)
                userExists = self.recvObj(16)
        else:
            self.sendObj(("exit", False))
            sys.exit()

        self.start()

    def start(self):
        print(f"type '{self.disconnectMessage}' to disconnect")

        connected = True
        while connected:
            message = input("> ")
            self.send(message)

            if message == self.disconnectMessage:
                print("- - disconnecting - -")
                connected = False


    def sendObj(self, message):
        pickledMessage = pickle.dumps(message)
        self.clientSocket.send(pickledMessage)

    def recvObj(self, length):
        return pickle.loads(self.clientSocket.recv(length))

    def send(self, message):
        self.clientSocket.send(f"{len(message):<{self.headerLength}}".encode(self.form) + message.encode(self.form))

    def recv(self):
        messageHeader = self.clientSocket.recv(self.headerLength)
        message = self.disconnectMessage.recv(int(messageHeader.decode(self.form)))
        return message.decode(self.form)

    @staticmethod
    def UserPass():
        username = input("username: ")

        while not username:
            print("Please input a valid username")
            username = input("username: ")

        password = input("password: ")

        while not password:
            print("Please input a valid password")
            password = input("password: ")

        return username, password

clientObj = Client()

"""""
        if not userExists:
            print("Invalid login")
            option = input("Do you want to retry or make a new user (type E for exit)? (R/N): ").lower()
            while option != "y" and option != "n" and option != "e":
                option = input("Do you want to make a new user? (R/N): ").lower()

            if option == "n":
                    username, password = self.UserPass()
                    self.sendObj(("new", True))
                    self.sendObj((username, password))
                    errorMessage, status = self.recvObj(2048)
                    print(errorMessage)
                    if not status:
                        sys.exit()
            elif option == "e":
                self.clientSocket.send(pickle.dumps(("", False)))
                sys.exit()
            elif option == "r":
                userInfoTuple = self.UserPass()
                self.sendObj(userInfoTuple)
                userExists = self.recvObj(16)
"""""

