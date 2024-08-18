from aiogram.types import User as TGUser
from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import BIGINT, VARCHAR
from sqlmodel import SQLModel, Field


class User(SQLModel, table=True):
    id: int | None = Field(sa_column=Column(BIGINT, primary_key=True, autoincrement=False, index=True))
    description: str | None = Field(sa_column=Column(VARCHAR))

    @classmethod
    def from_aiogram_user(cls, user: TGUser) -> TGUser:
        return User(id=user.id)
