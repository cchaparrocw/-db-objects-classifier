class querys:

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

	def select_qry(self,query,object):
		"""executes SQL SELECT query"""
		qyerystr=query %(object)
		cur = db_conn().cursor()
		cur.execute(querystr)
		results = cur.fetchall()
		cur.close()
		return results