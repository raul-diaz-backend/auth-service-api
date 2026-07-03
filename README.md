# 🔐 Auth Service API

Microservicio de autenticación desarrollado con FastAPI que permite gestionar usuarios, login seguro y protección de rutas mediante JWT.

---

## 🚀 Descripción

Este proyecto lo desarrollé con el objetivo de entender cómo funciona la autenticación en aplicaciones reales.

Incluye registro de usuarios, login con contraseñas encriptadas y generación de tokens JWT que permiten acceder a rutas protegidas.

También implementa OAuth2 para gestionar la autenticación de forma estándar.

---

## ⚙️ Funcionalidades

- Registro de usuarios
- Login con JWT
- Encriptación de contraseñas (Passlib)
- Protección de rutas con OAuth2
- Validación de tokens
- Base de datos con SQLAlchemy

---

## 🧠 Qué aprendí

- Cómo funciona el flujo completo de autenticación
- Generación y validación de JWT
- Seguridad en backend
- Uso de OAuth2 en FastAPI
- Estructuración de un microservicio

---

## 🛠️ Tecnologías

- Python
- FastAPI
- SQLAlchemy
- JWT (python-jose)
- Passlib
- SQLite

---

## ▶️ Cómo ejecutarlo

```bash
uvicorn app.main:app --reload
Ir a: http://127.0.0.1:8000/docs
