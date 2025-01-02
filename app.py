from flask import Flask, request, jsonify
from lunar_python import Solar, Lunar 

app = Flask(__name__)

@app.route('/bazi', methods=['GET'])
def calculate_bazi():
    # 获取参数
    birth_date = request.args.get('birth_date', '')
    birth_at = request.args.get('birth_at', '')
    
    # 验证参数
    if not birth_date or len(birth_date) != 12:
        return jsonify({"error": "Invalid birth_date format. Expected: YYYYMMDDhhmm"}), 400
        
    try:
        year = int(birth_date[:4])
        month = int(birth_date[4:6]) 
        day = int(birth_date[6:8])
        hour = int(birth_date[8:10])
        minute = int(birth_date[10:12])
        
        # 使用阳历创建对象
        solar = Solar.fromYmdHms(year, month, day, hour, minute, 0)
        lunar = solar.getLunar()
        
        # 获取八字
        ba = lunar.getEightChar()
        
        return jsonify({
            "birth_date": birth_date,
            "birth_at": birth_at,
            "bazi": {
                "year": {
                    "tiangan": ba.getYearGan(),
                    "dizhi": ba.getYearZhi()
                },
                "month": {
                    "tiangan": ba.getMonthGan(),
                    "dizhi": ba.getMonthZhi() 
                },
                "day": {
                    "tiangan": ba.getDayGan(),
                    "dizhi": ba.getDayZhi()
                },
                "time": {
                    "tiangan": ba.getTimeGan(),
                    "dizhi": ba.getTimeZhi()
                }
            }
        })
        
    except ValueError:
        return jsonify({"error": "Invalid date/time values"}), 400

if __name__ == '__main__':
    app.run(debug=True)