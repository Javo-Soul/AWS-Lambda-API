import psycopg2
import os

def conexionPostgres():
    conexion = ''
    try:
        host     = os.environ.get('POSTGRESQL_HOST')
        username = os.environ.get('POSTGRESQL_USER')
        password = os.environ.get('POSTGRESQL_PASSWORD')
        database = os.environ.get('POSTGRESQL_DB')

        conexion = psycopg2.connect(host = host,database = database,user = username,password = password)
        
        conexion.autocommit = True

    except Exception as e:
        print("Error", e)        

    return conexion


def queryRDS(id_deudor):
    query = f''' select id_deudor FROM copec_lims_prd.ft_deudores
                 where id_deudor = {id_deudor}'''
    response = []
    try:
        conexion = conexionPostgres()
        cursor = conexion.cursor()
        cursor.execute(query)
        response = cursor.fetchone()
        cursor.close()
    except Exception as e:
        response = 'Error aca'+ str(e)

    if response == None:
        response = None
    else:
        response = str(response[0])

    return response
