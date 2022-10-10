import os
from pathlib import Path
from dotenv import load_dotenv
import slack
from flask import Flask

env_path = Path('.') / '.env'
load_dotenv()

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "hello world redyeye"





if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)