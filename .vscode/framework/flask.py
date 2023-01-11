from flask import Flask
app = Flask(_name_)

@app.route('/')
def sample():
    sample = "Hello world"
    return sample

if _name_ == "_main_":
    app.run()