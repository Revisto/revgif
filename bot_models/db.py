
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Database:
        
    def __init__(self):
        self.base_path = "sqlite:///gifs.sqlite3"
        engine = sa.create_engine(self.base_path)
        Base.metadata.create_all(engine)
        session = sessionmaker(engine)
        self.session = session()

    class Gif(Base):
        __tablename__ = 'gif'
        id = sa.Column(sa.Integer, primary_key = True)
        gif_url = sa.Column(sa.Text)
        description = sa.Column(sa.Text)

    def add_gif_to_db(self, gif_url, description):
        new_gif = self.Gif(
            gif_url=gif_url,
            description=description
        )
        self.session.add(new_gif)
        self.session.commit()

    def get_all_gifs(self):
        return self.session.query(self.Gif)