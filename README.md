# Levantar entorno y hacer pruebas

<details>
<summary>Docker</summary>
</br>

## Requerimientos
- Docker instalado (con `docker-compose` o en versiones actuales con `docker compose`)

## Ejecutar tests unitarios de preguntas 1, 2 y 3
- En la raíz del repositorio ejecutar `docker build -t run-bb-tests .`
- Luego ejecutar `docker run -it --rm --name my-running-bb-tests run-bb-tests` para correr los tests.

## Levantar base de datos de prueba para pregunta 4
Nota: las tablas y los datos de ejemplo de la base de datos se crean automaticamente al levantar el contenedor.
- En la carpeta `pregunta4/` ejecutar `docker-compose up -d` o `docker compose up -d` para levantar la base de datos de prueba.
- Entrar al contenedor de la base de datos con `docker compose exec -it db bash` o `docker-compose exec -it db bash`
- Desde la terminal del contenedor conectarse a la base de datos con `psql -d bb_db_postgresql`
- Ejecutar la query en la terminal de la base de datos de la pregunta 4 que se encuentra en `pregunta4/cuarta_pregunta.sql`
</details>

<details>
<summary>Local</summary>
</br>

## Requerimientos
- Python v3.12.3
- PostgreSQL v16

## Ejecutar tests unitarios de preguntas 1, 2 y 3
- Instalar dependencias con `pip install -r requirements.txt`
- En la raíz del repositorio ejecutar `pytest -v`

## Probar pregunta 4
Nota: la consulta SQL la hice en PostgreSQL, por lo que no se garantiza que funcione en otros motores de base de datos.
- Crear tablas e insertar datos de ejemplo con el script `/pregunta4/docker-entrypoint-initdb.d/init-DDL-DML.sql`
- Copiar consulta SQL de `pregunta4/cuarta_pregunta.sql` y ejecutarla en la base de datos de prueba.
</details>
