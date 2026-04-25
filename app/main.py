from typing import Optional

from fastapi import FastAPI, Header, HTTPException

from app.auth.jwt_handler import create_access_token, verify_token
from app.auth.security import get_password_hash, verify_password
from app.database.database import Base, SessionLocal, engine
from app.models.user import User
from app.schemas.user_schema import UserCreate, UserLogin

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Auth Service API")


@app.get("/")
def read_root():
    return {"message": "Auth Service API running"}


@app.post("/register")
def register(user: UserCreate):
    db = SessionLocal()

    existing_user = db.query(User).filter(User.email == str(user.email)).first()

    if existing_user:
        db.close()
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = get_password_hash(user.password)

    new_user = User(
        email=str(user.email),
        hashed_password=hashed_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    db.close()

    return {"message": "User created successfully"}


@app.post("/login")
def login(user: UserLogin):
    db = SessionLocal()

    db_user = db.query(User).filter(User.email == str(user.email)).first()

    if not db_user:
        db.close()
        raise HTTPException(status_code=404, detail="User not found")

    if not verify_password(user.password, db_user.hashed_password):
        db.close()
        raise HTTPException(status_code=401, detail="Invalid password")

    access_token = create_access_token(data={"sub": db_user.email})

    db.close()

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


@app.get("/me")
def get_current_user(authorization: Optional[str] = Header(None, alias="Authorization")):
    if not authorization:
        raise HTTPException(status_code=401, detail="Token missing")

    token = authorization.replace("Bearer ", "")

    email = verify_token(token)

    if not email:
        raise HTTPException(status_code=401, detail="Invalid token")

    db = SessionLocal()

    user = db.query(User).filter(User.email == email).first()

    db.close()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return {
        "email": user.email
    }