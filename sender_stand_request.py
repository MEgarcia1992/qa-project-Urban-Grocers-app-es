import data
import requests
import configuration

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados


authtoken = post_new_user(data.dict_user_creation)
box_auth = authtoken.json()["authToken"]


def conversion_of_header():
    bearer = "Bearer "
    header_auth = bearer + box_auth
    kit_header = data.headers.copy()
    kit_header["Authorization"] = header_auth
    return kit_header

def positive_assert_user_kit_request(dict):
    case = requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                  json=dict,
                  headers=conversion_of_header())
    assert case.status_code == 201
    assert case.json()["name"] == dict["name"]

def negative_assert_user_kit_request(dict):
    case = requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=dict,
                         headers=conversion_of_header())
    assert case.status_code == 400