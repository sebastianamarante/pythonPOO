import psycopg2

# Postgres

try:
    # Conectarse a la base de datos
    conexion = psycopg2.connect(host="localhost", port="5432", database="postgres", user="postgres", password="<unique PostgreSQL password>")


    # Creamos el cursor con el objeto conexion
    cur = conexion.cursor()
    cur2 = conexion.cursor()

    # Ejecutamos una consulta
    sqlquery = "insert into softone (id, ingresos, gastos) values (4, 100, 50);"
    cur2.execute(sqlquery)
    cur.execute("SELECT * FROM softone s;")

    # Recorremos los resultados y los mostramos

    for id, ingresos, gastos in cur.fetchall():
        print (id, ingresos, gastos)

    # Cerramos la conexión
    conexion.commit()
    cur.close()
    conexion.close()
    
except:
    print("Error de base de datos")