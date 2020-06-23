from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

app: FastAPI = FastAPI()

# enable CORS
origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
