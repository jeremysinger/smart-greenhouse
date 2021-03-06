from flask import Flask, Response, request, jsonify, render_template

app = Flask(__name__)

datafile = '/tmp/data.csv'

def getTimestamp():
    '''read the timestamp from the local data file'''
    return getMostRecentValue(0)

def getTemp():
    '''read the temperature (in 'C) from the local data file'''
    return getMostRecentValue(2)

def getHumid():
    '''read the humidity (%age) from the local data file'''
    return getMostRecentValue(1)

def getIrLight():
    '''read the IR light (in lux) from the local data file'''
    return getMostRecentValue(3)

def getVisLight():
    '''read the visible light (in lux) from the local data file'''
    return getMostRecentValue(4)

def getMostRecentValue(i):
    f = open(datafile, 'r')
    lines = f.readlines()
    lastLine = lines[-1]
    f.close()
    value = (lastLine.split(','))[i]
    return int(value)

@app.route('/')
def index():
    return render_template('index.html', temperature=getTemp(), humidity=getHumid(), irLight=getIrLight(), visLight=getVisLight(), tColor='red', hColor='red')

@app.route('/dashboard')
def dashboard():
    return "current temperature is " + str(getTemp())

@app.route('/temp')
@app.route('/temperature')
def temp():
    currentTemp = getTemp()
    return jsonify({'temperature': float(currentTemp)})

@app.route('/humid')
@app.route('/humidity')
def humid():
    currentHumid = getHumid()
    return jsonify({'humidity': float(currentHumid)})

@app.route('/light')
def light():
    irLight = getIrLight()
    visLight = getVisLight()
    return jsonify({'infrared (lux)': int(irLight),
                    'visible (lux)': int(visLight)})

@app.route("/download")
def download():
    with open("/tmp/data.csv") as fp:
        csv = fp.read()
        return Response(
            csv,
            mimetype="text/csv",
            headers={"Content-disposition":
                     "attachment; filename=data.csv"})

        
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port = 80)
