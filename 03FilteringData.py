from mysql.connector import connect
from password import Password

Password = Password()

database = connect(
    host = 'localhost',
    user = 'root',
    password = Password,
    database = 'DemoDB'
)

cursor = database.cursor(prepared=True)

def CreatePerson():
    try:
        query = """ create table if not exists Person (
                    name  char(50),
                    address char(200),
                    dob date,
                    ownAHouse bit default 0
                    )
                    """
        cursor.execute(query)
        database.commit()
        print('Person table created successfully')
    except Exception as e:
        print(e)


def InsertIntoPerson():
    try:
        query = """ insert into Person (name, address, dob, ownAHouse) values (?, ?, ?, ?) """
        values = [('A','Addr1','2001-01-21', 1), ('B','Addr2','2001-02-21', 0), ('AB','Addr1','2001-03-21', 1), ('AC','Addr3','2001-04-21', 0)]
        cursor.executemany(query, values)
        database.commit()
        print('Values are instered successfully into Person')
    except Exception as e:
        print(e)

def InsertSpecificValueIntoPerson():
    try:
        query = "insert into Person (name, address) values (?, ?)"
        values = [('D','Addr2')]
        cursor.executemany(query, values)
        database.commit()
        print('Specific data inserted successfully')
    except Exception as e:
        print(e)


def ViewPerson():
    try:
        query = "select * from Person"
        cursor.execute(query)
        results = cursor.fetchall()
        database.commit()
        print('Person Table Data')
        for rows in results:
            print(rows)
    except Exception as e:
        print(e)

def NameFromA():
    """ Get those data whose name is A """
    try:
        query = "select * from Person where name = 'A' "
        cursor.execute(query)
        results = cursor.fetchall()
        database.commit()
        print('Details of Person whose name is A')
        for rows in results:
            print(rows)
    except Exception as e:
        print(e)

def NameStartWithA():
    """ Get those data whose name start with A and then there are any number of character after A """
    try:
        query = "select * from Person where name like 'A%'"
        cursor.execute(query)
        results = cursor.fetchall()
        database.commit()
        print('Details of Person whose name started with A')
        for rows in results:
            print(rows)
    except Exception as e:
        print(e)



def NameFromAThenSingleCharacter():
    """ Name start with A and after A there is only one character """
    try:
        query = "select * from Person where name like 'A_'"
        cursor.execute(query)
        results = cursor.fetchall()
        database.commit()
        print('Details of Person whose name started with A and thereafter only one character')
        for rows in results:
            print(rows)
    except Exception as e:
        print(e)


def NameHaveBOnSecondPlace():
    try:
        query = "select * from Person where name like '_B%'"
        cursor.execute(query)
        results = cursor.fetchall()
        database.commit()
        print('Second character is B and thereafter any characters')
        for rows in results:
            print(rows)
    except Exception as e:
        print(e)


def PersonOfSpecificAddress():
    try:
        query = "select * from Person where address = 'Addr1' or address = 'Addr3'"
        cursor.execute(query)
        results = cursor.fetchall()
        database.commit()
        print('PersonOfSpecificAddress')
        for rows in results:
            print(rows)
    except Exception as e:
        print(e)


def PersonOfSpecificAddressWithDifferentWay():
    try:
        query = "select * from Person where address in ('Addr1' ,'Addr3')"
        cursor.execute(query)
        results = cursor.fetchall()
        database.commit()
        print('PersonOfSpecificAddress with different way')
        for rows in results:
            print(rows)
    except Exception as e:
        print(e)


def SpecificAddress():
    try:
        query = "select * from Person where address not in ('Addr1' ,'Addr3')"
        cursor.execute(query)
        results = cursor.fetchall()
        database.commit()
        print('SpecificAddress')
        for rows in results:
            print(rows)
    except Exception as e:
        print(e)

def DOBBetween():
    try:
        query = "select * from Person where dob between '2001-01-21' and '2001-03-21';"
        cursor.execute(query)
        results = cursor.fetchall()
        database.commit()
        print('DOB Between')
        for rows in results:
            print(rows)
    except Exception as e:
        print(e)

def MonthDOB():
    try:
        query = "select * from Person where ownAHouse = 1 and Month(dob) = 3"
        cursor.execute(query)
        results = cursor.fetchall()
        database.commit()
        print('Month DOB')
        for rows in results:
            print(rows)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    databasename = 'DemoDB'
    # CreatePerson()
    # InsertIntoPerson()
    # InsertSpecificValueIntoPerson()
    # ViewPerson()
    # NameFromA()
    # NameStartWithA()
    # NameFromAThenSingleCharacter()
    # NameHaveBOnSecondPlace()
    # PersonOfSpecificAddress()
    # PersonOfSpecificAddressWithDifferentWay()
    # SpecificAddress()
    # DOBBetween()
    # MonthDOB()
