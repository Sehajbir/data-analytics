from flask import Flask, render_template, url_for, request, send_file
from data1 import temp
from LSS import LSS
import os
app = Flask(__name__)
DOWNLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/downloads/'
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dataProject1')
def ClassificationEnsembler():
    return render_template('data1.html')

@app.route('/data1/evaluation', methods = ['GET', 'POST'])
def uploadBinaryClassificationEnsembler():
    if request.method == 'POST':
      f = request.files['file']
      f.filename = 'data.csv'
      f.save("data1/"+f.filename)
      result = temp.Classifier()
      fi = open("data1/result.txt", "w+")
      fi.write("The suggested models that should be used are : %s\n" % result.get("Models Used"))
      fi.write("These have an accuracy of %s" % result.get("Accuracy"))
      fi.close()
      return send_file('data1/result.txt', as_attachment=True)
@app.route('/leastSumOfSquares')
def leastSumOfSquares():
      return render_template('leastSumOfSquares.html')

@app.route('/eval/leastSumOfSquares' ,methods = ['GET', 'POST'])
def uploadLeastSumOfSquares():
      if request.method == 'POST':
            f = request.files['file']
            f.filename = 'data.csv'
            f.save("LSS/"+f.filename)
            result = LSS.leastSumOfSquares()
            fi = open("LSS/result.txt", "w+")
            fi.write("The suggested weights that should be used are : %s\n" % result.get("Weights Used :"))
            fi.write("These have a value of %s" % result.get("Least Sum Of Squares :"))
            fi.close()
            return send_file('LSS/result.txt', as_attachment=True)

if __name__ == '__main__':
    app.run(debug = True)