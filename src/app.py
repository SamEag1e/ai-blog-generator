import logging

from flask import Flask, request, jsonify

from core.ai_generator import generate_blog_post, generate_mock_blog_post
from core.seo_fetcher import get_keyword_data_mock
from config.cfg import settings

DEBUG = settings.DEBUG
MOCK_DATA = settings.MOCK_DATA
logger = logging.getLogger(__name__)
app = Flask(__name__)


@app.route("/generate")
def generate():
    keyword = request.args.get("keyword")
    if not keyword:
        return jsonify({"error": "Missing 'keyword' parameter"}), 400

    try:
        post = (
            generate_mock_blog_post(keyword)
            if MOCK_DATA
            else generate_blog_post(keyword, api_key=settings.OPEN_AI_API_KEY)
        )

        return jsonify({"post": post})

    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400

    except Exception:
        logger.exception("Unexpected error during blog post generation")
        raise


@app.route("/seo-data")
def seo_data():
    keyword = request.args.get("keyword")
    if not keyword:
        return jsonify({"error": "Missing 'keyword' parameter"}), 400

    return jsonify({"result": get_keyword_data_mock(keyword)})


if __name__ == "__main__":
    app.run(debug=DEBUG)
