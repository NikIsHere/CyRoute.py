import sqlite3
from pyFiles import config
from sqlite3 import Error

table = config.table

def create_connection(db_file):
    """ create a database connection to a SQLite database """

    print("Now trying to connect to sqlite3 Database or if not existent creating it for you!")

    try:
        global conn
        conn = sqlite3.connect(db_file)
        print("Connection built successfully! SQLite Ver. is: " + sqlite3.version)

        global cursor
        cursor = conn.cursor()

        sql_command = """
        CREATE TABLE IF NOT EXISTS {} ( 
        IDnr INTEGER PRIMARY KEY, 
        IPaddr TEXT, 
        latitude REAL, 
        longitude REAL, 
        Os TEXT);
        """.format(table)

        cursor.execute(sql_command)
        conn.commit()
        print("Main Database Table built if it didn't exist already...")

        addValues("127.0.0.1",1,2,"Win")

    except Error as e:
        print(e)

def addValues(IPaddr, latitude, longitude, Os):


        sql_command = sql_command = """
                    INSERT INTO {} (
                    IPaddr,
                    latitude,
                    longitude,
                    Os
                    ) VALUES (
                    "{}",
                    {},
                    {},
                    "{}"
                    )
                    ;
                    """.format(table,IPaddr, latitude, longitude, Os)

        if(config.verbose):
            print(("VERBOSE: Inserted the following values to Table {} IPaddr: {},Latitude: {}"
                   ",Longitude: {},Os: " + Os).format(table,IPaddr,latitude,longitude,Os))
        cursor.execute(sql_command)
        conn.commit()



def closeConnection():
        conn.close()



if __name__ == "__main__":
    create_connection("CyRoute.db")