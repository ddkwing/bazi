from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs, urlparse
from lunar_python import Solar
import json

def parse_birth_date(birth_date):
    year = int(birth_date[:4])
    month = int(birth_date[4:6]) 
    day = int(birth_date[6:8])
    hour = int(birth_date[8:10])
    minute = int(birth_date[10:12])
    return year, month, day, hour, minute

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 设置CORS头
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

        try:
            # 解析URL参数
            parsed_path = urlparse(self.path)
            query_params = parse_qs(parsed_path.query)
            
            birth_date = query_params.get('birth_date', [''])[0]
            birth_at = query_params.get('birth_at', [''])[0]
            
            # 验证输入
            if not birth_date or len(birth_date) != 12:
                response = {"error": "Invalid birth_date format. Expected: YYYYMMDDhhmm"}
                self.wfile.write(json.dumps(response).encode())
                return

            # 解析日期
            year, month, day, hour, minute = parse_birth_date(birth_date)
            
            # 使用阳历创建对象
            solar = Solar.fromYmdHms(year, month, day, hour, minute, 0)
            lunar = solar.getLunar()
            
            # 获取八字
            ba = lunar.getEightChar()
            
            response = {
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
            }
            
            self.wfile.write(json.dumps(response, ensure_ascii=False).encode('utf-8'))
            
        except Exception as e:
            response = {"error": str(e)}
            self.wfile.write(json.dumps(response).encode())

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()