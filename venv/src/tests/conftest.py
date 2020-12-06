import pytest
import requests

from helpers.ApiTests import SessionApi


@pytest.fixture()
def prepare_two_characters(two_characters):
    prepare_character(two_characters[0])
    prepare_character(two_characters[1])
    return two_characters


@pytest.fixture()
def deleted_character(character: dict):
    delete_character(character)
    return character


@pytest.fixture()
def prepared_character(character: dict):
    prepare_character(character)
    return character


@pytest.fixture()
def character():
    return {"name": "Hawkeye", "universe": "Marvel Universe",
            "education": "High school (unfinished)", "weight": 104,
            "height": 1.90, "identity": "Publicly known"}


@pytest.fixture()
def two_characters():
    character_original_long = {
        "education": "Unrevealed",
        "height": 170,
        "identity": "Secret (known to the U.S. government)",
        "name": "Avalanche",
        "other_aliases": "Jon Bloom",
        "universe": "Marvel Universe",
        "weight": 87.75
    }
    character_original_short = {
        "name": "Ben Parker",
        "other_aliases": "Ben, Uncle Ben, Unca' Ben"
    }
    return character_original_long, character_original_short

# В методе реализуеться подготовка данных через requests, но в реальном фреймворке предпологаеться доступ к базе данных
def delete_character(character: dict):
    name = character.get("name").replace(" ", "+")
    requests.delete("http://rest.test.ivi.ru/v2/character?name={}".format(name),
                    auth=('kce@yandex.ru', 'APZrVp83vFNk5F'))


# В методе реализуеться подготовка данных через requests, но в реальном фреймворке предпологаеться доступ к базе данных
def prepare_character(character: dict):
    name = character.get("name").replace(" ", "+")
    requests.delete("http://rest.test.ivi.ru/v2/character?name={}".format(name),
                    auth=('kce@yandex.ru', 'APZrVp83vFNk5F'))
    requests.post(
        "http://rest.test.ivi.ru/v2/character",
        headers={'Content-type': 'application/json'},
        json=character,
        auth=('kce@yandex.ru', 'APZrVp83vFNk5F')
    )
