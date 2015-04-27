# coding=utf-8
class FileClassifier:
    def __init__(self):
        pass
    def setNext(self,next):
        raise NotImplementedError('subclasses must override setNext()!')

    def classifier(self,type,file):
        raise NotImplementedError('subclasses must override setNext()!')
