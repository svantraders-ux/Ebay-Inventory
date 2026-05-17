from flask import Flask, request, jsonify
import hashlib

app = Flask(__name__)

VERIFICATION_TOKEN = "asdfghjjllpoiuytrdcffgghjklpoiygg"

ENDPOINT = "https://ebay-inventory-webhook.onrender.com"

@app.route("/", methods=["GET", "POST"])
def webhook():

    challenge_code = request.args.get("challenge_code")

    if challenge_code:
        hash_input = challenge_code + VERIFICATION_TOKEN + ENDPOINT

        challenge_response = hashlib.sha256(
            hash_input.encode()
        ).hexdigest()

        return jsonify({
            "challengeResponse": challenge_response
        })

    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
