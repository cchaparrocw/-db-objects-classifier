# coding=utf-8
class GetSchema():
  import codecs
  import sys
  import os
  import zipfile

  import os.path
  import time
  import re
  from core.extractor.Querys import querys
  import getfiles

  USE_JYTHON = 0

  TABLES_ONLY = 0

  try:
    from com.ziclix.python.sql import zxJDBC
    USE_JYTHON = 1
    USAGE = JUSAGE
  except:
    import cx_Oracle


  DB_ENCODINGS = ('cp1250', 'iso8859_2', 'utf8')

  OUT_FILE_ENCODING = 'UTF8'

  def __init__():
    """main function"""
    connect_string, username, passwd = conn_args
    exec connect_string
    separate_files = '--separate-files' in sys.argv
    if separate_files:
      if os.path.exists(SCHEMA_DIR):
        if not '--force-dir' in sys.argv:
          print_err('Output directory "%s" already exists,\nuse --force-dir or --date-dir option!' % (SCHEMA_DIR))
          return 0
    stdout = sys.stdout
    out_f = None
    out_fn = get_option_value('-o')
    if out_fn:
      if '--date-dir' in sys.argv:
        os.mkdir(SCHEMA_DIR)
        out_fn = os.path.join(SCHEMA_DIR, out_fn)
      out_f = open(out_fn, 'w')
      sys.stdout = out_f
      CREATED_FILES.append(out_fn)

    if not init_db_conn(connect_string, username, passwd):
      print_err('Something is terribly wrong with db connection')
      return 0
    dump_db_info(separate_files, out_f, stdout)

    

  def dump_db_info(separate_files, out_f, stdout):
    """saves information about database schema in file/files"""
    test = '--test' in sys.argv
    if test or separate_files:
      for dn in (TABLES_INFO_DIR, VIEWS_INFO_DIR, SEQUENCES_INFO_DIR, FUNCTIONS_INFO_DIR, PROCEDURES_INFO_DIR, PACKAGES_INFO_DIR, CONSTRAINT_FK_INFO_DIR, CONSTRAINT_NOFK_INFO_DIR, INDEXES_INFO_DIR):
        ensure_directory(dn)

      if not test:
        sorted_in_comment = '--sorted-info' in sys.argv
        rs = select_qry(TABLE_NAMES_SQL)
        if rs:
          for row in rs:
            table = row[0]
            save_table_definition(table, sorted_in_comment)
            save_foreign_key_definition(table, sorted_in_comment)
            #save__noforeign_key_definition(table, sorted_in_comment)
            #save_indexes_definition(table , sorted_in_comment)
    else:
      pass
      #show_tables()
    if not TABLES_ONLY and not test:
      show_additional_info(separate_files)
    output_line('\n\n--- the end ---')
    if out_f:
      out_f.close()
      sys.stdout = stdout
    if '--zip' in sys.argv:
      save_files_in_zip()