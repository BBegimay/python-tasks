from Module19.petstore.api import PetFriends
from Module19.petstore.settings import valid_email, valid_password
import os

pf = PetFriends()


def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    """ Проверяем что запрос api ключа возвращает статус 200 и в тезультате содержится слово key"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert 'key' in result


def test_get_api_key_for_invalid_user(email=None, password=valid_password):
    """ Проверяем что запрос api ключа возвращает статус 403 если не задать пользователя"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403
    assert 'key' not in result


def test_get_api_key_for_invalid_password(email=valid_email, password="Wrong password"):
    """ Проверяем что запрос api ключа возвращает статус 403 если не задать неверный пароль"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403
    assert 'key' not in result


def test_get_all_pets_with_valid_key(filter=''):
    """ Проверяем что запрос всех питомцев возвращает не пустой список.
    Для этого сначала получаем api ключ и сохраняем в переменную auth_key. Далее используя этого ключ
    запрашиваем список всех питомцев и проверяем что список не пустой.
    Доступное значение параметра filter - 'my_pets' либо '' """

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)

    assert status == 200
    assert len(result['pets']) > 0


def test_get_all_pets_with_invalid_key(filter=''):
    """ Проверяем что запрос всех питомцев возвращает 403 ошибку."""

    status, result = pf.get_list_of_pets({"key": "wrong"}, filter)

    assert status == 403


def test_get_all_pets_with_invalid_filter(filter='Wrong filter'):
    """ Проверяем что запрос всех питомцев возвращает 500 ошибку при неверном фильтре."""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)

    assert status == 500


def test_add_new_pet_with_valid_data(name='Барбоскин', animal_type='двортерьер',
                                     age='4', pet_photo='images/cat1.jpg'):
    """Проверяем что можно добавить питомца с корректными данными"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_add_new_pet_with_invalid_key(name='Барбоскин', animal_type='двортерьер',
                                     age='4', pet_photo='images/cat1.jpg'):
    """Проверяем что можно добавить питомца с некорекным ключем"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Добавляем питомца
    status, result = pf.add_new_pet({"key": "wrong"}, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 403


def test_add_new_pet_with_invalid_photo(name='Барбоскин', animal_type='двортерьер',
                                     age='4', pet_photo='images/cat1000.jpg'):
    """Проверяем что возникнет ошибка если задать неверное имя фото для питомца"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    try:
        # Добавляем питомца
        pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

        # Тест не должен дойти до этого момента
        assert False
    except FileNotFoundError:
        assert True


def test_successful_delete_self_pet():
    """Проверяем возможность удаления питомца"""

    # Получаем ключ auth_key и запрашиваем список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем - если список своих питомцев пустой, то добавляем нового и опять запрашиваем список своих питомцев
    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "Суперкот", "кот", "3", "images/cat1.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Берём id первого питомца из списка и отправляем запрос на удаление
    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)

    # Ещё раз запрашиваем список своих питомцев
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем что статус ответа равен 200 и в списке питомцев нет id удалённого питомца
    assert status == 200
    assert pet_id not in my_pets.values()


def test_unsuccessful_delete_self_pet_with_invalid_key():
    """Проверяем ошибку возможности удаления питомца если задать неверный ключ"""

    # Получаем ключ auth_key и запрашиваем список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем - если список своих питомцев пустой, то добавляем нового и опять запрашиваем список своих питомцев
    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "Суперкот", "кот", "3", "images/cat1.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Берём id первого питомца из списка и отправляем запрос на удаление
    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet({"key": "wrong"}, pet_id)

    # Проверяем что статус ответа равен 403
    assert status == 403


def test_unsuccessful_delete_self_pet_with_invalid_pet_id():
    """Проверяем ошибку возможности удаления питомца если задать неверный id"""

    # Получаем ключ auth_key и запрашиваем список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Берём id первого питомца из списка и отправляем запрос на удаление
    pet_id = "some random id"
    status, _ = pf.delete_pet(auth_key, pet_id)

    # Ещё раз запрашиваем список своих питомцев
    _, my_pets2 = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем что статус ответа равен 200 и список своих питомцев не поменялся
    assert status == 200
    assert len(my_pets) == len(my_pets2)


