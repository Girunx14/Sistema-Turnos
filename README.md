# Sistema de Turnos — Backend

API REST construida con **FastAPI** y **SQLAlchemy** para gestionar un sistema de turnos de atención al público.

## Tecnologías

- Python 3.13
- FastAPI
- SQLAlchemy
- MariaDB / MySQL
- Uvicorn
- Pydantic
- python-dotenv

## Requisitos previos

- Python 3.10 o superior
- MariaDB o MySQL instalado y corriendo
- Base de datos `sistema_turnos` creada

## Instalación

```bash
# 1. Clona el repositorio
git clone https://github.com/tu-usuario/sistema-turnos-api.git
cd sistema-turnos-api

# 2. Crea y activa el entorno virtual
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate

# 3. Instala las dependencias
pip install -r requirements.txt
```

## Configuración

Crea un archivo `.env` en la raíz del proyecto con tus credenciales:

```env
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=tu_contraseña
DB_NAME=sistema_turnos
```

## Base de datos

Ejecuta el siguiente script SQL en MySQL Workbench para crear las tablas e insertar los datos base:

```sql
-- Datos base necesarios
INSERT INTO tipo_area (nombre) VALUES ('Caja'), ('Ejecutivo');
INSERT INTO area (nombre, fk_tipo_area) VALUES ('Caja 1', 1), ('Ejecutivo', 2);
INSERT INTO estatu (nombre) VALUES ('En espera'), ('Atendido'), ('Cancelado');
INSERT INTO genero (id, nombre) VALUES (1, 'Masculino'), (2, 'Femenino'), (3, 'Otro');

-- Usuarios
INSERT INTO usuario (username, password, nombre, apellido_paterno, fk_area)
VALUES ('cajero1', '1234', 'Juan', 'Pérez', 1);

INSERT INTO usuario (username, password, nombre, apellido_paterno, fk_area)
VALUES ('ejecutivo1', '1234', 'Carlos', 'García', 2);

INSERT INTO usuario (username, password, nombre, apellido_paterno, fk_area)
VALUES ('admin', 'admin123', 'Admin', 'Sistema', NULL);
```

## Ejecución

```bash
uvicorn app.main:app --reload
```

La API estará disponible en `http://127.0.0.1:8000`

## Documentación interactiva

Una vez corriendo, accede a la documentación automática en:

- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

## Endpoints principales

|Método|Ruta|Descripción|
|---|---|---|
|POST|`/auth/login`|Iniciar sesión|
|GET|`/turno/`|Listar todos los turnos|
|POST|`/turno/`|Crear nuevo turno|
|PUT|`/turno/{id}/atender`|Marcar turno como atendido + registrar género|
|PUT|`/turno/{id}/cancelar`|Cancelar turno|
|GET|`/area/`|Listar áreas|
|GET|`/genero/`|Listar géneros|
|GET|`/estatu/`|Listar estatus|

## Estructura del proyecto

```
app/
├── main.py           # Punto de entrada
├── database.py       # Conexión a la base de datos
├── models/           # Modelos SQLAlchemy (tablas)
├── schemas/          # Schemas Pydantic (validación)
└── routers/          # Endpoints por recurso
```

## Notas

- Las contraseñas actualmente se almacenan en texto plano. Para producción se recomienda implementar hashing con **bcrypt**.
- El folio se genera automáticamente con el prefijo del tipo de área + consecutivo diario (ej: `CA001`, `EJ001`).
- El género se registra al momento de **atender** el turno, no al generarlo.