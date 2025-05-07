from app.db.session import get_db

def get_db_session():
    return next(get_db())