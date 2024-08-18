# Proyecto Urban Grocers 
El siguiente proyecto aborda pruebas de API especificamente para crear kits a partir de usuarios creados en la aplicacion 
Urban Grocers.

La documentacion API se puede obtener de la siguiente manera:
1) se ejercuta el servidor y se copia la URL del banco
2) se agrega a la URL el path /docs/
3) enter

La siguiente descripcion habla de como ejecutar las pruebas en el actual proyecto:

1) Para el actual proyecto se descargaron los packages "requests" y "pytest" (si no estan instalados deben instalarse 
para poderse ejecutar)
2) configuration.py contiene URL y paths como variables y data.py contiene diccionarios que se utilizaran a lo largo
del archivo create_kit_name_kit_test.py
3) Para asegurar efectividad de la automatizacion la variable URL_SERVICE en configuration.py debe actualizarse cada 
cierto tiempo a traves de iniciar el servidor en la plataforma de TripleTen
4) Se decidio que el archivo sender_stand_request.py no iria a ser parte del actual proyecto asi que permanecera
inutil y vacio.
5) Para ejecutar el programa se debe situar en el archivo create_kit_name_kit_test.py y ejecutar Run 
6) Una de las particularidades de Pytest es identificar las funciones que comienzan con test..... asi que las 9 
pruebas contenidas en 9 funciones con dicho comienzo son las que deberian ejecutarse.
