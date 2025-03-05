import os

# Leer una variable de ambiente
covid19_host = os.getenv('COVID19_HOST')
covid19_api_key = os.getenv('X_API_KEY_COVID19')


if covid19_host:
    print(f'El valor de la variable es: {covid19_host}')
else:
    print('La variable de ambiente no está definida.')

if covid19_api_key:
    print(f'El valor de la variable es: {covid19_api_key}')
else:
    print('La variable de ambiente no está definida.')
