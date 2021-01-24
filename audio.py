from flask import *
from flask.views import MethodView
import os
import time
import datetime
lines = os.listdir("D:\\pdfreader\\templates\\audio\\")

# app.route("/wav")
# def streamwav():
#     def generate():
#         with open("signals/song.wav", "rb") as fwav:
#             data = fwav.read(1024)
#             while data:
#                 yield data
#                 data = fwav.read(1024)
#     return Response(generate(), mimetype="audio/x-wav")

app = Flask(__name__)

@app.route("/color/",methods=["GET"])
def mus():
    return render_template('index.html',lines=lines)
        
# def generate(line):
#     with open(f"static/{line}", "rb") as fwav:
#         data = fwav.read(1024)
#         while data:
#             yield data
#             data = fwav.read(1024)
            
    


if __name__ == "__main__":
    print(lines)
    app.run(host='192.168.0.118', port=3000,debug=True)
