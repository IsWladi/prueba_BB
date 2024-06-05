-- DDL
CREATE TABLE evento (
    id INT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL
);

CREATE TABLE entradas (
    id INT PRIMARY KEY,
    id_evento INT,
    fecha_compra DATE,
    costo INT,
    FOREIGN KEY (id_evento) REFERENCES evento(id)
);

-- DML

-- Inserts para la tabla evento
INSERT INTO evento (id, nombre) VALUES (1, 'Concierto');
INSERT INTO evento (id, nombre) VALUES (2, 'Campeonato de futbol');
INSERT INTO evento (id, nombre) VALUES (3, 'Ballet');
INSERT INTO evento (id, nombre) VALUES (4, 'Fiesta');

-- Inserts para la tabla entradas
INSERT INTO entradas (id, id_evento, fecha_compra, costo) VALUES (1, 1, '2019-03-21', 20000);
INSERT INTO entradas (id, id_evento, fecha_compra, costo) VALUES (2, 1, '2019-03-22', 30000);
INSERT INTO entradas (id, id_evento, fecha_compra, costo) VALUES (3, 4, '2019-03-22', 6000);
INSERT INTO entradas (id, id_evento, fecha_compra, costo) VALUES (4, 4, '2019-03-23', 6000);
INSERT INTO entradas (id, id_evento, fecha_compra, costo) VALUES (5, 4, '2019-03-24', 6000);
INSERT INTO entradas (id, id_evento, fecha_compra, costo) VALUES (6, 1, '2019-03-25', 15000);
INSERT INTO entradas (id, id_evento, fecha_compra, costo) VALUES (7, 3, '2019-03-25', 8000);
