from flask import Flask, render_template, request
from hatebert import user_input_fn, load_model, load_tokenizer

app = Flask(__name__)

# Load the model and tokenizer
model = load_model()
tokenizer = load_tokenizer()

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    plot = None
    if request.method == 'POST':
        user_input = request.form['user_input']
        result, plot = user_input_fn(user_input, model, tokenizer)
    return render_template('index.html', result=result, plot=plot)

if __name__ == '__main__':
    app.run(debug=True)
