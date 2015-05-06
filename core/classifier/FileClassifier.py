# coding=utf-8
import shutil
import os
from core.Router import Router
from core.ModuleExtractor import ModuleExtractor
class FileClassifier:

    _router = None
    _extractor = None

    def __init__(self):
        self._router = Router()
        self._extractor = ModuleExtractor()

    def setNext(self,next):
        raise NotImplementedError('subclasses must override setNext()!')

    def classifier(self,type,file,move=False):
        raise NotImplementedError('subclasses must override setNext()!')

    def copy(self,file,path):
        if os.path.exists( path ):
            shutil.copy2(file, path)
        else:
            os.makedirs( path )
            shutil.copy2(file, path)
