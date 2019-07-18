import tempfile
from typing import NamedTuple

from flask import Flask, request, jsonify, make_response

from ripper import parse_file, parse_metadata

app = Flask(__name__)


class Response(NamedTuple):
    message: str
    code: int
    data: object


@app.route("/", methods=['POST'])
def hello():
    upload = request.files['file']

    filename = upload.filename.split('.')
    suffix = filename[1] if len(filename) > 0 else ".invalid"

    temp = tempfile.NamedTemporaryFile(suffix=suffix, delete=True)

    upload.save(temp.name)

    df, meta, err = parse_file(temp.name)

    if err:
        e = Response(f"Uploaded file \"{upload.filename}\" is not supported at this time.", 400, None)._asdict()
        return make_response(jsonify(e), 400)

    data = parse_metadata(meta)
    res = Response(f"{upload.filename} parsed successfully!", 200, data)._asdict()

    return jsonify(res)
