## La librería sqlite

SQLite en general, es una base de datos *server-less* que se puede utilizar en
casi todos los lenguajes de programación, incluido Python.

Server-less significa
que no hay necesidad de instalar un servidor separado para trabajar con SQLite
para que pueda conectarse directamente con la base de datos.

La librería sqlite de pYthon nos permite conectarnos y usar este sistema
gestor de base de datos desde Python.


### Crear una conexión

El primer paso, como siempre,es importar el módulo sqlite3.

Luego, crearemos una conexión llamando a la función `connect()`. Como parámetro, tenemos
que pasarle el nombre del fichero donde está (o estará, si es la primera vez que
nos conectamos) la base de datos:

    import sqlite3

    con = sqlite3.connect('database.db')

Si es la primera vez que nos conectamos, sqlite crea una base de datos nueva
y la almacena en el fichero indicado; en este ejemplo `database.db`.

Ejercicio: Crear una base de datos llamada `ejemplo.db`

### Cursores

Para ejecutar sentencias de SQLite en Python, necesita un objeto `cursor`. Puedes
crearlo utilizando el método `cursor()` de la conexion.

Para ejecutar sentencias de SQLite3, primero se establece una conexión y luego
se crea un objeto cursor utilizando el objeto de conexión de la siguiente
manera:

    con = sqlite3.connect('ejemplo.db')
    cursor = con.cursor()

Ahora podemos usar el objeto `cursor` para llamar a su método `execute()`
para ejecutar cualquier consulta SQL.

#### Crear una base de datos en RAM

Cuando creas una conexión con SQLite, un archivo de base de datos se crea
automáticamente si no existe ya. Este archivo de base de datos se crea en el
disco, ademas, también podemos crear una base de datos en la RAM usando el
nombre especial `:memory:` como parametro de la función de conexión. Esta base
de datos se llama base de datos en memoria.

### Crear una tabla

Para crear una tabla en SQLite3, puede usar la sentencia `CREATE TABLE` en el
método `execute()`. 
Veamos el siguiente ejemplo:

