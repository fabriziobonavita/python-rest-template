from project_name.schemas import EntityBase


class Example(EntityBase):
    test: str

    class Config:
        orm_mode = True
