import pickle
from flask import Flask, render_template, request

# Flask is a class
app = Flask(__name__)

# Now we need to undump our model
model = pickle.load(open('model.pkl', 'rb'))

# End points
# By default the methods is GET
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    # input should be in a 2D form
    rndspend = request.form.get('rndspend')
    administration = request.form.get('administration')
    marketingspend = request.form.get('marketingspend')
    state = request.form.get('state')
    a = 0
    b = 0 
    c = 0
    if state == 1:
        c = 1
    elif state == 2:
        a = 1
    else:
        b = 1
    prediction = model.predict([[a, b, c, rndspend, administration, marketingspend]])
    output = round(prediction[0], 2)
    return render_template('index.html', prediction = output)


# used to run the app
# debug=True -> error flash up in terminal
if __name__ == '__main__':
    app.run(debug=True)