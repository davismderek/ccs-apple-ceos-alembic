from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from db import session
# from models import CEO, CEOSchema
# from models import Base
from models.Base import Base
from models.CEO import CEO, CEOSchema


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173",

]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def home():
    return {"message": "Root Route"}

@app.get("/CEOs")
def get_ceo():
    ceo = session.query(CEO)
    return ceo.all()

@app.post('/CEOs/Add')
async def create_ceo(ceo_data: CEOSchema):
    ceo = CEO(name=ceo_data.name, slug=ceo_data.slug, year_served=ceo_data.year_served)
    session.add(ceo)
    session.commit()
    return {"CEO added": ceo.name}
     


def create_tables():
	Base.metadata.create_all(session)
     