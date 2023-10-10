from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class TipoUsuarioModel(Base):
    __tablename__ = 'tipo_usuario'
    id = Column(Integer, primary_key=True)
    nome = Column(String)