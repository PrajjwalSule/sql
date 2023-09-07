from mysql.connector import connect


connection = connect(
  host="localhost",
  user="root",
  password='password', 
)

cursor = connection.cursor()

def CreateDatabase(name):
    try:
        query = f'CREATE DATABASE IF NOT EXISTS {name}'
        cursor.execute(query)
        print(f'{name} is successfully created')
    except Exception as e:
        print(e)

def CreateEmployeeTable(db_name):
    try:
        query = f"""
                    CREATE TABLE IF NOT EXISTS {db_name}.`Employee`(
                            `EmpID`  		INT,
                            `FirstName`		VARCHAR(50),
                            `LastName`	    VARCHAR(50),
                            `Salary`	    NUMERIC(20,2)
                        );

                    """
        cursor.execute(query)
        connection.commit()
        print('Employee table is successfully created')
    except Exception as e:
        print(e)


def InsertDataIntoEmployee(db_name):
    try:
        query = f""" INSERT INTO {db_name}.`Employee`
                     VALUES (1, 'A', 'A', 1000);
                        """
        cursor.execute(query)
        connection.commit()
        print('Data inserted into Employee table')
    except Exception as e:
        print(e)

def MultipleInstertEmployee(db_name):
    try:
        cursor = connection.cursor(prepared=True)
        query = f"INSERT INTO {db_name}.`Employee` (`EmpID`, `FirstName`, `LastName`, `Salary`) VALUES (?, ?, ?, ?)"
        values = [(2, 'B', 'B', 2000), (3, 'C', 'C', 3000), (4, 'D', 'D', 3000), (5, 'E', 'E', 5000)]
        cursor.executemany(query, values)
        connection.commit()
        print('Inserted many data in one go')
    except Exception as e:
        print(e)

def ViewEmployeeData(db_name):
    try:
        query = f"SELECT * FROM {db_name}.`Employee`"
        cursor.execute(query)
        results = cursor.fetchall()
        connection.commit()
        print('Data of Employee table')
        for rows in results:
            print(rows)
    except Exception as e: 
        print(e)

if __name__ == '__main__':
    db_name = 'DemoDB'
    # CreateDatabase(db_name)
    # CreateEmployeeTable(db_name)
    # InsertDataIntoEmployee(db_name)
    # MultipleInstertEmployee(db_name)
    # ViewEmployeeData(db_name)
    

