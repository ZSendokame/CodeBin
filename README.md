# Code bin
***Code bin*** it's a secure JSON API to manage your files.<br>
It's completely backend, no front-end.<br>

# How to install
```
git clone https://github.com/ZSendokame/CodeBin
```

# How to use
After downloading, here is a brief tutorial.

### Start API:
```
cd CodeBin; python api.py
```

### Routes:
```bash
# (GET) Return all files with it's size and creation date.
http://localhost:5000/

# (GET) Download the selected file.
http://localhost:5000/download/<File>

# (POST) Submit a file with JSON data.
http://localhost:5000/post
{
    "file": fileContent,
    "file_two": fileContent
}

# Also, you can create directories.
{
    "type": "directory"
    "directory": [
        "directory_one",
        "directory_two"
    ]
}

# (POST) Delete selected files, it receives an array.
http://localhost:5000/delete
[
    "file_one",
    "file_two"
]
```