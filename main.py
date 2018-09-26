from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                border: 2px black solid;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>

        <form action="/" method="POST">
            <label>Rotate by:
                <input name="rot" type="text" value="0"/>
            </label><br>
            <br><br>
            <label>Encrypted data
                <textarea name="text_before" rows="20" cols="20">{0}</textarea>
            </label>
            <br>
            <input type="submit">
        </form>

"""

@app.route("/")
def index():
    return form.format("")

@app.route("/", methods=['POST'])
def encrypt():
    rot = request.form['rot']
    rot = int(rot)
    text = request.form['text_before']
    encrypted_text = rotate_string(text, rot)
    return form.format(encrypted_text)


app.run()
