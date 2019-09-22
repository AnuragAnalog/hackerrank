#!/usr/bin/python3

def txt2db(ftxt: str, fsql: str, dbname: str) -> None:
    fhtxt = open(ftxt, "r")
    fhsql = open(fsql, "a")

    fhsql.write("\n")
    for row in fhtxt:
        val = row.split(",")

        query = "insert into "+dbname+" values ("
        for x in val:
            if x == val[-1]:
                query = query + (x[:-1])
            else:
                query = query + (x+",")
        query = query + ");\n"

        fhsql.write(query)
    fhsql.close()
    fhtxt.close()

if __name__ == '__main__':
    ftxt = input("Enter the name of csv: ")
    fsql = input("Enter the name of sql: ")
    dbname = input("Enter the name of table: ")

    txt2db(ftxt, fsql, dbname)
