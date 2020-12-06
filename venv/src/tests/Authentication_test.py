import json

# учитывать версионость и не прописывать полный путь
import pytest

from helpers.CharactersHelper import CharactersHelper


@pytest.mark.usefixtures("api_session")
class TestCharacters(CharactersHelper):
    """
    Проверка получения актеров из БД и проверки корректной передачи данных
    prepare_two_characters: фикстура в которой подготавливает базу и возвращающая двух актеров.
    """

    def test_get_characters(self, prepare_two_characters):
        response = self.get_characters()
        result = self.get_result(response)

        # Так бы я написал при возможности подготовить базу к тесту и внести только два персонажа
        # assert len(result) == 10, "В result пришло меньше characters"

        assert self.check_character_in_result(result,
                                              prepare_two_characters[0]), "Некорректно передано длинное сообщение"
        assert self.check_character_in_result(result,
                                              prepare_two_characters[1]), "Некорректно передано короткое сообщение"

    """
    Проверка получения актера из БД и проверки корректной передачи данных
    prepare_two_characters: фикстура в которой подготавливает базу и возвращающая двух актеров.
    """

    @pytest.mark.parametrize("number_character", [1, 2])
    def test_get_character(self, prepare_two_characters, number_character):
        response = self.get_character(prepare_two_characters[number_character - 1].get("name"))
        result = self.get_result(response)

        assert type(result) is dict, 'Некорректный тип данных в result'

        assert result == prepare_two_characters[number_character - 1], \
            "Некорректно переданы данные для {}".format(prepare_two_characters[number_character - 1].get("name"))

    def test_create_character(self, deleted_character):
        response = self.post_character(deleted_character)
        result = self.get_result(response)

        assert result == deleted_character, "Результат в ответе на добавление character не соответствует отправленным " \
                                            "данным"

        assert self.check_character_in_bd(deleted_character)

    def test_update_character(self, prepared_character):
        prepared_character.update({"weight": 300})
        response = self.put_character(prepared_character)
        result = self.get_result(response)

        assert result == prepared_character, "Результат в ответе на обновление character не соответствует отправленным " \
                                             "данным"

        assert self.check_character_in_bd(prepared_character)

    # def test_delete_character(self, prepared_character):
    #     # prepared_character.update({"weight": 300})
    #     # response = self.put_character(prepared_character)
    #     # result = self.get_result(response)
    #     #
    #     # assert result == prepared_character, "Результат в ответе на обновление character не соответствует отправленным " \
    #     #                                      "данным"
    #     #
    #     # assert self.check_character_in_bd(prepared_character)
