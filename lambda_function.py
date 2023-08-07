import json
import logging
import os
from get_muestras import get_muestras
from conexionPostgress import queryRDS
from datetime import datetime
import warnings

warnings.filterwarnings("ignore")

### variable
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    headers = event.get('headers')
    api_key = headers.get('API_key')

    idDeudor = queryRDS(api_key)
    faena = headers.get('faena')
    fecha_desde = headers.get('fecha-desde')
    fecha_hasta = headers.get('fecha-hasta')

    ########################################################
    ##### se valida que los parametros sean correctos
    try:
        fecha_desde = datetime.strptime(fecha_desde, "%Y-%m-%d")
        fecha_hasta = datetime.strptime(fecha_hasta, "%Y-%m-%d")
    except:
        return {'statusCode': 500,'body': 'Uno o mas parametros no tienen el formato adecuado'}

    ########################################################
    ##### se confirma que la API KEY sea valida
    if idDeudor is None:
        return {'statusCode': 401, 'body': json.dumps('Unauthorized')}
    
    method = event.get('httpMethod')
    path   = event.get('path')

    if method not in ['GET']:
        return {'statusCode': 405, 'body': json.dumps('Method Not Allowed')}
    
    if method == 'GET':
        response_body = manage_get_request(path,idDeudor,faena,fecha_desde,fecha_hasta)
#        response_body = 'listo'
        return {'statusCode': 200, 'body': response_body}

    return {'statusCode': 500,'body': json.dumps('Error')}
    

def manage_get_request(path,idDeudor,faena,fecha_desde,fecha_hasta):
    if path == '/muestras':
        return get_muestras(idDeudor,faena,fecha_desde,fecha_hasta)
    
