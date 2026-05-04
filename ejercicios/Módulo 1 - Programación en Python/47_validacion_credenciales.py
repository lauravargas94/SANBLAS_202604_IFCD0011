"""
Programa que permite validar las credenciales formadas
por un correo electrónico y una contraseña.

La contraseña se obtiene de un fichero cifrada con SHA256
"""
import modulo_47_gestor_credenciales as credenciales

if __name__=='__main__':
    email = input('Introduce tu email:')
    password = input('Introduce tu contraseña:')

    es_valido = credenciales.validar_credenciales(email, password)
    print(es_valido)




    