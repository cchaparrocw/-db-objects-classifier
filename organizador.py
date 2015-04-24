
# coding=utf-8
"""
Script para organizar la información de la base de datos generada
De acuerdo a los estandares de casewaresa
"""

import os
import shutil

pathDeploy = r'build/'
paths = [
    'sql/fisica/table',
    'sql/fisica/sequence',
    'sql/fisica/index',
    'sql/fisica/constraint',
    'sql/fisica/constraint/fk',
    'sql/fisica/constraint/nofk',
    'sql/fisica/logica-plsql',
    'sql/fisica/logica-plsql/package',
    'sql/fisica/logica-plsql/package-body',
    'sql/fisica/logica-plsql/trigger',
    'sql/query/datos',
    'sql/query/lov',
    'sql/query/join',
    'sql/query/report',
    'sql/query/bi'
]
#verifico si existe la estructura creada anteriormente
#para eliminarla
#esto si se quiere borrar todo
if os.path.exists( pathDeploy ):
    shutil.rmtree( pathDeploy )
#creo la estructura de directorios para copiar la información
#posteriormente.
for path in paths:
    os.makedirs( pathDeploy + path )
