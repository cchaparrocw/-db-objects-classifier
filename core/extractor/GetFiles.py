#coding=utf-8
import shutil
import os
import re
from core.Router import Router
from core.ModuleExtractor import ModuleExtractor
from core.extractor.Querys import querys
from core.extractor.GetSchema import GetSchema
from core.extractor.GetTables import get_tables
from core.extractor.GetForeign import get_foreign
from core.extractor.GetNoForeign import get_no_foreign
from core.extractor.GetIndex import get_index
from core.extractor.GetPackage import get_package

class getfiles:

    RE_INVALID_FNAME = re.compile(r'[^a-z0-9\.\\/]')
 

    _router = None
    _extractor = None

    
    def __init__(self):
        self._router = Router()
        self._extractor = ModuleExtractor()

    def normalize_fname(self,fname):
        """replaces to _ strange chars in filename te be created"""
        fname = fname.lower()
        fname = self.RE_INVALID_FNAME.sub('_', fname)
        return fname

    def save(self,file,object,type):
        
        module = self._extractor.getModule(object)
        path = self._router.getPath(type,module)
        if not os.path.exists(path):
            os.makedirs(path)
        fname = os.path.join(path, '%s.sql' % (self.normalize_fname(object)))
        print fname
        with open( fname ,'a+') as f:
            f.write(file)
        f.close()

    def copy(self,file,path):
        if os.path.exists( path ):
            shutil.copy2(file, path)
        else:
            os.makedirs( path )
            shutil.copy2(file, path)

    def dump_db_info(self):
        """saves information about database schema in file/files"""
        query = querys()
        tables = get_tables()
        foreign= get_foreign()
        noforeign=get_no_foreign()
        index=get_index()
        package=get_package()

        rs = query.select_qry('querystr=self.TABLE_NAMES_SQL')
        if rs:
          for row in rs:
            table = row[0]
            """
            tfs=tables.save_table_definition(table)
            self.save(tfs[0],tfs[1],tfs[2])
            ffs=foreign.save_foreign_key_definition(table)
            if ffs[0] is not '':
                self.save(ffs[0],ffs[1],ffs[2])
        
            nffs=noforeign.save__noforeign_key_definition(table)
            if nffs[0] is not '':
                self.save(nffs[0],nffs[1],nffs[2])
            
            ifs=index.save_indexes_definition(table)
            if ifs:
                self.save(ifs[0],ifs[1],ifs[2])

            """
        rs = query.select_qry('querystr=self.GET_PACKAGES_SQL')
        for row in rs:
            pks=row[0]
            """
            pfs=package.save_package_definition(pks)
            self.save(pfs[0],pfs[1],pfs[2])
            """
            pbfs=package.save_package_body_definition(pks)
            if pbfs:
                self.save(pbfs[0],pbfs[1],pbfs[2])

    def connect(self):
        get_schema = GetSchema()
        if not get_schema.init_db_conn("connect_string = cx_Oracle.makedsn('soporte.casewaresa.com', 1521, 'soporte')", 'iceberg_pre', 'icebergpre2013'):
            print_err('Something is terribly wrong with db connection')
            return 0
        self.dump_db_info()