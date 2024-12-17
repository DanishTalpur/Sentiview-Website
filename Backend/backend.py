import pickle
from flask import Flask, render_template, request

with open('sentiment_model.pkl', 'rb') as model_file:
    sentiment_model = pickle.load(model_file)

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def main():
    return render_template('main.html')

@app.route('/index', methods=['POST', 'GET'])
def index():
    if request.method=='POST':
        input_tweet= request.form['tweet']
        output= sentiment_model.predict([input_tweet])
        if output==[-1]:
            sentiments="Negative"
        elif output==[1]:
            sentiments="Positive"
        else:
            sentiments="Neutral"
        return render_template('index.html', output=sentiments)
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)

