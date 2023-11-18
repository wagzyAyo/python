#!/usr/bin/python3
"""
This module contain City class that inherits
from Base imported from model_state
"""
from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False,
                      ForeignKey=State.id)
