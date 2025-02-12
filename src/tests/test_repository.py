import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.tron.repository import TronRepository
from src.config.database.db_config import Base

SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="function")
def db():
    Base.metadata.create_all(bind=engine)
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()
        Base.metadata.drop_all(bind=engine)


def test_create_request(db):
    repository = TronRepository(db)
    address = "TXYZ"
    tron_request = repository.create_request(address)
    assert tron_request.id is not None
    assert tron_request.address == address
