from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ⚠️ depois podemos restringir para segurança
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelo de entrada para login
class LoginInput(BaseModel):
    email: str
    password: str

# Simula um banco de dados fake
fake_users_db = {
    "carlos@aiflow.com": {
        "password": "senha123"
    }
}

@app.post("/auth/login")
def login(credentials: LoginInput):
    email = credentials.email
    password = credentials.password

    user = fake_users_db.get(email)
    if not user or user["password"] != password:
        raise HTTPException(status_code=400, detail="Usuário ou senha inválidos")

    return {
        "access_token": "fake-jwt-token",
        "token_type": "bearer"
    }

@app.get("/")
def root():
    return {"message": "API do AI Flow Backend funcionando"}
