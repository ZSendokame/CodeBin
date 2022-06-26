import os
import time
from flask import Flask, request, send_file

app = Flask(__name__)

@app.get('/')
def root():
    directory_list = os.listdir('./code')
    data = {}

    for file in directory_list:
        relative_file = './code/' + file

        data[file] = {
            'size': os.path.getsize(relative_file),
            'creation_date': time.ctime(os.path.getctime(relative_file))
        }

    return data

@app.get('/download/<file>')
def download(file):
    if os.path.exists('./code/' + file):
        return send_file('./code/' + file)

    return {
        'error': True,
        'error_data': 'File does not exists.'
    }

@app.post('/post')
def post():
    for file in request.json:
        with open('./code/' + file) as file_object:
            file_object.write(request.json[file])

    return "200"

@app.post('/delete')
def delete():
    for file in request.json:
        if os.path.exists('./code/' + file):
            os.remove('./code/' + file)

    return "200"

app.run()