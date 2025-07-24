from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flashing messages

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        flash(f"Thank you {name}, your message has been received!")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

