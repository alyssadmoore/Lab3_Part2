from sqlalchemy import Column, Integer, String
from base import Base


class Juggler(Base):
    __tablename__ = 'jugglers'

    name = Column(String, primary_key=True)
    country = Column(String)
    catches = Column(Integer)

    def __repr__(self):
        return 'Juggler: Name = {} Country = {} Catches = {}'.format(self.name, self.country, self.catches)