def test_successful_update_self_pet_info(name='Мурзик', animal_type='Котэ', age=5):
    """Проверяем возможность обновления информации о питомце"""

    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Если список не пустой, то пробуем обновить его имя, тип и возраст
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        # Проверяем что статус ответа = 200 и имя питомца соответствует заданному
        assert status == 200
        assert result['name'] == name
    else:
        # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")


def test_unsuccessful_update_self_pet_info_with_invalid_key(name='Мурзик', animal_type='Котэ', age=5):
    """Проверяем ошибку при обновлении информации о питомце с неверным ключем"""

    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    pet_id = 0
    # Если список не пустой, то пробуем обновить его имя, тип и возраст
    if len(my_pets['pets']) > 0:
        pet_id = my_pets['pets'][0]['id']
    else:
        # если спиок питомцев пустой, то создаем питомца
        status, result = pf.add_new_pet_simple(auth_key, 'Барбоскин', 'двортерьер', '4')
        pet_id = result['id']

    status, result = pf.update_pet_info({"key": "wrong"}, pet_id, name, animal_type, age)

    # Проверяем что статус ответа = 403
    assert status == 403


def test_unsuccessful_update_self_pet_info_with_invalid_id(name='Мурзик', animal_type='Котэ', age=5):
    """Проверяем ошибку при обновлении информации о питомце с неверным id"""

    # Получаем ключ auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.update_pet_info(auth_key, "wrong id", name, animal_type, age)

    # Проверяем что статус ответа = 400
    assert status == 400


def test_add_new_simple_pet_with_valid_data(name='Барбоскин', animal_type='двортерьер', age='4'):
    """Проверяем что можно добавить питомца в упрощенном виде с корректными данными"""

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet_simple(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_add_new_simple_pet_with_invalid_key(name='Барбоскин', animal_type='двортерьер', age='4'):
    """Проверяем ошибку при добавлении питомца в упрощенном виде с некорректным ключем"""

    # Добавляем питомца
    status, result = pf.add_new_pet_simple({"key": "wrong"}, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 403


def test_set_pet_photo_with_valid_data(pet_id=None, pet_photo='images/cat1.jpg'):
    """Проверяем что можно задать фото питомца с корректными данными"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Если pet_id не задан, создаем нового питомца без фото
    if pet_id is None:
        status, result = pf.add_new_pet_simple(auth_key, 'Барбоскин', 'двортерьер', '4')
        pet_id = result['id']

    # Добавляем фото
    status, result = pf.set_pets_photo(auth_key, pet_id, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200


def test_set_pet_photo_with_invalid_key(pet_id=None, pet_photo='images/cat1.jpg'):
    """Проверяем что можно задать фото питомца с некорректным ключем"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Если pet_id не задан, создаем нового питомца без фото
    if pet_id is None:
        status, result = pf.add_new_pet_simple(auth_key, 'Барбоскин', 'двортерьер', '4')
        pet_id = result['id']

    # Добавляем фото
    status, result = pf.set_pets_photo({"key": "wrong"}, pet_id, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 403


def test_set_pet_photo_with_invalid_photo(pet_id=None, pet_photo='images/cat100000.jpg'):
    """Проверяем что можно задать фото питомца с некорректными данными"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Если pet_id не задан, создаем нового питомца без фото
    if pet_id is None:
        status, result = pf.add_new_pet_simple(auth_key, 'Барбоскин', 'двортерьер', '4')
        pet_id = result['id']

    try:
        # Добавляем фото
        pf.set_pets_photo(auth_key, pet_id, pet_photo)

        # Тест не должен дойти до этого момента
        assert False
    except FileNotFoundError:
        assert True

