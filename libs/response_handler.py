from typing import Dict, Any, List

class ResponseHandler:
    def __init__(self, raw_data: Dict[str, Any]):
        self.raw_data = raw_data

    def process(self) -> Dict[str, Any]:
        """处理并重组响应数据"""
        return {
            # 1. 基础信息
            "basic_info": self._process_basic_info(),
            
            # 2. 八字信息
            "bazi_structure": self._process_bazi_structure(),
            
            # 3. 五行分析
            "five_elements": self._process_five_elements(),
            
            # 4. 运势周期
            "life_cycles": self._process_life_cycles(),

            # 5. 神煞信息
            "destiny_indicators": self._process_destiny_indicators()
        }
    
    def _process_basic_info(self) -> Dict[str, Any]:
        """处理基础信息"""
        calendar_analysis = self.raw_data.get("calendar_analysis", {})
        return {
            "birth_time": self.raw_data.get("birth_date", ""),
            "birth_place": self.raw_data.get("birth_at", ""),
            "zodiac": calendar_analysis.get("sx", ""),
            "constellation": calendar_analysis.get("xz", "")
        }

    def _process_bazi_structure(self) -> Dict[str, Any]:
        """处理八字结构"""
        bazi = self.raw_data.get("calendar_analysis", {}).get("bazi", [])
        return {
            "year": f"{bazi[0][0]}{bazi[0][1]}" if len(bazi) > 0 else "",
            "month": f"{bazi[1][0]}{bazi[1][1]}" if len(bazi) > 1 else "",
            "day": f"{bazi[2][0]}{bazi[2][1]}" if len(bazi) > 2 else "",
            "hour": f"{bazi[3][0]}{bazi[3][1]}" if len(bazi) > 3 else ""
        }

    def _process_five_elements(self) -> Dict[str, Any]:
        """处理五行分析"""
        wx_fen = self.raw_data.get("calendar_analysis", {}).get("wx_fen", [])
        return {
            "metal": wx_fen[0] if len(wx_fen) > 0 else 0,
            "wood": wx_fen[1] if len(wx_fen) > 1 else 0,
            "water": wx_fen[2] if len(wx_fen) > 2 else 0,
            "fire": wx_fen[3] if len(wx_fen) > 3 else 0,
            "earth": wx_fen[4] if len(wx_fen) > 4 else 0
        }

    def _process_life_cycles(self) -> Dict[str, Any]:
        """处理运势周期"""
        calendar_analysis = self.raw_data.get("calendar_analysis", {})
        return {
            "current_phase": calendar_analysis.get("start_desc", ""),
            "cycles": self._process_big_fate()
        }

    def _process_big_fate(self) -> List[Dict[str, Any]]:
        """处理大运数据"""
        cycles = []
        calendar_analysis = self.raw_data.get("calendar_analysis", {})
        big_start_time = calendar_analysis.get("big_start_time", [])
        big = calendar_analysis.get("big", [])
        big_cs = calendar_analysis.get("big_cs", [])

        for i, start_time in enumerate(big_start_time):
            if i < len(big) and i < len(big_cs):
                cycle = {
                    "period": big[i],
                    "start_time": f"{start_time[0]}-{start_time[1]:02d}-{start_time[2]:02d}",
                    "status": big_cs[i].get("char", "")
                }
                cycles.append(cycle)
        return cycles

    def _process_destiny_indicators(self) -> Dict[str, Any]:
        """处理神煞信息"""
        calendar_analysis = self.raw_data.get("calendar_analysis", {})
        return {
            "time_spirit": calendar_analysis.get("sc", {}).get("char", ""),
            "stars": self._process_stars()
        }

    def _process_stars(self) -> List[Dict[str, Any]]:
        """处理神煞星耀信息"""
        stars = []
        lunar_analysis = self.raw_data.get("lunar_analysis", {})
        pillars = lunar_analysis.get("pillars", {})

        # 处理年柱星耀
        if "year" in pillars and "stars" in pillars["year"]:
            for star in pillars["year"]["stars"]:
                stars.append({
                    "name": star.get("star_name", ""),
                    "type": star.get("star_type", "")
                })

        # 处理日柱星耀
        if "day" in pillars and "stars" in pillars["day"]:
            for star in pillars["day"]["stars"]:
                stars.append({
                    "name": star.get("star_name", ""),
                    "type": star.get("star_type", "")
                })

        return stars

def format_response(raw_data: Dict[str, Any]) -> Dict[str, Any]:
    """格式化响应数据的入口函数"""
    print(f"format_response called with raw_data: {raw_data}")  
    handler = ResponseHandler(raw_data)
    return handler.process()