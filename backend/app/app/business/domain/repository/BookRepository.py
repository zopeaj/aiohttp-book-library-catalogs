from sqlalchemy import Session
from fastapi import Depends


class BookRepository:
    def __init__(self):
        self.db: Session = Depends(get_db)
