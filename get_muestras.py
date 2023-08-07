import json
from conexionPostgress import conexionPostgres
import pandas as pd

def get_muestras(idDeudor,parametros):
    datosMuestras = parametros

    query = f'''select * FROM copec_lims_prd.muestra_rl as b
                inner join copec_lims_prd.ensayo_rl as a
                on a.correlativo = b.correlativo
                
                where id_solicitante in ({datosMuestras['faena']})
                and fecha_ensayo between cast('{datosMuestras['fechadesde']}' as date) and cast('{datosMuestras['fechahasta']}' as date)
                and id_deudor in ({idDeudor});'''
    
    try:
        datosMuestras = query

        # conexion = conexionPostgres()
        # dato = pd.read_sql(query,conexion)

        # if dato['codigo_ensayo'].count() == 0:
        #     datosMuestras = json.dumps('No existen datos!')

        # else:
        #     df = pd.DataFrame(dato)
        #     datosMuestras = df
        #     datosMuestras = df.to_json(orient="split")

    except Exception as e:
         datosMuestras = {json.dumps(str(e))}

    return datosMuestras
