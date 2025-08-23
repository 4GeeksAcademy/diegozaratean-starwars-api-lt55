from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "esta_vivo": self.is_active,
            # do not serialize the password, its a security breach
        }


class Empresa(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(120), nullable=False)
    slogan: Mapped[str] = mapped_column(nullable=False)
    ciudad: Mapped[str] = mapped_column(nullable=False)

    videojuegos: Mapped[List["Videojuego"]] = relationship(back_populates="empresa")

    def __repr__(self):
        return f'<Empresa  {self.id } - {self.nombre } >' 


    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "ciudad": self.ciudad,
            # "games": self.videojuegos
            # do not serialize the password, its a security breach
        }


class Videojuego(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(120), nullable=False)
    year: Mapped[int] = mapped_column(nullable=False)
  
    empresa_id: Mapped[int] = mapped_column(ForeignKey("empresa.id"))
    empresa: Mapped["Empresa"] = relationship(back_populates="videojuegos")

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "empresa": self.empresa.serialize()
        }
