# Levantar entorno y probar con Docker

## Requerimientos
- Docker instalado (con `docker-compose` o en versiones actuales con `docker compose`)

## Ejecutar tests unitarios de preguntas 1, 2 y 3
- En la raíz del repositorio ejecutar `docker build -t run-bb-tests .`
- Luego ejecutar `docker run -it --rm --name my-running-bb-tests run-bb-tests` para correr los tests.

## Levantar base de datos de prueba para pregunta 4
Nota: las tablas y los datos de ejemplo de la base de datos se crean automaticamente al levantar el contenedor.
- En la carpeta `pregunta4/` ejecutar `docker-compose up -d` o `docker compose up -d` para levantar la base de datos de prueba.
- Entrar al contenedor de la base de datos con `docker compose exec -it db bash`
- Conectarse a la base de datos con `psql -d bb_db_postgresql`
- Ejecutar la query de la pregunta 4 que se encuentra en `pregunta4/cuarta_pregunta.sql`

