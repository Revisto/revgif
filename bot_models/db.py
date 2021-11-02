
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
        gif_path = sa.Column(sa.Text)
        description = sa.Column(sa.Text)

    def add_gif_to_db(self, gif_path, description):
        new_gif = self.Gif(
            gif_path=gif_path,
            description=description
        )
        self.session.add(new_gif)
        self.session.commit()

    def update_gif(self, gif_path, description):
        matched_gif = self.session.query(self.Gif).filter(self.Gif.gif_path == gif_path).first()
        new_description = " ".join(set((f"{matched_gif.description} {description}").split(" ")))
        matched_gif.description = new_description
        self.session.commit()

    def get_all_gifs(self):
        return self.session.query(self.Gif)