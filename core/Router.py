
class Router:

    def __init__(self):
        self.pathDeploy = r'build/'
        self.pathSource = r'files/'
        self.paths = [
            ('table',        'sql/fisica/table/%(modulo)s'),
            ('sequence',     'sql/fisica/sequence/%(modulo)s'),
            ('index',        'sql/fisica/index/%(modulo)s'),
            ('constraint',   'sql/fisica/constraint'),
            ('fk',           'sql/fisica/constraint/%(modulo)s/fk'),
            ('nofk',         'sql/fisica/constraint/%(modulo)s/nofk'),
            ('package',      'sql/fisica/logica-plsql/package/%(modulo)s'),
            ('package_body', 'sql/fisica/logica-plsql/package-body/%(modulo)s'),
            ('trigger',      'sql/fisica/logica-plsql/trigger/%(modulo)s'),
            ('datos',        'sql/query/datos/%(modulo)s'),
            ('lov',          'sql/query/lov/%(modulo)s'),
            ('join',         'sql/query/join/%(modulo)s'),
            ('report',       'sql/query/report/%(modulo)s'),
            ('bi',           'sql/query/bi/%(modulo)s')
        ]

    def getPath(self,path,module):
        for key,value in self.paths:
            if key==path:
                return self.pathDeploy + value % {'modulo':module}
        return ""
