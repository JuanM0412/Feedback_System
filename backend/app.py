import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.modules.auth.routes import router as auth_router
from src.core.database import engine
from src.models.user import User

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)


@app.get("/")
def read_root():
    return {"message": "Feedback System API"}

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)