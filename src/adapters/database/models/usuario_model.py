from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class UsuarioModel(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    senha = Column(String)
    cpf = Column(String)
    tipo_id = Column(Integer, ForeignKey('tipo_usuario.id'))
    tipo = relationship('TipoUsuarioModel')