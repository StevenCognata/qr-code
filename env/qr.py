from flask import Flask, request, jsonify
import qrcode
from io import BytesIO

app = Flask(__name__)

@app.route("/qr", methods=['GET'])
def generate_qr_code():
    url = request.args.get("url")
    if not url:
        return jsonify({"error": "Missing URL parameter"}), 400
    
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    buffer = BytesIO()
    img.save(buffer, "PNG")
    buffer.seek(0)

    return buffer.getvalue(), 200, {'Content-Type': 'image/png', 'Content-Disposition': 'attachment;filename=qr.png'}


if __name__ == '__main__':
    app.run(debug=True)
