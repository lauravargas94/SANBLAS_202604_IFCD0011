"""
Programa que permite registrar las credenciales formadas
por un correo electrónico y una contraseña.

La contraseña se almacena en un fichero cifrada con SHA256
"""
import modulo_47_gestor_credenciales as credenciales


if __name__=='__main__':
    email = input('Introduce tu email:')
    password = input('Introduce tu contraseña:')

    credenciales.guardar_credenciales(email, password)

    print('Las credenciales se han guardado satisfactoriamente')