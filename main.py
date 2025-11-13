from typing import Literal

from fastapi import FastAPI ,HTTPException
import uvicorn
from pydantic import BaseModel
import encrypt_decrypt

app = FastAPI()
class CaesarBudy(BaseModel):
    text: str
    offset:int
    mode : Literal["encrypt","decrypt"]

class Fence(BaseModel):
    text:str


@app.get("/test/")
def root():
    return {"msg":"hi from test"}

@app.get("/test/{name}")
def get_name(name):
    with open("name.txt","a",encoding="utf-8") as file:
        file.write(name)
    return { "msg": "saved user"}

@app.post("/caesar")
def caesar_cipher_endpoint(budy:CaesarBudy):
    if budy.mode == "encrypt":
        encrypted = encrypt_decrypt.encrypt_caesar(budy.text,budy.offset)
        return {"encrypted_text":f"{encrypted}"}
    elif budy.mode == "decrypt":
        decrypted = encrypt_decrypt.decrypt_caesar(budy.text,budy.offset)
        return {"encrypted_text":f"{decrypted}"}
    else:
        return None

@app.get("/fence/encrypt")
def fence_cipher_endpoints(text):
    response = encrypt_decrypt.cipher_fence_rail(text)
    return {"encrypted_text":f"{response}"}

@app.post("/fence/decrypt")
def fence_cipher_decrypt(text:Fence):
    response = encrypt_decrypt.decrypt_cipher_fence_rail(text)
    return {"decrypted": f"{response}" }



if __name__ == "__main__":
    uvicorn.run(app,host="localhost",port=8000)