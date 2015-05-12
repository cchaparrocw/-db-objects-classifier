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
from core.format.BuilderFormat import BuilderFormat

from core.validator.read.BuilderReadingValidator import BuilderReadingValidator

from core.extractor.GetSchema import GetSchema

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

def loadFilesDefault():
    router = Router()
    path = router.getPath("default","")
    return [ f for f in listdir( path ) if isfile(join(path,f)) ]


def main():

    #buildDirectories()
    #files = loadFiles()
    router = Router()
    """
    for file in files:
        builderValidator  = BuilderFileValidator()
        validator = builderValidator.build()
        type = validator.validate(file)
        builderClassifier = BuilderFileClassifier()
        classifier = builderClassifier.build()
        classifier.classifier(type,router.pathSource+file)

    router = Router()

    for dirName, subdirList, fileList in os.walk(router.pathDeploy):
       # print('Found directory: %s' % dirName)
       #ConstraintForeingKey.format(dirName)
       builderFormat = BuilderFormat()
       formatter = builderFormat.build()
       formatter.format(dirName)
    
    print("proceso normal finalizado")
    #proceso para los archivos que quedaron en dafault
    print("iniciando proceso en default...")
    files = loadFilesDefault()
    #print(files)
    pathDefault = router.getPath("default","")

    for file in files:
        print("file")
        print(file)
        builderReadingValidator = BuilderReadingValidator()
        readingValidator = builderReadingValidator.build()
        tipo= readingValidator.validate(pathDefault+"/"+file)
        #tipo = 1
        print("type:")
        print(tipo)
        builderClassifier = BuilderFileClassifier()
        classifier = builderClassifier.build()
        if( tipo is not None  and  tipo != 0):
            classifier.classifier(tipo,pathDefault+"/"+file,True)

    #for dirName, subdirList, fileList in os.walk(router.pathDeploy):
    #   builderFormat = BuilderFormat()
    #   formatter = builderFormat.build()
    #   formatter.format(dirName)
"""
    get_schema  = GetSchema()
    print("proceso finalizado")


if __name__ == "__main__":
    main()
