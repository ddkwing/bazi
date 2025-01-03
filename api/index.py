from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs, urlparse
from lunar_python import Solar
import json
from libs.chinese_calendar import ChineseCalendar
from libs.response_handler import format_response

def parse_birth_date(birth_date: str) -> tuple:
    """解析生日字符串"""
    year = int(birth_date[:4])
    month = int(birth_date[4:6])
    day = int(birth_date[6:8])
    hour = int(birth_date[8:10])
    minute = int(birth_date[10:12])
    return year, month, day, hour, minute

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        """处理GET请求"""
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

        try:
            # 解析请求参数
            parsed_path = urlparse(self.path)
            query_params = parse_qs(parsed_path.query)
            
            birth_date = query_params.get('birth_date', [''])[0]
            birth_at = query_params.get('birth_at', [''])[0]
            gender = query_params.get('gender', ['1'])[0]
            
            if not birth_date or len(birth_date) != 12:
                response = {"error": "Invalid birth_date format. Expected: YYYYMMDDhhmm"}
                self.wfile.write(json.dumps(response).encode())
                return

            # 生成原始数据
            year, month, day, hour, minute = parse_birth_date(birth_date)
            solar = Solar.fromYmdHms(year, month, day, hour, minute, 0)
            lunar = solar.getLunar()
            eight_char = lunar.getEightChar()
            
            analyzer = BaziAnalyzer(eight_char)
            lunar_analysis = analyzer.analyze()
            
            calendar = ChineseCalendar()
            calendar_analysis = calendar.GetInfo(
                int(gender),
                year, month, day,
                hour, minute, 0
            )
            
            # 构建原始响应
            raw_response = {
                "birth_date": birth_date,
                "birth_at": birth_at,
                "lunar_analysis": lunar_analysis,
                "calendar_analysis": calendar_analysis
            }
            
            # 使用新的响应处理器格式化数据
            formatted_response = format_response(raw_response)
            
            self.wfile.write(json.dumps(formatted_response, ensure_ascii=False).encode('utf-8'))
            
        except Exception as e:
            response = {"error": str(e)}
            self.wfile.write(json.dumps(response).encode())

    def do_OPTIONS(self):
        """处理OPTIONS请求"""
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()