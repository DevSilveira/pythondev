from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///database.db", echo=True)
Base = declarative_base()

class Movies(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    score = Column(Float, nullable=False)

Base.metadata.create_all(engine)

def add_movie(name, year, score):
    Session = sessionmaker(bind=engine)
    session = Session()
    movie = Movies(name=name, year=year, score=score)
    session.add(movie)
    session.commit()
    session.close()

# add_movie("Mario", 2022, 9.5)
# add_movie("Sonic", 2019, 8.5)

def update_movie(id, name=None, year=None, score=None):
    Session = sessionmaker(bind=engine)
    session = Session()
    movie = session.query(Movies).filter_by(id=id).first()
    if movie:
        if name is not None:
            movie.name = name
        if year is not None:
            movie.year = year
        if score is not None:
            movie.score = score
        session.commit()
    session.close()

# update_movie(1, "Homem Aranha", 2016, 9.0)

def remove_movie(id):
    Session = sessionmaker(bind=engine)
    session = Session()
    movie = session.query(Movies).filter_by(id=id).first()
    if movie:
        session.delete(movie)
    session.commit()
    session.close()

# remove_movie(2)
