# comments are fo rgit execution
# commen
# codeo
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
# from ml_utils import load_model, predict

app = FastAPI(
    title="Iris Predictor",
    docs_url="/"
)
