from flask import Flask, render_template, request, send_file, jsonify
from helper import generate_qr_code

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({"data": "hello world"})

@app.route("/qr_code", methods=["POST"])
def qr_code():
    try:
        json_data = request.get_json()
        if "data" in json_data:
            generate_qr_code(json_data)
            
            data = json_data["data"]
            
            name = data["name"]
            employee_id = data["employee_id"]
            return jsonify({"name": name, "employee_id":employee_id})
        
        else:
            return jsonify({"message": "No data provided"})
    except Exception as e:
        return jsonify({"message": "Invalid data provided"})

if __name__ == "__main__":
    app.run(debug=True)