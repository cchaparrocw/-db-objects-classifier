#coding=utf-8
import shutil
import os
from core.Router import Router
from core.ModuleExtractor import ModuleExtractor
class get_files:

    _router = None
    _extractor = None
    RE_INVALID_FNAME = re.compile(r'[^a-z0-9\.\\/]')

    def __init__(self):
        self._router = Router()
        self._extractor = ModuleExtractor()


    def normalize_fname(self,fname):
        """replaces to _ strange chars in filename te be created"""
        fname = fname.lower()
        fname = RE_INVALID_FNAME.sub('_', fname)
        return fname

    def save(self,file,path,object):
        s = file
        fname = os.path.join(path, '%s.sql' % (normalize_fname(object)))
        f = open_file_write(fname)
        output_line(s, f)
        f.close()

    def open_file_write(self,fname):
        """opens file for writing in required encoding"""
        CREATED_FILES.append(fname)
        return codecs.open(fname, 'w', OUT_FILE_ENCODING)

    def copy(self,file,path):
        if os.path.exists( path ):
            shutil.copy2(file, path)
        else:
            os.makedirs( path )
            shutil.copy2(file, path)