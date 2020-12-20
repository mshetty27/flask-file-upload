from flask import Flask, render_template, request, jsonify, abort
import os
from datetime import datetime

UPLOADS_DIRECTORY = "uploads" 
if not os.path.exists(UPLOADS_DIRECTORY):
    os.makedirs(UPLOADS_DIRECTORY)

application = Flask(__name__)

@application.route("/")
def index():
  return render_template("index.html")

@application.route("/upload", methods=["POST"])
def upload():
  if request.method == "POST":
    try:
      for item in request.files:
        current_file = request.files[item]
        filename, file_ext = os.path.splitext(current_file.filename)
        file_save_path = os.path.join(UPLOADS_DIRECTORY, make_unique_filename(filename, file_ext))
        current_file.save(file_save_path)
        return "", 201
    except Exception:
      abort(500, "Error occured while saving file")
  abort(400, "Method not allowed")

def make_unique_filename(filename, ext):
  return filename + "_" + datetime.now().strftime('%Y-%m-%d %H%M%S') + ext
  

if __name__ == "__main__":
  application.run(host="0.0.0.0", port=80)