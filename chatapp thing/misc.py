import mysql.connector


class DatabaseHandling:
    myDatabase = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="fasih123",
        database="testdatabase"
    )

    myCursor = myDatabase.cursor(buffered=True)

    def __init__(self):
        self.headerLength, self.form, self.disconnectMessage = self.getData()

    def getData(self):
        query = "SELECT headerLength, format, disconnectMessage FROM ChatData"
        self.myCursor.execute(query)
        return self.myCursor.fetchone()

    def checkUserPass(self, username, password):
        searchQuery = "SELECT username, password FROM UserInfo"

        self.myCursor.execute(searchQuery)

        for x in self.myCursor:
            user, passwd = x

            if user == username and passwd == password:
                return True

        return False

    def createNewUser(self, username, password):
        createQuery = "INSERT INTO UserInfo (username, password) VALUES (%s, %s)"
        searchQuery = "SELECT username FROM UserInfo"
        self.myCursor.execute(searchQuery)
        for x in self.myCursor:
            name, = x
            if name == username:
                return "User already exists", False
        try:
            self.myCursor.execute(createQuery, (username, password))
            self.myDatabase.commit()
            return "", True
        except:
            return "Something went wrong while adding", False
