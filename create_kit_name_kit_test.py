import data
import sender_stand_request



def test_kit_1char_on_name():
    sender_stand_request.positive_assert_user_kit_request(data.dict1_kit_1char_on_name)




def test_kit_511char_on_name():
    sender_stand_request.positive_assert_user_kit_request(data.dict2_kit_511char_on_name)



def test_kit_0char_on_name():
    sender_stand_request.negative_assert_user_kit_request(data.dict3_kit_0char_on_name)



def test_kit_512char_on_name():
    sender_stand_request.negative_assert_user_kit_request(data.dict4_kit_512char_on_name)



"""El siguiente caso tiene como cuerpo de la solicitud caracteres especiales que tienen que corregirse con el tema de las comillas ya que
#en los datos de la plataforma esta mal su sixtaxis y fue modificada ligeramente en el diccionario correspondiente en el archivo data.py"""
def test_kit_special_char_on_name():
    sender_stand_request.positive_assert_user_kit_request(data.dict5_kit_special_char_on_name)



def test_kit_space_char_on_name():
    sender_stand_request.positive_assert_user_kit_request(data.dict6_kit_space_char_on_name)



def test_kit_number_str_char_on_name():
    sender_stand_request.positive_assert_user_kit_request(data.dict7_kit_number_str_char_on_name)



def test_kit_no_body_char_on_name():
    sender_stand_request.negative_assert_user_kit_request(data.dict8_kit_no_body_char_on_name)



def test_kit_number_char_on_name():
    sender_stand_request.negative_assert_user_kit_request(data.dict9_kit_number_char_on_name)

