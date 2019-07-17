import tempfile

from flask import Flask, request, jsonify

from ripper import parse_file, parse_metadata

app = Flask(__name__)


@app.route("/", methods=['POST'])
def hello():
    upload = request.files['file']

    filename = upload.filename.split('.')
    suffix = filename[1] if len(filename) > 0 else ".invalid"

    temp = tempfile.NamedTemporaryFile(suffix=suffix, delete=True)

    upload.save(temp.name)

    df, meta = parse_file(temp.name)
    res = parse_metadata(meta)

    return jsonify(res)
