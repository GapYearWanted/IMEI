from flask import Flask, render_template
from pyimei import ImeiSupport

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():    
    return render_template('index.html', imei=ImeiSupport.generateNew())

@app.route('/thank')
def thank():    
    return render_template('thank.html')
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')