import os
from flask import Flask, render_template, url_for, send_from_directory, request, redirect
app = Flask(__name__)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, 'static'),
        'airplane.ico', mimetype='image/vnd.microsoft.icon'
    )

@app.route('/')
@app.route('/index.html')
def home():
    return render_template('index.html')

@app.route('/works.html')
def works():
    return render_template('works.html')

@app.route('/work.html')
def work():
    return render_template('work.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')
    
@app.route('/<path:page_name>')
def render_template_for(page_name):
    return render_template(page_name)

@app.route('/submit_contact_form', methods=['GET', 'POST'])
def submit_contact_form():
    if request.method == 'POST':
        print('>>>>', request.form)
        data = request.form.to_dict()
        print(data)
        return redirect('/thank_you.html')

    else:    
        return 'Something goes wrong !!'