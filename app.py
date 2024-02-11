from flask import Flask, jsonify, render_template, request

from database import add_application_to_db, load_job_from_db, load_jobs_from_db

app = Flask(__name__)

#JOBS = [{
#    'id': 1,
#    'title': 'Data Analyst',
#    'location': 'Bengaluru, India',
#    'salary': 'Rs. 10,00,000'
#}, {
#    'id': 2,
#    'title': 'Data Scientist',
#    'location': 'Delhi, India',
#    'salary': 'Rs. 15,00,000'
#}, {
#    'id': 3,
#    'title': 'Frontend Engineer',
#    'location': 'Remote',
##    'salary': 'Rs. 12,00,000'
#}, {
#    'id': 4,
#    'title': 'Backend Engineer',
#    'location': 'San Francisco, USA',
#    'salary': '$120,000'
#}]


@app.route('/')
def hellow_world():
  jobs = load_jobs_from_db()
  return render_template('home.html',
                         jobs = jobs,
                         company_name = 'AbdelHakim')


@app.route('/api/jobs')
def list_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)

@app.route('/job/<id>')
def show_job(id):
  job = load_job_from_db(id)
  if not job:
    return "Not Found", 404
  return render_template('jobpage.html',
                         job = job)

@app.route('/api/job/<id>')
def show_job_json(id):
  job = load_job_from_db(id)
  return jsonify(job)

@app.route('/job/<id>/apply', methods = ['POST'])
def apply_to_job(id):
  data = request.form
  job = load_job_from_db(id)

  add_application_to_db(id, data)
  # Store this data in the database
  # Send an email to the user
  return render_template('application_submitted.html',
                         application = data,
                         job = job)
    
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True, port=8080)
