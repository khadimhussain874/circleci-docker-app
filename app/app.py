from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def root():
    return jsonify({
        "message": "Welcome to my containerized app",
        "version": "1.0.0"
    })

@app.route('/health')
def health():
    return jsonify({
        "status": "unhealthy"
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
