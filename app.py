from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="API de Productos",
    description="API simple para registrar y listar productos",
    version="1.0.0"
)

class Producto(BaseModel):
    nombre: str
    precio: float
    stock: int

productos = []

@app.get("/productos", status_code=200)
def listar_productos():
    return productos

@app.post("/productos", status_code=201)
def registrar_producto(producto: Producto):
    productos.append(producto)
    return {
        "mensaje": "Producto registrado correctamente",
        "producto": producto
    }
