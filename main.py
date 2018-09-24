from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
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
                border: 2px black solid;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>

        <form method="POST">
            <label>Rotate by:
                <input name="rotate" type="number" value="rotnum"/>
            </label><br>
            <br><br>
            <label>Bla
                <textarea name="caesar_text" rows="20" cols="20"></textarea>
            </label>
            <br>
            <input type="submit">
        </form>

"""

@app.route("/")
def index():
    return form


app.run()
