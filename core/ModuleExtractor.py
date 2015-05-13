# coding=utf-8
import re
class ModuleExtractor:

    def __init__(self):
        pass

    def getModule(self,file,prefix="files/"):
        if len(prefix)>0:
            file = file.replace(prefix,"")
        if self.isICE(file):
            arr = file.split("_")
            module = arr[1]
            module = module[:2]
            return module.lower()
        elif self.isBAS(file):
            return ""
        elif file.find("_")==3:
            module =  file[:2]
            return module.lower()
        return ""
    def isICE(self,file):
        return file[:3]=="ICE"

    def isBAS(self,file):
        return file[:3]=="BAS"
