from enum import Enum
from typing import List, Dict, Tuple

class CangGanStrength(Enum):
    STRONG = 1.0  # 最强，单藏或建禄
    MEDIUM = 0.6  # 中等，三藏第二个
    WEAK = 0.3    # 最弱，三藏最后一个

class CangGan:
    # 地支藏干对应表，每个地支对应的天干列表按照力量强弱排序
    DIZHI_CANGGAN: Dict[str, List[str]] = {
        "子": ["癸"],           # 单藏癸水
        "丑": ["己", "癸", "辛"], # 建禄己土藏得最强
        "寅": ["甲", "丙", "戊"],
        "卯": ["乙"],           
        "辰": ["戊", "乙", "癸"],
        "巳": ["丙", "戊", "庚"],
        "午": ["丁", "己"],      
        "未": ["己", "丁", "乙"],
        "申": ["庚", "壬", "戊"],
        "酉": ["辛"],           
        "戌": ["戊", "辛", "丁"],
        "亥": ["壬", "甲"]
    }

    # 地支建禄天干对应
    DIZHI_JIANLU: Dict[str, str] = {
        "子": "癸", "丑": "己", "寅": "甲",
        "卯": "乙", "辰": "戊", "巳": "丙",
        "午": "丁", "未": "己", "申": "庚",
        "酉": "辛", "戌": "戊", "亥": "壬"
    }

    @staticmethod
    def get_canggan_list(dizhi: str) -> List[str]:
        """获取地支所藏天干列表"""
        return CangGan.DIZHI_CANGGAN.get(dizhi, [])

    @staticmethod
    def get_canggan_with_strength(dizhi: str) -> List[Tuple[str, float]]:
        """获取地支所藏天干及其强度"""
        canggan_list = CangGan.DIZHI_CANGGAN.get(dizhi, [])
        result = []
        
        if not canggan_list:
            return result

        # 确定每个藏干的强度
        if len(canggan_list) == 1:
            # 单藏的情况
            result.append((canggan_list[0], CangGanStrength.STRONG.value))
        elif len(canggan_list) == 2:
            # 两藏的情况，都按中等强度
            for gan in canggan_list:
                result.append((gan, CangGanStrength.MEDIUM.value))
        else:
            # 三藏的情况，按强中弱排序
            strengths = [CangGanStrength.STRONG.value, 
                        CangGanStrength.MEDIUM.value, 
                        CangGanStrength.WEAK.value]
            for gan, strength in zip(canggan_list, strengths):
                result.append((gan, strength))

        # 如果是建禄，提升强度
        jianlu_gan = CangGan.DIZHI_JIANLU.get(dizhi)
        if jianlu_gan:
            result = [(gan, strength if gan != jianlu_gan else CangGanStrength.STRONG.value)
                     for gan, strength in result]

        return result

    @staticmethod
    def analyze_pillar_canggan(dizhi: str) -> Dict[str, any]:
        """分析单柱藏干"""
        canggan_list = CangGan.get_canggan_with_strength(dizhi)
        details = []
        
        for gan, strength in canggan_list:
            details.append({
                "gan": gan,
                "strength": strength,
                "is_jianlu": gan == CangGan.DIZHI_JIANLU.get(dizhi)
            })
        
        return {
            "dizhi": dizhi,
            "canggan_list": canggan_list,
            "count": len(canggan_list),
            "has_jianlu": dizhi in CangGan.DIZHI_JIANLU,
            "jianlu_gan": CangGan.DIZHI_JIANLU.get(dizhi),
            "details": details
        }

class BaziPillar:
    def __init__(self, tiangan: str, dizhi: str):
        self.tiangan = tiangan
        self.dizhi = dizhi
        self.canggan = CangGan()
    
    def analyze(self) -> Dict[str, any]:
        """分析单柱天干地支与藏干"""
        return {
            "tiangan": self.tiangan,
            "dizhi": self.dizhi,
            "canggan_analysis": self.canggan.analyze_pillar_canggan(self.dizhi)
        }