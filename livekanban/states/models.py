from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from livekanban.db import Base

class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    order = Column(Integer, nullable=False)
    board_id = Column(Integer, ForeignKey('boards.id'))
    