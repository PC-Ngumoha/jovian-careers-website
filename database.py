from sqlalchemy import create_engine, text
import os

uri = os.getenv('DB_CONN_STR')


engine = create_engine(uri,
        connect_args={
          "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
          }
        })
def load_jobs_from_db():
  """Loads the jobs from the database"""
  with engine.connect() as conn:
    result = conn.execute(text('SELECT * FROM jobs'))

    jobs = []
    for job in result.all():
      jobs.append(dict(job._mapping))
    return jobs
