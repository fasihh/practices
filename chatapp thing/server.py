import socket, threading, pickle
from misc import DatabaseHandling


class Server:
    db = DatabaseHandling()
    headerLength, form, disconnectMessage = db.getData()
    clients = {}

    def __init__(self):
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serverSocket.bind((socket.gethostname(), 1235))
        self.socketsList = [self.serverSocket]
        self.main()

    def addClient(self, clientSocket, username):
        user = {"clientHeader": f"{username:<{self.headerLength}}", "clientUser": username}
        self.clients[clientSocket] = user

    def handleClient(self, clientSocket, address):
        connected = True
        userAddress = f"{address[0]}:{address[1]}"
        dataTuple = pickle.dumps(self.db.getData())
        clientSocket.send(dataTuple)

        userReq, userReqStatus = pickle.loads(clientSocket.recv(2048))
        if userReqStatus:
            username, password = pickle.loads(clientSocket.recv(2048))
            if userReq == "new":
                errorMessage, status = self.db.createNewUser(username, password)

                if status:
                    self.addClient(clientSocket, username)
                    print(f"{userAddress} joined as {username}")

                connected = status
                clientSocket.send(pickle.dumps((errorMessage, status)))

            elif userReq == "login":
                try:
                    loggedIn = self.db.checkUserPass(username, password)
                    while not loggedIn:
                        clientSocket.send(pickle.dumps(loggedIn))
                        username, password = pickle.loads(clientSocket.recv(2048))
                        loggedIn = self.db.checkUserPass(username, password)

                    clientSocket.send(pickle.dumps(loggedIn))

                    self.addClient(clientSocket, username)
                    print(f"{userAddress} joined as {username}")
                except:
                    connected = False
                    print(f"{address[0]}:{address[1]} attempted to join but disconnected: {userReq}")
        else:
            connected = userReqStatus
            if userReq == "exit":
                print(f"{address[0]}:{address[1]} attempted to join but disconnected: {userReq}")


        while connected:
            messageLength = clientSocket.recv(self.headerLength).decode(self.form)

            if messageLength:
                messageLength = int(messageLength)
                message = clientSocket.recv(messageLength).decode(self.form)

                if message == self.disconnectMessage:
                    print(f"{username} has disconnected")
                    connected = False
                else:
                    print(f"{username} > {message}")

        clientSocket.close()


    def main(self):
        self.serverSocket.listen()
        print("starting...")

        while True:
            clientSocket, address = self.serverSocket.accept()
            thread = threading.Thread(target=self.handleClient, args=(clientSocket, address))
            thread.start()


serverObj = Server()

#store username and password in database
#give user option to send message where
