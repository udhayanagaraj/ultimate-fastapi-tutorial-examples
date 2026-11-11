import logging


from app.db.init_db import init_db
from app.db.session import SessionLocal

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def init() -> None:
    logger.info("Initializing database data")
    with SessionLocal() as db:
        try:
            init_db(db)
            logger.info("Initial data created successfully")

        except Exception:
            db.rollback()
            logger.exception("Failed to create initial data")
            raise

def main():
    logger.info("Creating initial data")
    init()


if __name__ == "__main__":
    main()