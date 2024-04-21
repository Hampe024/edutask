import pytest
import pymongo
import os
from pymongo.errors import WriteError
from src.util.dao import DAO
from dotenv import dotenv_values


class TestDAO:
    @pytest.fixture
    def sut(self):
        yield DAO(collection_name="test_assignment_3")

        LOCAL_MONGO_URL = dotenv_values('.env').get('MONGO_URL')
        MONGO_URL = os.environ.get('MONGO_URL', LOCAL_MONGO_URL)
        client = pymongo.MongoClient(MONGO_URL)
        client.edutask.test_assignment_3.drop()

    @pytest.mark.unit
    def test_create_valid_data(self, sut):
        return_data = sut.create({
            "name": "john doe",
            "gender": "male",
            "email": "test@email.com",
            "bool": True
        })
        assert return_data["name"] == "john doe"

    @pytest.mark.unit
    def test_create_missing_required_properties(self, sut):
        with pytest.raises(WriteError):
            sut.create({
                "name": "john doe",
                "gender": "male",
                "email": "test@email.com"
            })

    @pytest.mark.unit
    def test_create_not_bosn_constricting(self, sut):
        with pytest.raises(WriteError):
            sut.create({
                "name": "john doe",
                "gender": False,
                "email": "test@email.com",
                "bool": True
            })

    @pytest.mark.unit
    def test_create_not_unique(self, sut):
        sut.create({
            "name": "john doe",
            "gender": "male",
            "email": "test@email.com",
            "bool": True
        })
        with pytest.raises(WriteError):
            sut.create({
                "name": "totally not john doe",
                "gender": "male",
                "email": "test@email.com",
                "bool": True
            })