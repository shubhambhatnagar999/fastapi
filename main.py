from fastapi import FastAPI
from core.router_register import include_routers

# Create app instance
app = FastAPI()


# include routers
include_routers(app)

# Root route
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI is running 🚀"}

