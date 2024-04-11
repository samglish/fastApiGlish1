from fastapi import FastAPI
from pydantic import BaseModel
from api import generate_description
app=FastAPI()
class Product(BaseModel):
    name:str
    notes:str
#Pour comprendre fastApi une API qui renvoie hello, suivi du nom entré
@app.post("/Accueil")
async def hello_endpoint(name: str):
    return {"message":f"Hello, {name}!"}
#Pour aller plus loin Une API qui prend en entrée un produit et son nombre et renvoie : Order for {units} units of {product} place successfully
@app.post("/Detail")
async def place_holder(product:str, units:int):
    return {"message":f"Order for {units} units of {product} place successfully."}
#Enfin notre mini GPT
@app.post("/IA_samglish")
async def Openai(question:str) :
    reponse=generate_description(f"name:{question.name},notes:{question.notes} ")
    return {"reponse": reponse}