# coding=utf-8

import os
import shutil
import re

from  core.validator.BuilderFileValidator import BuilderFileValidator

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

def buildDirectories():
    #verifico si existe la estructura creada anteriormente
    #para eliminarla
    #esto si se quiere borrar todo
    if os.path.exists( pathDeploy ):
        shutil.rmtree( pathDeploy )
    #creo la estructura de directorios para copiar la información
    #posteriormente.
    for path in paths:
        os.makedirs( pathDeploy + path )

def main():
    #buildDirectories()
    builderValidator  = BuilderFileValidator()
    validator = builderValidator.build()
    file = 'LNS_acumulado'
    type = validator.validate(file)
    print( type )
if __name__ == "__main__":
    main()
