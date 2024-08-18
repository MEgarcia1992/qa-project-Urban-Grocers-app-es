

headers = {"Content-Type": "application/json"}



dict_user_creation = {
    "firstName": "Max",
    "email": "max@example.com",
    "phone": "+10005553535",
    "comment": "Cuidado con el perro",
    "address": "8042 Lancaster Ave.Hamburg, NY"
}

dict1_kit_1char_on_name = {"name": "a"}
dict2_kit_511char_on_name = {"name":"Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc\
dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda\
bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc\
dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab\
cdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab\
cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc\
dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda\
bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"}
dict3_kit_0char_on_name = {"name": ""}
dict4_kit_512char_on_name = {"name":"Abcdabcdabcdabcdabcdabcdabcdabcda\
bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc\
dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab\
cdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab\
cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc\
dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"}
dict5_kit_special_char_on_name = {"name": "№%@,"}
dict6_kit_space_char_on_name = {"name": " A Aaa "}
dict7_kit_number_str_char_on_name = {"name": "123"}
dict8_kit_no_body_char_on_name = {}
dict9_kit_number_char_on_name = {"name": 123}
