from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title='Flask App')

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        # In a real app, you would store this data or send an email
        return render_template('thank_you.html', name=name)
    return render_template('contact.html', title='Contact')

if __name__ == '__main__':
    app.run(debug=True)
