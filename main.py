from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

sample_trends = {
    "اليمن": ["ارتفاع أسعار النفط", "مباراة المنتخب اليمني", "إطلاق مبادرة تعليمية"],
    "السعودية": ["موسم الرياض", "ترند تيك توك", "السيارات الكهربائية"],
    "مصر": ["مسلسل الاختيار", "قرارات اقتصادية", "الأهلي والزمالك"],
    "أمريكا": ["انتخابات الرئاسة", "آيفون 15", "فضيحة سياسية"],
    "عالمي": ["كريستيانو رونالدو", "ظاهرة نادرة", "ChatGPT"]
}

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    country = data.get("country", "عالمي")
    trend = random.choice(sample_trends.get(country, sample_trends["عالمي"]))
    return jsonify({
        "trend": trend,
        "title": f"🔥 عاجل | {trend[:30]}",
        "description": f"في هذا الفيديو نغطي أهم تفاصيل '{trend}' وكيف أثار تفاعلًا واسعًا."
    })

@app.route("/", methods=["GET"])
def home():
    return "✅ TrendStormer API يعمل!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
