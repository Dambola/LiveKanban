from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from livekanban.db import Base

class Board(Base):
    __tablename__ = 'boards'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    states = relationship('State', backref='board')
    
    def as_json(self):
        return {
            'id': self.id,
            'name': self.name
        }