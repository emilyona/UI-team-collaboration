from flask import Flask, render_template
from flask import request, jsonify


import matplotlib
import yt
import random
import numpy as np

matplotlib.use('agg')

app = Flask(__name__)
app.secret_key = 's3cr3t'
app.debug = True



@app.route('/')
def index():
    return render_template('/index.html')


@app.route('/background_process')
def background_process():
	try:

        #eval to convert the string into any array
		redValues = np.asarray(eval(request.args.get('redValues')))
        	greenValues = np.asarray(eval(request.args.get('redValues')))
		blueValues = np.asarray(eval(request.args.get('redValues')))

		print(smooth(redValues,10))
        	print(redValues)

                print assignValues(redValues,greenValues, blueValues)

		return jsonify(result='data arrived')
		
	except Exception as e:
		return str(e)
    
def assignValues(redVal, greenVal, blueVal):
        ctf = yt.ColorTransferFunction( (-10.0, -5.0) )
        ctf.add_layers(8)
        ctf.red.y = redVal
        ctf.green.y = np.asarray([random.random() for _ in xrange(256)])
        ctf.blue.y = np.asarray([random.random() for _ in xrange(256)])
        
        '''
        ctf.red.y = smooth(redVal, 20)
        ctf.green.y = smooth(greenVal, 20)
        ctf.blue.y = smooth(blueVal, 20)
        '''
        ctf.plot("static/img/result.png")
        
def smooth(y, box_pts):
    box = np.ones(box_pts)/box_pts
    y_smooth = np.convolve(y, box, mode='same')
    return y_smooth
        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)