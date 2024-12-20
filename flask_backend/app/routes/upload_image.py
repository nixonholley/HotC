from flask import Flask, request, jsonify, Blueprint, current_app

upload_image_bp = Blueprint('upload_image', __name__)

@upload_image_bp.route('/upload', methods=['POST'])
def upload_image():
    pass
    # if 'image' not in request.files:
    #     return jsonify({"error"})
    # file = request.files['image']
    # if file.filename == '':
    #     return jsonify({"error": "No selected file"}), 400

    # # Mock OCR result
    # ocr_result = {
    #     "card_name": "Blue-Eyes White Dragon",
    #     "rarity": "Ultra Rare",
    #     "value": "$15.00"
    # }

    # # Save the card to the database
    # db = get_db()
    # query = """
    # INSERT INTO cards (card_name, rarity, value)
    # VALUES (%s, %s, %s) RETURNING id;
    # """
    # card_id = db.execute(query, (ocr_result['card_name'], ocr_result['rarity'], ocr_result['value'])).fetchone()
    # db.commit()

    # return jsonify({"message": "Image processed", "card_id": card_id, "data": ocr_result}), 200