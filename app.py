from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Lagos, Lagos State',
    'salary': 'NGN. 1,000,000.00'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Abuja, F.C.T',
    'salary': 'NGN. 500,000.00'
  },
  {
    'id': 3,
    'title': 'Backend Engineer',
    'location': 'Remote',
    'salary': 'USD. 10,000.00'
  },
  {
    'id': 4,
    'title': 'Frontend Engineer',
    'location': 'San Francisco, California',
    'salary': 'USD. 12,000.00'
  }
]


@app.route('/')
def hello_world():
  """Displays 'Hello World!' on the browser.'"""
  return render_template('home.html', jobs=JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
