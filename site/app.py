from flask import Flask,render_template,request,redirect,url_for
from werkzeug.utils import secure_filename
import sys, os
from os import path
import matlab
import runme_demo2

rootdir = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(rootdir, "static")
#runme_demo.initialize_runtime(['-nojvm', '-nodisplay'])
rmd2=runme_demo2.initialize()

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/", methods=['GET', 'POST'])
def run():
    if request.method == 'POST':        
        file1 = request.files['file1']
        file2 = request.files['file2']        
        if (file1.filename == '') or (file2.filename == ''):
            return render_template("hata.html")
        else:
            filename1 = secure_filename(file1.filename)
            file1.save(os.path.join(UPLOAD_FOLDER , filename1))
            path1=os.path.join(UPLOAD_FOLDER , filename1)
            #print(path1)
            filename2 = secure_filename(file2.filename)
            file2.save(os.path.join(UPLOAD_FOLDER , filename2))
            path2=os.path.join(UPLOAD_FOLDER , filename2)
            #print(path2)
            
            rmd2=runme_demo2.initialize()
            output4app=rmd2.runme_demo2(path1,path2)
            #print(output4app)

            return render_template("deneme.html", variable=output4app)
    elif request.method == 'GET':
        return render_template("hata.html")

if __name__== "__main__":
    app.run(host='0.0.0.0', port=80)
