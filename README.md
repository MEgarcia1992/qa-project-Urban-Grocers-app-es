# Proyecto Urban Grocers 

# Miguel Eduardo Garcia Lopez 13vo Cohort, 7mo Sprint
El siguiente proyecto aborda pruebas de API especificamente para crear kits a partir de usuarios creados en la aplicacion 
Urban Grocers.

# Tecnologias Utilizadas
-Python (lenguaje de programacion utilizado gracias a su versatilidad y facilidad de sintaxis)
-PyCharm (IDE utilizado por generar un ambiente muy propicio para Python y el cual contiene Pytest y Requests incluidos como packages listos para descargar)
-Pytest (framework usado en el testing por facilitar una reporteria de cada prueba y en conjunto)
-Requests (HTTP library que se adapta apropiadamente para Python y se puede utilizar para automatizar pruebas API´s)


# La documentacion API se puede obtener desde ApiDocs de la siguiente manera:
1) Se ejercuta el servidor y se copia la URL del proporcionada en la plataforma TripleTen. Desgraciadamente este paso solo lo podran hacer personas que tienen acceso a la plataforma o sea que estan inscritos al programa de QA analyst.
2) A la URL obtenida en el paso anterior se le agrega el path /docs/
3) Enter

# La siguiente descripcion habla de como ejecutar las pruebas en el actual proyecto:
1) Si tienes descargado PyCharm ignora esta instruccion. Si no es el caso entonces descarga la version gratuita de PyCharm y elige la opcion que coincida con tu hardware.
![Captura de pantalla 2024-09-03 a la(s) 12 49 38 p m](https://github.com/user-attachments/assets/cc64f5fe-b551-4e03-8dc7-db0bf1c10d3e)


1) Para el actual proyecto se descargaron los packages "requests" y "pytest" (si no estan instalados deben instalarse 
para poderse ejecutar)
2) configuration.py contiene URL y paths como variables y data.py contiene diccionarios que se utilizaran a lo largo
del archivo create_kit_name_kit_test.py
3) Para asegurar efectividad de la automatizacion la variable URL_SERVICE en configuration.py debe actualizarse cada 
cierto tiempo a traves de iniciar el servidor en la plataforma de TripleTen
4) El archivo sender_stand_request.py se utilizo para generar el usuario necesario y obtener informacion 
para poder realizar las pruebas en create_kit_name_kit_test.py
5) Para ejecutar el programa se debe situar en el archivo create_kit_name_kit_test.py y ejecutar Run 
6) Una de las particularidades de Pytest es identificar las funciones que comienzan con test..... asi que las 9 
pruebas contenidas en 9 funciones con dicho comienzo son las que deberian ejecutarse.
