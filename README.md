# Flask EC2 App 🚀

Esta es una aplicación web sencilla desarrollada con **Flask** que se conecta a una base de datos **MySQL**. Está diseñada para ser desplegada en instancias de **AWS EC2**.

## 📋 Características

- API REST básica con Flask.
- Conexión a base de datos MySQL.
- Endpoint `/` para verificar el estado de la aplicación.
- Endpoint `/datos` para consultar registros de la base de datos.
- Configuración mediante variables de entorno.

## 🛠️ Tecnologías

- **Python 3**
- **Flask**: Micro-framework web.
- **MySQL Connector**: Driver para la base de datos.
- **Gunicorn**: Servidor WSGI para producción.
- **python-dotenv**: Gestión de variables de entorno.

## 🚀 Instalación y Configuración Local

1.  **Clonar el repositorio:**
    ```bash
    git clone <url-del-repositorio>
    cd mi-app
    ```

2.  **Crear y activar un entorno virtual:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configurar variables de entorno:**
    Crea un archivo `.env` en la raíz del proyecto con los siguientes datos:
    ```env
    DB_HOST=tu_host_mysql
    DB_USER=app_user
    DB_PASS=tu_password
    DB_NAME=app_db
    ```

5.  **Ejecutar la aplicación:**
    ```bash
    python app.py
    ```
    La app estará disponible en `http://localhost:5000`.

## 🌐 Despliegue en EC2

Para producción, se recomienda usar **Gunicorn**:

```bash
gunicorn --bind 0.0.0.0:5000 app:app
```

## 🛣️ Endpoints

- `GET /`: Retorna un mensaje de bienvenida y estado "ok".
- `GET /datos`: Retorna los primeros 10 registros de la tabla `registros` en formato JSON.