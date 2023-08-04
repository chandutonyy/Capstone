from flask import Flask, request, render_template
from hatebert import user_input_fn, load_model, load_tokenizer
import os

app = Flask(__name__)

model = load_model()
tokenizer = load_tokenizer()

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None
    prediction_text = None
    plot = None

    if request.method == 'POST':
        # Delete previous plot
        plot_path = "static/plot.png"  # Or whatever is the path to your plot
        if os.path.exists(plot_path):
            os.remove(plot_path)

    if request.method == 'POST':
        user_input = request.form.get('user_input')
        if user_input:
            prediction, prediction_text, plot_path = user_input_fn(user_input, model, tokenizer)

            # Store the path to the plot
            plot = plot_path

    return render_template('index.html', prediction=prediction, prediction_text=prediction_text, plot=plot)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
