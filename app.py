from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import torch

app = FastAPI()

# Load the best model
model = torch.load('best_model.pth')
model.eval()

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image = await file.read()
    # Preprocess image and run prediction
    result = model(torch.tensor(image))
    # Return result as JSON response
    return JSONResponse({"prediction": result.tolist()})
