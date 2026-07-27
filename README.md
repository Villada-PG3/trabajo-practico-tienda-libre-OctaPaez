# 🛒 Tienda Libre

Ecommerce didáctico desarrollado con **Django** como proyecto integrador de **Programación III** (6.° año, ITS Villada).

Este repositorio se construye **clase a clase** durante el ciclo lectivo, incorporando progresivamente los conceptos fundamentales del desarrollo web con Django: modelos y ORM, patrón MTV, vistas basadas en clases, formularios, autenticación y CRUD completo.

---

## Stack tecnológico

- **Python** 3.12+
- **Django** 5.x
- **SQLite** (base de datos de desarrollo)
- **Bootstrap 5** (via CDN)
- HTML5 / CSS3 / JavaScript

## Requisitos previos

- WSL2 con Ubuntu (Windows) o Linux/macOS
- `pyenv` o Python 3.12 o superior
- `git` configurado con clave SSH en GitHub
- Editor: VS Code recomendado (con extensión Remote — WSL si corresponde)

---

## Puesta en marcha

### 1. Cloná el repositorio

```bash
git clone git@github.com:tu-usuario/tienda-libre.git
cd tienda-libre
```

### 2. Creá y activá el entorno virtual

```bash
python -m venv .venv
source .venv/bin/activate
```

Al activarlo, el prompt debería mostrar `(.venv)` al inicio.

### 3. Instalá las dependencias

```bash
pip install -r requirements.txt
```

### 4. Aplicá las migraciones

```bash
python manage.py migrate
```

### 5. Creá un superusuario para el admin

```bash
python manage.py createsuperuser
```

### 6. Levantá el servidor de desarrollo

```bash
python manage.py runserver
```

- App: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/

---


## Convenciones de trabajo

### Git

- Al final de **cada clase** se hace commit descriptivo.
- Formato de mensajes: `tipo: descripción` — `feat`, `fix`, `refactor`, `docs`, `style`, `chore`.
- Ejemplos:
  - `feat: agregar modelo Categoria y ForeignKey en Producto`
  - `refactor: migrar CatalogoView de FBV a CBV`
  - `docs: agregar ejemplos de consultas ORM`
- Trabajo por rama por funcionalidad. `main` siempre estable.

### Qué NO se sube al repositorio

Estos elementos van en `.gitignore` y **no** deben commitearse:

- `.venv/` — entorno virtual
- `db.sqlite3` — base de datos local
- `media/` — archivos subidos por el usuario
- `__pycache__/` — bytecode de Python
- `.env` — variables de entorno con secretos

### Dependencias

Cuando se instala un paquete nuevo con `pip`, hay que regenerar `requirements.txt`:

```bash
pip freeze > requirements.txt
```

---

## Comandos útiles

```bash
# Crear una migración a partir de cambios en los modelos
python manage.py makemigrations

# Aplicar migraciones pendientes
python manage.py migrate

# Abrir el shell interactivo de Django
python manage.py shell

# Correr el servidor en otro puerto
python manage.py runserver 8080

# Crear una nueva app
python manage.py startapp <nombre>
```

---