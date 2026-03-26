create database sistema_turnos;
use sistema_turnos;

CREATE TABLE tipo_area (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL
);

CREATE TABLE area (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    fk_tipo_area INT NOT NULL,
    CONSTRAINT fk_area_tipo
        FOREIGN KEY (fk_tipo_area)
        REFERENCES tipo_area(id)
);

CREATE TABLE estatu (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(30) NOT NULL
);

CREATE TABLE genero (
    id INT PRIMARY KEY,
    nombre VARCHAR(30) NOT NULL
);

CREATE TABLE usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL,
    nombre VARCHAR(50) NOT NULL,
    apellido_paterno VARCHAR(50),
    apellido_materno VARCHAR(50)
);


CREATE TABLE turno (
    id INT AUTO_INCREMENT PRIMARY KEY,
    folio VARCHAR(10) NOT NULL,
    fecha_hora DATETIME NOT NULL,
    fecha_hora_atendida DATETIME,
    fk_usuario INT,
    fk_area_asignada INT,
    fk_estatu INT NOT NULL,
    fk_genero INT,
    CONSTRAINT fk_turno_usuario
        FOREIGN KEY (fk_usuario) REFERENCES usuario(id),
    CONSTRAINT fk_turno_area
        FOREIGN KEY (fk_area_asignada) REFERENCES area(id),
    CONSTRAINT fk_turno_estatu
        FOREIGN KEY (fk_estatu) REFERENCES estatu(id),
    CONSTRAINT fk_turno_genero
        FOREIGN KEY (fk_genero) REFERENCES genero(id)
);

CREATE TABLE contador (
    id INT AUTO_INCREMENT PRIMARY KEY,
    consecutivo INT NOT NULL,
    fecha DATE NOT NULL,
    fk_tipo_area INT NOT NULL,
    CONSTRAINT fk_contador_tipo_area
        FOREIGN KEY (fk_tipo_area) REFERENCES tipo_area(id)
);

INSERT INTO estatu (nombre) VALUES ('En espera'), ('Atendido'), ('Cancelado');
INSERT INTO genero (id, nombre) VALUES (1, 'Masculino'), (2, 'Femenino'), (3, 'Otro');
INSERT INTO tipo_area (nombre) VALUES ('Caja'), ('Servicio');
INSERT INTO area (nombre, fk_tipo_area) VALUES ('Caja 1', 1), ('Servicio General', 2);

ALTER TABLE usuario 
ADD COLUMN fk_area INT,
ADD CONSTRAINT fk_usuario_area 
    FOREIGN KEY (fk_area) REFERENCES area(id);
    
SELECT * FROM tipo_area;
SELECT * FROM area;
SELECT * FROM estatu;
SELECT * FROM genero;
SELECT * FROM usuario;

-- Primero asegúrate de tener un área creada, luego:
INSERT INTO usuario (username, password, nombre, apellido_paterno, fk_area)
VALUES ('cajero1', '1234', 'Juan', 'Pérez', 1);

INSERT INTO usuario (username, password, nombre, apellido_paterno, fk_area)
VALUES ('admin', 'admin123', 'Admin', 'Sistema', NULL);

UPDATE area SET nombre = 'Ejecutivo' WHERE id = 2;
SELECT * FROM area;

SELECT * FROM area;
SELECT * FROM usuario;

SELECT u.*, a.nombre as area_nombre 
FROM usuario u 
LEFT JOIN area a ON u.fk_area = a.id;

INSERT INTO usuario (username, password, nombre, apellido_paterno, fk_area)
VALUES ('ejecutivo1', '1234', 'Carlos', 'García', 2);

select * from tipo_area;
select * from estatu;
select * from genero; 