from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "status": "success",
        "message": "Servidor web operando correctamente en la nube gratuita",
        "modulo": "Entorno Web y Servidor - Proyecto"
    })

@app.route('/health')
def health_check():
    return jsonify({"status": "UP", "server": "running"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
