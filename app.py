from flask import Flask, render_template, url_for, request, send_file
from data1 import temp
import os
app = Flask(__name__)
DOWNLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/downloads/'
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dataProject1')
def binaryClassificationEnsembler():
    return render_template('data1.html')

@app.route('/data1/evaluation', methods = ['GET', 'POST'])
def uploadBinaryClassificationEnsembler():
    if request.method == 'POST':
      f = request.files['file']
      f.filename = 'data.csv'
      f.save("data1/"+f.filename)
      result = temp.binaryClassifier()
      fi = open("data1/result.txt", "w+")
      fi.write("The suggested models that should be used are : %s\n" % result.get("Models Used"))
      fi.write("These have an accuracy of %s" % result.get("Accuracy"))
      fi.close()
      return send_file('data1/result.txt', as_attachment=True)
    
    
if __name__ == '__main__':
    app.run()