import sqlite3

    con = sqlite3.connect('ejemplo.db')
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE employee (
            id integer PRIMARY KEY,
            name text,
            salary real
        """)
    con.commit()


Para verificar si nuestra tabla está creada, puedes utilizar el navegador de la
base de datos de sqlite para ver tu tabla. Abre tu archivo `ejemplo.db` con
este programa y deberías ver tu tabla:


### Insertar en una tabla

Para insertar datos en una tabla, usamos la sentencia `INSERT INTO`.

    con = sqlite3.connect('ejemplo.db')
    cur = con.cursor()
    cur.execute("""
        INSERT INTO employee (id, name, salary)
        VALUES (1, 'John Smith', 1200)
        """)
    con.commit()

Podemos verificar que se han insertado los datos con el navegador.

### Pasar argumentos a la sentencia SQL

Podemos pasar valores / argumentos a las sentencias INSERT en el método `execute ()`. 
Se usa el signo de interrogación como un indicador por posicion de cada argumento. Luego
hay que añadir como segundo parametro, sdespues de la sentencia SQL, una tupla
con tantos valores como argumentos hayamos declarado en la sentencia.

Como siempre, se ve mejor con un ejemplo:

    con = sqlite3.connect('ejemplo.db')
    cur = con.cursor()
    user_id = 2
    user_name = "Robert Mill"
    user_salary = 1400
    cur.execute("""
        INSERT INTO employee (id, name, salary)
        VALUES (?, ?, ?)
        """, (user_id, user_name, user_salary))
    con.commit()


### Actualizar una tabla

Para actualizar valores en una tabla se usa la
sentencia `UPDATE` dentro del método `execute()`.

Supongamos que queremos actualizar el nombre del empleado cuyo Id es igual a 2 y que
insertamos en el ejemplo amnteror. **Importante** Tenemos que usaren la sentencia
un `WHERE` como condición para seleccionar a este empleado, si no, se
modificarían todos los empleados de la tabla.

Veamos el ejemplo:

    con = sqlite3.connect('ejemplo.db')
    cur = con.cursor()
    user_id = 2
    new_name = "Robert Millhouse"
    cur.execute("""
        UPDATE employee
           SET name = ?
         WHERE id = ?
        """, (new_name, user_id))
    con.commit()

### Hacer consultas

#### La Sentencia `SELECT`

La sentencia `SELECT` se usa para seleccionar datos de una tabla en particular.
Si deseas seleccionar todas las columnas de los datos de una tabla, puede usar
el asterisco (*). La sintaxis para esto seria la siguiente:


    SELECT * FROM <table_name>


En SQLite3, ejecutamos la instrucción `SELECT` usando el método `execute` del 
cursor. Por ejemplo para obtener todas las columnas de la tabla de empleados,
ejecutariamos el siguiente código:

    SELECT * FROM employee

Si deseas seleccionar algunas columnas de una tabla solamente, especifica las
columnas de la siguiente manera:

    SELECT <column1>[, <column2>] FROM <table_name>

Por ejemplo:

    SELECT id, name FROM employee


La sentencia select realiza la búsqueda de los datos requeridos desde la 
tabla de la base de datos y a continuación, para obtener los datos 
seleccionados, podemos utilizar el método `fetchall()` del cursor, que nos
devolvería todos los registros encontrador (En este caso, como no hay clausula
`WHERE`, todos). Veamos el siguiente eejmplo:

    con = sqlite3.connect('ejemplo.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM employee')
    rows = cur.fetchall()
    for row in rows:
        print(row)



Obtener todos los datos
También puede usar el fetchall () en una línea de la siguiente manera:

[print(row) for row in cursorObj.fetchall()]
Si deseas obtener datos específicos de la base de datos, puede utilizar la cláusula WHERE. Por ejemplo, queremos obtener los ids y los nombres de aquellos empleados cuyo salario es superior a 800. Para esto, llenemos nuestra tabla con más filas y luego ejecutemos nuestra consulta.

Populate table
Puede usar la sentencia insert para rellenar los datos o puede ingresarlos manualmente en el programa del navegador DB.

Ahora, para obtener los ids y los nombres de aquellos empleados que tienen un salario superior a 800:

import sqlite3

con = sqlite3.connect('mydatabase.db')

def sql_fetch(con):

    cursorObj = con.cursor()

    cursorObj.execute('SELECT id, name FROM employees WHERE salary > 800.0')

    rows = cursorObj.fetchall()

    for row in rows:

        print(row)

sql_fetch(con)
En la sentencia SELECT anterior, en lugar de usar el asterisco (*), especificamos los atributos id y name. El resultado se muestra a continuación:

Select where clause
 


SQLite3 rowcount
El SQLite3 rowcount se utiliza para devolver el número de filas afectadas o seleccionadas por la última consulta SQL ejecutada.

Cuando utilizamos el conteo de de filas con la sentencia SELECT, devolverá -1, ya que se desconoce la cantidad de filas seleccionadas hasta que se recuperan todas. Considera el siguiente ejemplo:

print(cursorObj.execute('SELECT * FROM employees').rowcount)
SQLite3 rowcount
Por lo tanto, para obtener el conteo de filas, debes obtener todos los datos y luego obtener la longitud del resultado:

rows = cursorObj.fetchall()

print len (rows)
Cuando la instrucción DELETE se utiliza sin ninguna condición (una sentencia WHERE), todas las filas de la tabla se eliminarán y el número total de filas eliminadas se devolverá por conteo de filas.

print(cursorObj.execute('DELETE FROM employees').rowcount)
Row count
Si no se borra ninguna fila, se devolverá 0.

Los registros no han sido borrados
Listar tablas
Para enumerar todas las tablas en una base de datos SQLite3, debes consultar la tabla sqlite_master y luego usar fetchall() para obtener los resultados de la sentencia SELECT.

El sqlite_master es la tabla maestra en SQLite3 que almacena todas las tablas.

import sqlite3

con = sqlite3.connect('mydatabase.db')

def sql_fetch(con):

    cursorObj = con.cursor()

    cursorObj.execute('SELECT name from sqlite_master where type= "table"')

    print(cursorObj.fetchall())

sql_fetch(con)
Con este código se listará todas las tablas de la siguiente manera:

List tables
 

Comprobar si una tabla existe o no
Al crear una tabla, debemos asegurarnos de que la tabla aún no exista. Del mismo modo, al remover / eliminar una tabla, la tabla debe existir.

Para verificar si la tabla no existe, usamos “if not exists” con la sentencia CREATE TABLE de la siguiente manera:

create table if not exists table_name (column1, column2, …, columnN)
Por ejemplo:

import sqlite3

con = sqlite3.connect('mydatabase.db')

def sql_fetch(con):

    cursorObj = con.cursor()

    cursorObj.execute('create table if not exists projects(id integer, name text)')

    con.commit()

sql_fetch(con)
Comprobar si una tabla existe o no
De manera similar, para verificar si la tabla existe al eliminar, usamos “if exists” con la sentencia DROP TABLE de la siguiente manera:

drop table if exists table_name
Por ejemplo,

cursorObj.execute('drop table if exists projects')
Tabla eliminada
También podemos verificar si la tabla a la que queremos acceder existe o no ejecutando la siguiente consulta:

cursorObj.execute('SELECT name from sqlite_master WHERE type = "table" AND name = "employees"')

print(cursorObj.fetchall())
Si existe la tabla de empleados, su nombre será devuelto como se muestra a continuación:

Tabla existe

Si el nombre de la tabla que especificamos no existe, se devolverá una arreglo vacío:

Tabla no existe
 


Eliminar una tabla
Puedes remover /eliminar una tabla utilizando la sentencia DROP. La sintaxis de la sentencia DROP es la siguiente:

drop table table_name
Para eliminar una tabla, la tabla debe existir en la base de datos. Por lo tanto, se recomienda utilizar “if exists” con la sentencia drop de la siguiente manera:

drop table if exists table_name
Por ejemplo,

import sqlite3

con = sqlite3.connect('mydatabase.db')

def sql_fetch(con):

    cursorObj = con.cursor()

    cursorObj.execute('DROP table if exists employees')

    con.commit()

sql_fetch(con)
Eliminar una tabla
Excepciones SQLite3
Las excepciones son errores de tiempo de ejecución. en la programación en Python, todas las excepciones son instancias de la clase derivadas de la BaseException.

En SQLite3, tenemos las siguientes excepciones principales de Python:

DatabaseError
Cualquier error relacionado con la base de datos genera el DatabaseError.

IntegrityError
IntegrityError es una subclase de DatabaseError y se genera cuando hay un problema de integridad de los datos, por ejemplo, los datos foráneos no se actualizan en todas las tablas, lo que resulta en una inconsistencia de los datos.

ProgrammingError
La excepción ProgrammingError se produce cuando hay errores de sintaxis o no se encuentra la tabla o se llama a la función con un número incorrecto de parámetros / argumentos.

OperationalError
Esta excepción se produce cuando fallan las operaciones de la base de datos, por ejemplo, una desconexión inusual. Esto no es culpa de los programadores.

NotSupportedError
Ocurre cuando utilizas algunos métodos que no están definidos o no son compatibles con la base de datos, se genera la excepción NotSupportedError.

 

SQLite3 Executemany (Inserción por lotes)
Puedes utilizar la sentencia Executemany para insertar varias filas a la vez.

Considera el siguiente código:

import sqlite3

con = sqlite3.connect('mydatabase.db')

cursorObj = con.cursor()

cursorObj.execute('create table if not exists projects(id integer, name text)')

data = [(1, "Ridesharing"), (2, "Water Purifying"), (3, "Forensics"), (4, "Botany")]

cursorObj.executemany("INSERT INTO projects VALUES(?, ?)", data)

con.commit()
Creamos una tabla con dos columnas, luego “data” tiene cuatro valores para cada columna. Esta variable se pasa al método executemany () junto con la consulta.

Ten en cuenta que hemos utilizado el ? para pasar los valores.

El código anterior generará el siguiente resultado:

Bulk insert (executemany)
 

Cerrar Conexión

Una vez que haya terminado de utilizar tu base de datos, es una buena práctica cerrar la conexión. La conexión se puede cerrar utilizando el método close ().

Para cerrar una conexión, utiliza el objeto de conexión y llame al método close () de la siguiente manera:

con = sqlite3.connect('mydatabase.db')

#program statements

con.close()
 

SQLite3 datetime
En la base de datos Python SQLite3, podemos almacenar fácilmente la fecha o la hora importando el módulo datatime. Los siguientes formatos son los formatos más utilizados para datetime:

YYYY-MM-DD

YYYY-MM-DD HH:MM

YYYY-MM-DD HH:MM:SS

YYYY-MM-DD HH:MM:SS.SSS

HH:MM

HH:MM:SS

HH:MM:SS.SSS

now
Observa el siguiente código:

import sqlite3

import datetime

con = sqlite3.connect('mydatabase.db')

cursorObj = con.cursor()

cursorObj.execute('create table if not exists assignments(id integer, name text, date date)')

data = [(1, "Ridesharing", datetime.date(2017, 1, 2)), (2, "Water Purifying", datetime.date(2018, 3, 4))]

cursorObj.executemany("INSERT INTO assignments VALUES(?, ?, ?)", data)

con.commit()
En este código, el módulo de fecha y hora se importa primero y hemos creado una tabla denominada assignments con tres columnas.

El tipo de datos de la tercera columna es una fecha. Para insertar la fecha en la columna, hemos usado datetime.date. De manera similar, podemos usar datetime.time para manejar la hora.

El código anterior generará la siguiente salida:

SQLite3 datetime
La gran flexibilidad y movilidad de la base de datos SQLite3 la convierten en la primera opción para que cualquier desarrollador la use y la integre con cualquier producto con el que trabaje.

Las bases de datos SQLite3 se utilizan en proyectos de Windows, Linux, Mac OS, Android e iOS debido a su increíble portabilidad. Es un archivo integrado con tu proyecto y listo.





