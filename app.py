from flask import Flask, request, jsonify
from bazi import BaZi
from datetime import datetime

app = Flask(__name__)

@app.route('/bazi', methods=['GET'])
def get_bazi():
    # 获取时间戳参数
    timestamp = request.args.get('timestamp', type=float)
    if not timestamp:
        return jsonify({"error": "Missing timestamp parameter"}), 400

    # 将时间戳转换为日期时间对象
    dt = datetime.fromtimestamp(timestamp)

    # 计算八字
    bazi = BaZi.from_datetime(dt)

    # 构建返回结果
    result = {
        "Main stars (主星)": bazi.main_stars,
        "Heaven stems (天干)": bazi.heaven_stems,
        "Earth branches (地支)": bazi.earth_branches,
        "Hidden stems (藏干)": bazi.hidden_stems,
        "Secondary stars (副星)": bazi.secondary_stars,
        "神煞": bazi.shen_sha
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)