# coding=utf-8
from core.extractor.GetSchema import GetSchema

class querys(GetSchema):

	TABLE_NAMES_SQL = """SELECT DISTINCT table_name
	FROM user_tables
	WHERE INSTR(table_name, 'X_') <> 1
	AND INSTR(table_name, '$') = 0
	AND NOT table_name IN (SELECT view_name FROM user_views)
	AND NOT table_name IN (SELECT mview_name FROM user_mviews)
	ORDER BY table_name
	"""


	TTABLE_COLUMNS = """SELECT column_name, data_type, nullable,
	decode(default_length, NULL, 0, 1) hasdef,
	decode(data_type,
		'DATE', '11',
		'NUMBER', data_precision || ',' || data_scale,
		data_length) data_length,
		data_default,
		char_length
	FROM user_tab_columns
	WHERE table_name='%s'
	"""

	TTABLE_COLUMNS_SQL = TTABLE_COLUMNS + " ORDER BY column_id "

	TAB_COMMENTS_SQL= """SELECT  * 
			FROM user_tab_comments
			WHERE table_name='%s'""" 

	TABLE_COMMENTS_SQL = """SELECT column_name, comments 
		FROM user_col_comments
		WHERE table_name='%s'
		"""

	NUMBER_OF_CONSTRAINTS = """SELECT COUNT(*)
		FROM user_constraints
		WHERE constraint_type = 'R' AND table_name='%s'
		"""

	TFOREIGN_KEYS_INFO_SQL = """
	SELECT uc.table_name, ucc.column_name, ucc.position
	, fc.table_name, uic.column_position, uic.column_name
	, uc.delete_rule, uc.constraint_name
	FROM user_cons_columns ucc
	,user_constraints fc
	,user_constraints uc
	,user_ind_columns uic
	WHERE  uc.constraint_type = 'R'
	AND    uc.constraint_name = ucc.constraint_name
	AND    fc.constraint_name = uc.r_constraint_name
	AND uic.index_name=fc.constraint_name
	AND uc.table_name='%s'
	ORDER BY uc.constraint_name, ucc.position, uic.column_position
	"""
	
	NO_FOREIGN_KEYS_INFO_SQL=""" SELECT uc.table_name,uc.constraint_name,uc.constraint_type,ucc.column_name,search_condition
	FROM user_constraints uc, user_cons_columns ucc
	WHERE uc.constraint_name = ucc.constraint_name
	AND uc.constraint_type in('P','U','C')
	AND uc.constraint_name not like  'SYS%%'
	AND uc.table_name='%s'
	"""

	TINDEXES_INFO_SQL = """SELECT DECODE(uniqueness,'UNIQUE','UNIQUE',null) ,index_name
	from user_INDEXES
	where table_name = '%s'
	and index_name not like 'SYS%%'"""

	TINDEXES_COLUMNS_INFO_SQL="""SELECT column_name
	FROM user_ind_columns
	WHERE index_name = '%s'
	ORDER BY column_position
	"""

	GET_PACKAGES_SQL= """ SELECT object_name 
	FROM user_objects 
	WHERE object_type='PACKAGE' 
	ORDER BY 1
	""" 

	GET_PACKAGE_DEFINITION_SQL= """SELECT text 
	FROM sys.user_source 
	where name = '%s' 
	AND type='%s' 
	ORDER BY line
	"""


	def select_qry(self,query,object=''):
		"""executes SQL SELECT query"""
		if object is not '':
			query+=' % (\''+object+'\')'
		print query
		querystr=query
		exec query
		
		cur = self.db_conn().cursor()
		cur.execute(querystr)
		results = cur.fetchall()
		cur.close()
		return results
