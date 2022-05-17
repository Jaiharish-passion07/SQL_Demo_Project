import psycopg2
import psycopg2.extras


hostname = 'localhost'
database = 'webappdb'
username = 'postgres'
pwd = '123jai'
port_id = 5432
conn=None
try:
   conn=psycopg2.connect(
           database=database,
           user=username,
           password=pwd,
           host=hostname,
           port=port_id)
   conn.autocommit=True
   with conn.cursor() as cur:
      # db_name='webappdb'
      # drop_db_script=f'''DROP DATABASE IF EXISTS {db_name}'''
      # cur.execute(drop_db_script)
      # create_database_script=f'''CREATE DATABASE {db_name}'''
      # cur.execute(create_database_script)
      create_table_mech_dept_script='''CREATE TABLE IF NOT EXISTS mech_dept (
                                    student_id      INT PRIMARY KEY,
                                    student_name    VARCHAR(40) NOT NULL,
                                    Fluid_Mechanics  INT,
                                    Mechatronics INT,
                                    Mathematics INT 
                                    )'''
      create_table_cs_dept_script='''CREATE TABLE IF NOT EXISTS cs_dept (
                                    student_id      INT PRIMARY KEY,
                                    student_name    VARCHAR(40) NOT NULL,
                                    Data_Structure  INT,
                                    Computer_Architecture INT,
                                    SQL int
                                    )'''
      create_table_ds_dept_script='''CREATE TABLE IF NOT EXISTS ds_dept (
                                    student_id      INT PRIMARY KEY,
                                    student_name    VARCHAR(40) NOT NULL,
                                    Machine_learning  INT,
                                    Data_visualization INT,
                                    Python int
                                    )'''

      cur.execute(create_table_mech_dept_script)
      cur.execute(create_table_cs_dept_script)
      cur.execute(create_table_ds_dept_script)


       
except Exception as error:
   print(error)

finally:
   if conn is not None:
      conn.close()