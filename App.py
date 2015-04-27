# coding=utf-8

import os
import shutil
import re
from os import listdir
from os.path import isfile, join
from stat import ST_MODE, S_IWRITE

from  core.validator.BuilderFileValidator import BuilderFileValidator
from core.classifier.BuilderFileClassifier import BuilderFileClassifier

pathDeploy = r'build/'
pathSource = r'files/'
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
        shutil.rmtree( pathDeploy, ignore_errors=True )
        #shutil.rmtree( pathDeploy , onerror=del_rw )

    #creo la estructura de directorios para copiar la información
    #posteriormente.
    for path in paths:
        os.makedirs( pathDeploy + path )

def del_rw(action,name, exc ):
    os.chmod(name, stat.S_IWRITE)
    os.remove(name)

def loadFiles():

    return [ f for f in listdir(pathSource ) if isfile(join(pathSource,f)) ]

def main():
    buildDirectories()
    files = loadFiles()
    for file in files:
        builderValidator  = BuilderFileValidator()
        validator = builderValidator.build()
        type = validator.validate(file)
        builderClassifier = BuilderFileClassifier()
        classifier = builderClassifier.build()
        classifier.classifier(type,pathSource+file)

if __name__ == "__main__":
    main()
