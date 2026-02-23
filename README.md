# 🚀 Backend ADSO - API (Django + Firebase)

Este es el repositorio central para el desarrollo de la API del programa **ADSO**. El proyecto utiliza **Django** como framework robusto para el backend y **Firebase** para la gestión de datos en tiempo real y autenticación.

---

## 🏗️ Stack Tecnológico

* **Lenguaje:** [Python 3.12+](https://www.python.org/)
* **Framework:** [Django 5.x](https://www.djangoproject.com/)
* **API Toolkit:** [Django REST Framework (DRF)](https://www.django-rest-framework.org/)
* **Base de Datos / Auth:** [Firebase Admin SDK](https://firebase.google.com/)
* **Entorno:** `venv` (Virtual Environment)

---

## 🚧 Estado del Proyecto: `PENDIENTE / INCOMPLETO`

> [!WARNING]
> **Aviso:** El proyecto se encuentra en fase de planeación inicial. No existe código funcional en la rama principal todavía. Este documento sirve como guía para la configuración del entorno por parte de los desarrolladores.

---

## ⚙️ Configuración del Entorno e Instalación

Para preparar el entorno de desarrollo una vez se inicie el repositorio, sigue estos comandos en tu terminal:

### 1. Clonar y Entorno Virtual
```bash
# Clonar el repositorio
git clone [https://github.com/tu-usuario/nombre-del-repo.git](https://github.com/tu-usuario/nombre-del-repo.git)

# Acceder a la carpeta raíz
cd backend

# Crear entorno virtual
python -m venv venv

# Activar entorno (Windows)
.\venv\Scripts\activate

# Activar entorno (Linux/Mac)
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

```

### 2. 📁 Estructura del Proyecto

```
/ (Raíz del Repositorio)
├── venv/                      # Entorno virtual de Python (Excluido de Git)
├── manage.py                  # Script de gestión de Django
├── requirements.txt           # Listado de dependencias
├── .gitignore                 # Archivos excluidos del control de versiones
│
├── backend/                   # Directorio de Configuración (Core)
│   ├── .env                   # Variables de entorno (SECRET_KEY, etc.)
│   ├── settings.py            # Configuración global de Django
│   ├── urls.py                # Enrutador principal del proyecto
│   ├── firebase_config.py     # Lógica de conexión a Firebase
│   └── serviceAccountKey.json # Credenciales privadas de Firebase
│
└── api-tareas/                # Aplicación de Gestión de Tareas
    ├── admin.py
    ├── apps.py
    ├── models.py              # Modelos de datos
    ├── serializers.py         # Serializadores para la API
    ├── urls.py                # Rutas locales de la API
    └── views.py               # Lógica de los Endpoints
```

### 3. .gitignore
```
# Entorno Virtual
venv/

# Secretos y Credenciales
backend/.env
backend/serviceAccountKey.json

# Python
__pycache__/
*.py[cod]

# DB local (si se usa)
db.sqlite3
```