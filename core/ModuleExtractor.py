# coding=utf-8
import re
class ModuleExtractor:

    def __init__(self):
        pass

    def getModule(self,file):
        arr = re.split("(^(([a-zA-Z]{1,3}_){1,2}))|(^[a-zA-Z]{1,3}_)", file)
        arr = arr[1:]
        module = arr[1:2]
        module = module[0]
        underscores = module.count("_")
        if underscores == 1:
            return module[:2]
        elif underscores == 2 :
            arr = module.split("_")
            module = arr[1]
            module = module[:2]
            return module
        else:
            return ""