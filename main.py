from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form= """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
      <form method="post">
        <label for="rot">Robate by:
            <input id="rot" type="text" name="rot" value=0 /><br>
            <textarea name="text"></textarea>
        </label><br>
        <input type="submit"/>
    </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form

@app.route("/", methods=['POST'])
def encrypt():
    rotation = int(request.form['rot'])
    text = request.form['text']
    encrypted_text = rotate_string(text, rotation)
    return "<h1`>" + encrypted_text + "</h1>"

app.run()