from flask import Flask, request, jsonify, abort
import requests

app = Flask(__name__)

# รองรับหลาย API Key
API_KEYS = {"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6Imh0dHBzOi8vZGF0YS1rZWVwZXIub25yZW5kZXIuY29tIiwiaWF0IjoxNTE2MjM5MDIyfQ._f2gGhQVfmZk9c9tLG-KF5CGhDhTGtoE8JrmvsRAUeY", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6Imh0dHBzOi8vZGF0YS1rZWVwZXIub25yZW5kZXIuY29tIiwiaWF0IjoxNTE2MjM5MDIyfQ.eRVdPSuyKtWid-Q_TlvY0dk_4DLRJ3-VIgYF6qoAO90", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6Imh0dHBzOi8vZGF0YS1rZWVwZXIub25yZW5kZXIuY29tIiwiaWF0IjoxNTE2MjM5MDIyfQ.MxnFKE-9dWb7bVnSbg-ajEbcu_NEkmLcnWzTwKLNNm4"}

@app.before_request
def check_auth():
    if request.path.startswith('/translate'):
        token = request.headers.get("Authorization", "").replace("Bearer ", "")
        if token not in API_KEYS:
            abort(403)

@app.route('/translate', methods=['POST'])
def proxy_translate():
    try:
        payload = request.get_json()
        response = requests.post("http://libretranslate:5000/translate", json=payload)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/ping')
def ping():
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
