from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection_string)

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(row._asdict())

  return jobs

def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs where id = :val"),
                          {'val': id}
                         )
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return rows[0]._asdict()
  
#with engine.connect() as conn:
  #result = conn.execute(text("select * from jobs"))
  #result_dicts = []
  #for row in result.all():
    #result_dicts.append(row._asdict())

  #print(result_dicts)
  #print("type(result):", type(result))
  #result_all = result.all()
  #print("type(result.all()):", type(result_all))
  #first_result = result_all[0]
  #print("type(first_result):", type(first_result))
  #first_result_dict = dict()
  #first_result_dict = dict(result_all[0])
  #first_result_dict = result_all[0]._asdict()
  #print("type(first_result_dict):", type(first_result_dict))
  #print(first_result_dict)