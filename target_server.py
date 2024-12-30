from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(f"POST request received with data: {request.data}")
    else:
        print(f"GET request received from {request.remote_addr}")
    return "Request received", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001)
