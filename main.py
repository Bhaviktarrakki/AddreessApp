from fastapi import FastAPI
from routes.address import route
from config.database import meta, engine

app = FastAPI()
meta.create_all(engine)
app.include_router(route)
