# coding=utf-8

import os
import shutil
import re
from os import listdir
from os.path import isfile, join
from stat import ST_MODE, S_IWRITE

from core.validator.BuilderFileValidator import BuilderFileValidator
from core.classifier.BuilderFileClassifier import BuilderFileClassifier
from core.Router import Router
from core.ModuleExtractor import ModuleExtractor
from core.format.ConstraintForeingKeyFormatter import ConstraintForeingKeyFormatter

def buildDirectories():
    #verifico si existe la estructura creada anteriormente
    #para eliminarla
    #esto si se quiere borrar todo
    router = Router()
    if os.path.exists( router.pathDeploy ):
        shutil.rmtree( router.pathDeploy, ignore_errors=True )
        #shutil.rmtree( pathDeploy , onerror=del_rw )

    #creo la estructura de directorios para copiar la información
    #posteriormente.
    router = Router()
    paths = router.getSimplePaths()
    print(paths)
    for path in paths:
        os.makedirs( router.pathDeploy + path )

def del_rw(action,name, exc ):
    os.chmod(name, stat.S_IWRITE)
    os.remove(name)

def loadFiles():
    router = Router()
    return [ f for f in listdir(router.pathSource ) if isfile(join(router.pathSource,f)) ]

def main():
    """
    buildDirectories()
    files = loadFiles()
    router = Router()
    for file in files:
        builderValidator  = BuilderFileValidator()
        validator = builderValidator.build()
        type = validator.validate(file)
        builderClassifier = BuilderFileClassifier()
        classifier = builderClassifier.build()
        classifier.classifier(type,router.pathSource+file)
    """
    router = Router()
    ConstraintForeingKey=ConstraintForeingKeyFormatter()
    for dirName, subdirList, fileList in os.walk(router.pathDeploy):
        print('Found directory: %s' % dirName)
        ConstraintForeingKey.format(dirName)
if __name__ == "__main__":
    main()
