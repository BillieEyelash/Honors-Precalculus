from flask import Flask, render_template, request
from SineCalculator import sin, cos, tan

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        try:
            rad = float(request.form.get('radians'))
        except:
            return render_template('index.html', error=True)
        sine = round(sin(rad), 3)
        cosine = round(cos(rad), 3)
        tangent = round(tan(rad), 3)
        return render_template('index.html', sine=sine, cosine=cosine, tangent=tangent)
