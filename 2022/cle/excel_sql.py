import sqlite3
import pandas


def create_connexion(db_file):
    print(f"open {db_file!r}")
    return sqlite3.connect(db_file)


def add_file(db_file, excel_file, table_name="data"):
    """
    Adds a file to a database.

    :param db_file: database file
    :param excel_file: excel file to add
    :param table_name: name of the table
    """
    con = create_connexion(db_file)    
    print(f"read {excel_file!r}")
    df = pandas.read_excel(excel_file)
    df.to_sql("data", con)
    con.close()


if __name__ == "__main__":
    # excel_file = r"c:\temp\example.xlsx"
    import fire
    fire.Fire({'add_file': add_file})
