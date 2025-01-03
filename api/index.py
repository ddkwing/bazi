from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs, urlparse
from lunar_python import Solar
from typing import Dict, Any
import json

from libs.canggan import CangGan, BaziPillar

def parse_birth_date(birth_date: str) -> tuple:
    """解析生日字符串"""
    year = int(birth_date[:4])
    month = int(birth_date[4:6])
    day = int(birth_date[6:8])
    hour = int(birth_date[8:10])
    minute = int(birth_date[10:12])
    return year, month, day, hour, minute

class BaziAnalyzer:
    def __init__(self, ba):
        """初始化八字分析器"""
        self.ba = ba
        # 初始化四柱
        self.year_pillar = BaziPillar(ba.getYearGan(), ba.getYearZhi())
        self.month_pillar = BaziPillar(ba.getMonthGan(), ba.getMonthZhi())
        self.day_pillar = BaziPillar(ba.getDayGan(), ba.getDayZhi())
        self.hour_pillar = BaziPillar(ba.getTimeGan(), ba.getTimeZhi())

    def analyze(self) -> Dict[str, Any]:
        """进行完整八字分析"""
        return {
            "pillars": {
                "year": self.year_pillar.analyze(),
                "month": self.month_pillar.analyze(),
                "day": self.day_pillar.analyze(),
                "hour": self.hour_pillar.analyze()
            }
        }

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
            
            # 验证输入
            if not birth_date or len(birth_date) != 12:
                response = {"error": "Invalid birth_date format. Expected: YYYYMMDDhhmm"}
                self.wfile.write(json.dumps(response).encode())
                return

            # 解析日期并创建八字
            year, month, day, hour, minute = parse_birth_date(birth_date)
            solar = Solar.fromYmdHms(year, month, day, hour, minute, 0)
            lunar = solar.getLunar()
            ba = lunar.getEightChar()
            
            # 进行八字分析
            analyzer = BaziAnalyzer(ba)
            analysis = analyzer.analyze()
            
            # 构建响应
            response = {
                "birth_date": birth_date,
                "birth_at": birth_at,
                "analysis": analysis
            }
            
            self.wfile.write(json.dumps(response, ensure_ascii=False).encode('utf-8'))
            
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