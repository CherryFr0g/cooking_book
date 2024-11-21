import re

from pydantic import BaseModel, Field, ValidationError, field_validator, constr

name_regex = r"^[A-Za-zА-Яа-я\s'-]+$"


class UserModel(BaseModel):
    id: int | None = Field(None, gt=0)
    first_name: constr(pattern=name_regex) = Field(..., min_length=1)
    last_name: constr(pattern=name_regex) = Field(..., min_length=1)
    middle_name: str | None = Field(None)

    @classmethod
    @field_validator("middle_name")
    def validate_middle_name(cls, value):
        if value is None:
            return None

        if not isinstance(value, str):
            raise ValueError("Поле отчество должно быть строкой")

        if len(value) == 0:
            return None

        if not re.match(name_regex, value):
            raise ValidationError()

        return value


class LoginModel(BaseModel):
    id: int = Field(gt=0)


