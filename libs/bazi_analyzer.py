from enum import Enum
from typing import List, Dict, Tuple

class HiddenStemStrength(Enum):
    STRONG = 1.0  # 最强,单藏或建禄
    MEDIUM = 0.6  # 中等,三藏第二个  
    WEAK = 0.3    # 最弱,三藏最后一个

class BaziHiddenStem:
    # 天干五行对应表
    HEAVENLY_STEM_FIVE_ELEMENTS: Dict[str, str] = {
        "甲": "木", "乙": "木",
        "丙": "火", "丁": "火", 
        "戊": "土", "己": "土",
        "庚": "金", "辛": "金",
        "壬": "水", "癸": "水"
    }
    
    # 地支藏干对应表,每个地支对应的天干列表按照力量强弱排序
    EARTHLY_BRANCH_HIDDEN_STEMS: Dict[str, List[str]] = {
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
    EARTHLY_BRANCH_RULING_STEM: Dict[str, str] = {
        "子": "癸", "丑": "己", "寅": "甲",
        "卯": "乙", "辰": "戊", "巳": "丙",
        "午": "丁", "未": "己", "申": "庚",
        "酉": "辛", "戌": "戊", "亥": "壬"
    }

    @staticmethod
    def get_stem_with_element(stem: str) -> str:
        """获取带五行的天干名称"""
        element = BaziHiddenStem.HEAVENLY_STEM_FIVE_ELEMENTS.get(stem, "")
        return f"{stem}{element}" if element else stem

    @staticmethod
    def get_hidden_stems(branch: str) -> List[str]:
        """获取地支所藏天干列表"""
        return BaziHiddenStem.EARTHLY_BRANCH_HIDDEN_STEMS.get(branch, [])

    @staticmethod
    def get_hidden_stems_with_strength(branch: str) -> List[Tuple[str, float]]:
        """获取地支所藏天干及其强度"""
        hidden_stems = BaziHiddenStem.EARTHLY_BRANCH_HIDDEN_STEMS.get(branch, [])
        result = []
        
        if not hidden_stems:
            return result

        # 确定每个藏干的强度
        if len(hidden_stems) == 1:
            # 单藏的情况
            result.append((hidden_stems[0], HiddenStemStrength.STRONG.value))
        elif len(hidden_stems) == 2:
            # 两藏的情况,都按中等强度
            for stem in hidden_stems:
                result.append((stem, HiddenStemStrength.MEDIUM.value))
        else:
            # 三藏的情况,按强中弱排序
            strengths = [HiddenStemStrength.STRONG.value, 
                        HiddenStemStrength.MEDIUM.value, 
                        HiddenStemStrength.WEAK.value]
            for stem, strength in zip(hidden_stems, strengths):
                result.append((stem, strength))

        # 如果是建禄,提升强度
        ruling_stem = BaziHiddenStem.EARTHLY_BRANCH_RULING_STEM.get(branch)
        if ruling_stem:
            result = [(stem, strength if stem != ruling_stem else HiddenStemStrength.STRONG.value)
                     for stem, strength in result]

        return result

    @staticmethod
    def analyze_pillar_hidden_stems(branch: str) -> Dict[str, any]:
        """分析单柱藏干"""
        hidden_stems = BaziHiddenStem.get_hidden_stems_with_strength(branch)
        details = []
        
        for stem, strength in hidden_stems:
            details.append({
                "stem": BaziHiddenStem.get_stem_with_element(stem),
                "strength": strength,
                "is_ruling": stem == BaziHiddenStem.EARTHLY_BRANCH_RULING_STEM.get(branch)
            })
        
        return {
            "branch": branch,
            "hidden_stems": [(BaziHiddenStem.get_stem_with_element(stem), strength) 
                            for stem, strength in hidden_stems],
            "count": len(hidden_stems),
            "has_ruling_stem": branch in BaziHiddenStem.EARTHLY_BRANCH_RULING_STEM,
            "ruling_stem": BaziHiddenStem.get_stem_with_element(BaziHiddenStem.EARTHLY_BRANCH_RULING_STEM.get(branch)) 
                          if branch in BaziHiddenStem.EARTHLY_BRANCH_RULING_STEM else None,
            "details": details
        }

class BaziPillar:
    def __init__(self, heavenly_stem: str, earthly_branch: str):
        self.heavenly_stem = heavenly_stem
        self.earthly_branch = earthly_branch
        self.hidden_stem_analyzer = BaziHiddenStem()
    
    def analyze(self) -> Dict[str, any]:
        """分析单柱天干地支与藏干"""
        return {
            "heavenly_stem": BaziHiddenStem.get_stem_with_element(self.heavenly_stem),
            "earthly_branch": self.earthly_branch,
            "hidden_stem_analysis": self.hidden_stem_analyzer.analyze_pillar_hidden_stems(self.earthly_branch)
        }