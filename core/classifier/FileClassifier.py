# coding=utf-8
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

    def classifier(self,type,file):
        raise NotImplementedError('subclasses must override setNext()!')
