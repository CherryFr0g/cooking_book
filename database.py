from typing import List

from sqlalchemy import String, create_engine, Integer, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

from settings import DATABASE_URL

engine = create_engine(DATABASE_URL)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    middle_name: Mapped[str] = mapped_column(String(50), nullable=True)


class Reciept(Base):
    __tablename__ = "receipts"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255))
    description: Mapped[str] = mapped_column(String(255), nullable=True)
    cooking_time: Mapped[int] = mapped_column(Integer, comment="Время готовки в минутах")
    photo: Mapped[str] = mapped_column(String(255), nullable=True)

    ingredients: Mapped[List["Ingredient"]] = relationship(back_populates="receipt")


class Ingredient(Base):
    __tablename__ = "ingredients"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255))
    amount: Mapped[str] = mapped_column(String(50))
    receipt_id: Mapped[int] = mapped_column(ForeignKey("receipts.id"))
    receipt: Mapped["Reciept"] = relationship(back_populates="ingredients")







