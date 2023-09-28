import os
import uvicorn
import datetime
from fastapi import FastAPI
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Pereval

app = FastAPI()
load_dotenv()

base_dir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(base_dir, 'fstr.db')

# Создаем подключение к базе данных
engine = create_engine(f'sqlite:///{db_path}')

# Создаем сессию базы данных
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@app.get("/")
def hello():
    return 'Привет'


def create_pereval(db, pereval_data):
    add_time = datetime.datetime.fromisoformat(pereval_data['add_time'])
    pereval = Pereval(
        beautyTitle=pereval_data['beautyTitle'],
        title=pereval_data['title'],
        other_titles=pereval_data['other_titles'],
        connect=pereval_data['connect'],
        add_time=add_time,
        user_email=pereval_data['user_email'],
        coord_id=pereval_data['coord_id'],
        status=pereval_data['status']
    )
    db.add(pereval)
    db.commit()
    db.refresh(pereval)
    return pereval


@app.post("/submitData")
def submit_data(data: dict):
    db = SessionLocal()
    try:
        pereval_data = data.get('pereval')
        pereval = create_pereval(db, pereval_data)
        return {
            "status": 200,
            "message": "null",
            "id": pereval.id
        }
    finally:
        db.close()


if __name__ == "__main__":
    # Создание таблиц в базе данных
    # Base.metadata.create_all(engine)

    uvicorn.run(app, host="127.0.0.1", port=8000)