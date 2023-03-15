from flask import Flask, render_template
from database import engine, load_jobs_from_db
from sqlalchemy import text

app = Flask(__name__)


@app.route('/')
def hello_world():
  """Displays 'Hello World!' on the browser.'"""
  jobs = load_jobs_from_db()
  return render_template('home.html', jobs=jobs)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
