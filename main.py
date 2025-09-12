from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None #(opcional quiere decir)
    price: float
    tax: float 

app = FastAPI()

@app.post('/api/v1/items/')
async def create_item(item: Item):
    return (f'El item {item.name} es: {item.description}, y tiene un impuesto de {item.tax}')


@app.get('/') #a la aplicación que acabamos de crear, definele un get. Path raíz, método 'get'.
async def hello_world():#programación asíncrona(mientras algo se está ejecutando, se puede ejecutar al mismo tiempo otra función), se define la función 
    return 'Hello World!'
# ya es un API con un sólo endpoint



@app.get('/api/v1/items/{item_id}')#parámetro de path
async def read_item(item_id: int):
    return {'item_id': item_id}


