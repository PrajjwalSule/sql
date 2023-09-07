from mysql.connector import connect

database = connect(
    host="localhost",
    user="root",
    password='password',
    database = 'DemoDB'
)

cursor = database.cursor(prepared=True)

def CreateUserProfile():
    try:
        query = """
                CREATE TABLE IF NOT EXISTS `UserProfile`(
                `ProfileID`    INT,
                `FirstName`	   VARCHAR(50),
                `LastName`     VARCHAR(50),
                `email`        VARCHAR(50)
                 );
                """
        cursor.execute(query)
        database.commit()
        print('UserProfile table created successfully')
    except Exception as e:
        print(e)


def CreateContact():
    try:
        query = """
                CREATE TABLE IF NOT EXISTS `Contact`(
                `ContactID`    INT,
                `FirstName`	   VARCHAR(50),
                `LastName`     VARCHAR(50),
                `email`        VARCHAR(50)
                );
                """
        cursor.execute(query)
        database.commit()
        print('Contact table created successfully')
    except Exception as e:
        print(e)

def InsertDataIntoUserProfile():
    try:
        query = "INSERT INTO `UserProfile` (`ProfileID`, `FirstName`, `LastName`, `email`) VALUES (?, ?, ?, ?)"
        values = [(1, 'A', 'A', 'a@test.com'), (2, 'B', 'B', 'b@test.com'), (3, 'C', 'C', 'c@test.com')]
        cursor.executemany(query, values)
        database.commit()
        print('Data into UserProfile has been inserted successfully')
    except Exception as e:
        print(e)

def ViewUserProfile():
    try:
        query = "SELECT * FROM `UserProfile`"
        cursor.execute(query)
        results = cursor.fetchall()
        database.commit()
        print('Data of UserProfile')
        for rows in results:
            print(rows)
    except Exception as e:
        print(e)


def InsertWithSeletIntoContact():
    try:
        query = "INSERT INTO `Contact` SELECT * FROM `UserProfile`"
        cursor.execute(query)
        database.commit()
        print('Inserted all the data from UserProfile into Contact table')
    except Exception as e:
        print(e)


def ViewContact():
    try:
        query = "SELECT * FROM `Contact`"
        cursor.execute(query)
        results = cursor.fetchall()
        database.commit()
        print('Data of Contact table')
        for rows in results:
            print(rows)
    except Exception as e:
        print(e)


def CreateNewContact():
    try:
        query = """ CREATE TABLE IF NOT EXISTS `NewContact`(
                    `ContactID`    INT Auto_Increment,
                    `Name`	   VARCHAR(50),
                    `Email`     VARCHAR(50),
                    PRIMARY KEY(`ContactID`)
                )
                """
        cursor.execute(query)
        database.commit()
        print('NewContact table is created successfully')
    except Exception as e:
        print(e)

def InsertWithSelectDifferentColumns():
    """ NewContact accept Name instead of FirstName and LastName so we concat those into Name column"""
    try:
        query = """ INSERT INTO `NewContact`(`Name`,`Email`) 
                    SELECT Concat(`FirstName`, Concat(' ', `LastName`)), `Email` FROM `UserProfile`
                     """
        cursor.execute(query)
        database.commit()
        print('Insert the UserProfile data into NewContact table While concating the firstname and lastname into name')
    except Exception as e:
        print(e)

def ViewNewContact():
    try:
        query = "SELECT * FROM `NewContact`"
        cursor.execute(query)
        results = cursor.fetchall()
        database.commit()
        for rows in results:
            print(rows)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    databasename = 'DemoDB'
    # CreateUserProfile()
    # CreateContact()
    # InsertDataIntoUserProfile()
    # ViewUserProfile()
    # InsertWithSeletIntoContact()
    # ViewContact()
    # CreateNewContact()
    # InsertWithSelectDifferentColumns()
    # ViewNewContact()