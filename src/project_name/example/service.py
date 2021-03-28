from sqlalchemy.orm import Session

from project_name.example.models import Example


def get_example(db: Session) -> Example:
    return db.query(Example).first()
