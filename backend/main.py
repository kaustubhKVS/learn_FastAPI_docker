from fastapi import FastAPI

from typing import Union

from fastapi import FastAPI, Path, HTTPException, UploadFile
from fastapi import File

from .inference import get_fsm_prediction

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/api/get_prediction_from_file/")
async def post_image_pred_by_file(image_file: UploadFile = File(...)):

    print("########### PREDICTION IN PROGRESS  ##################", image_file.filename, "\n")
    
    image_file_content = await image_file.read()
    
    predicted_label = await get_fsm_prediction(image_file_content)

    print("########### PREDICTION SUCCESSFUL  ##################")
        
    return predicted_label
