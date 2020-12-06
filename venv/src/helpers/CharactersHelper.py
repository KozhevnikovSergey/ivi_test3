import json

from helpers.ApiTests import ApiTests


class CharactersHelper(ApiTests):
    POINT_CHARACTERS = '/characters'
    POINT_CHARACTER = '/character'

    def get_characters(self):
        return self.session_authorized.get(self.URL + self.POINT_CHARACTERS)

    def get_character(self, name: str):
        name = name.replace(' ', '+')
        return self.session_authorized.get(self.URL + self.POINT_CHARACTER + '?name=' + name)

    def post_character(self, data: dict):
        self.session_authorized.headers.update({"Content-type": "application/json"})
        return self.session_authorized.post(self.URL + self.POINT_CHARACTER, json=data,
                                            headers={"Content-type": "application/json"})

    def put_character(self, data: dict):
        self.session_authorized.headers.update({"Content-type": "application/json"})
        return self.session_authorized.put(self.URL + self.POINT_CHARACTER, json=data,
                                            headers={"Content-type": "application/json"})

    """
    Проверка информации о character оригинального с полученым
    """
    def check_character_in_result(self, result: list, character_original: dict) -> bool:
        for element in result:
            if element.get("name") == character_original.get("name"):
                if element == character_original:
                    return True
        raise Exception("Отсутствует character c именем {}".format(character_original.get("name")))

    """
    Проверка информации о character оригинального с полученым.
    result: спис 
    """
    # ПО ИДЕИ ТУТ ДОЛЖНЕН БЫТЬ РЕАЛИЗОВАН ДОСТУП К БАЗЕ ДАННЫХ, НО У МЕНЯ НЕТ К НЕМУ ДОСТУПА
    def check_character_in_bd(self, character: dict):
        response = self.get_character(character.get("name"))
        result = self.get_result(response)
        if character == result:
            return True
        return False
