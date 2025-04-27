from flask import Flask, jsonify, request
from url_generate import process_course_name

app = Flask(__name__)


@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    course_name = data.get('course_name', '')
    result = process_course_name(course_name)
    return jsonify(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    