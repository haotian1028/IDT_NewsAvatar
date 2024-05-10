from flask import Flask, request, jsonify
from NewsAvatar import NewsAvatar


app = Flask(__name__)

@app.route('/api/getAvatar', methods=['POST'])
def calculate():

    data = request.json

    language ="IT"

    if 'URL' not in data or 'website' not in data:
        return jsonify({'error': 'Missing parameters'}), 400
    if 'language' in data:
        language=data['language']

    URL = data['URL']
    website = data['website']

    result= NewsAvatar(URL,website,language)

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
