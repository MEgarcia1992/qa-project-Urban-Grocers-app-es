import requests
import data
import configuration



def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados


authtoken = post_new_user(data.dict_user_creation)
print(authtoken.json()["authToken"])
box_auth = authtoken.json()["authToken"]
bearer = "Bearer "
header_auth = bearer + box_auth

def conversion_of_header():
    kit_header = data.headers.copy()
    kit_header["Authorization"] = header_auth
    return kit_header

def test_kit_1char_on_name():
    case1 = requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,  # inserta la dirección URL completa
                         json=data.dict1_kit_1char_on_name,  # inserta el cuerpo de solicitud
                         headers= conversion_of_header())  # inserta los encabezados
    assert case1.status_code == 201
    assert case1.json()["name"] == data.dict1_kit_1char_on_name["name"]




def test_kit_511char_on_name():
    case2 = requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=data.dict2_kit_511char_on_name,
                         headers=conversion_of_header())
    assert case2.status_code == 201
    assert case2.json()["name"] == data.dict2_kit_511char_on_name["name"]



def test_kit_0char_on_name():
    case3 = requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=data.dict3_kit_0char_on_name,
                         headers=conversion_of_header())
    assert case3.status_code == 400



def test_kit_512char_on_name():
    case4 = requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=data.dict4_kit_512char_on_name,
                         headers=conversion_of_header())
    assert case4.status_code == 400



"""El siguiente caso tiene como cuerpo de la solicitud caracteres especiales que tienen que corregirse con el tema de las comillas ya que 
en los datos de la plataforma esta mal su sixtaxis y fue modificada ligeramente en el diccionario correspondiente en el archivo data.py"""
def test_kit_special_char_on_name():
    case5 = requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=data.dict5_kit_special_char_on_name,
                         headers=conversion_of_header())
    assert case5.status_code == 201
    assert case5.json()["name"] == data.dict5_kit_special_char_on_name["name"]



def test_kit_space_char_on_name():
    case6 = requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=data.dict6_kit_space_char_on_name,
                         headers=conversion_of_header())
    assert case6.status_code == 201
    assert case6.json()["name"] == data.dict6_kit_space_char_on_name["name"]



def test_kit_number_str_char_on_name():
    case7 = requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=data.dict7_kit_number_str_char_on_name,
                         headers=conversion_of_header())
    assert case7.status_code == 201
    assert case7.json()["name"] == data.dict7_kit_number_str_char_on_name["name"]



def test_kit_no_body_char_on_name():
    case8 = requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=data.dict8_kit_no_body_char_on_name,
                         headers=conversion_of_header())
    assert case8.status_code == 400



def test_kit_number_char_on_name():
    case9 = requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=data.dict9_kit_number_char_on_name,
                         headers=conversion_of_header())
    assert case9.status_code == 400



