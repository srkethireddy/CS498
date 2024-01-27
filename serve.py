from flask import Flask, request
import subprocess
import socket

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def handle_requests():
    if request.method == 'POST':
        try:
            subprocess.Popen(['python', 'stress_cpu.py'])
            return 'CPU stress started!', 200
        except Exception as e:
            return f'Error: {str(e)}', 500
    elif request.method == 'GET':
        private_ip = socket.gethostbyname(socket.gethostname())
        return f'Private IP Address: {private_ip}', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
