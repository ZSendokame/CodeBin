import os
import shutil
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
    file_list = request.json if not 'type' in request.json \
        else request.json['directory']

    for file in file_list:
        file_path = './code/' + file.replace('../', '')

        if not 'type' in request.json:
            with open(file_path, 'a') as file_object:
                file_object.write(request.json[file])

        elif request.json['type'] == 'directory':
            os.mkdir(file_path)

    return "200"

@app.post('/delete')
def delete():
    for file in request.json:
        file_path = './code/' + file.replace('../', '')

        if os.path.exists(file_path):
            if os.path.isfile(file_path):
                os.remove(file_path)

            else:
                shutil.rmtree(file_path)

    return "200"

app.run()