from enum import Enum
from typing import List, Dict, Tuple, Optional

class HiddenStemStrength(Enum):
    STRONG = 1.0  # 最强,单藏或建禄
    MEDIUM = 0.6  # 中等,三藏第二个  
    WEAK = 0.3    # 最弱,三藏最后一个

class StarType(Enum):
    MAIN = "主星"    # 主星
    SECONDARY = "副星" # 副星

class BaziStar:
    # 天干生克关系的主星映射
    MAIN_STAR_MAP: Dict[str, Dict[str, str]] = {
        # 日干对其他干的主星关系
        "甲": {"己": "正财", "乙": None, "丙": None, "丁": None, "戊": None, "庚": None, "辛": None, "壬": None, "癸": None},
        "乙": {"己": "正财", "甲": None, "丙": None, "丁": None, "戊": None, "庚": None, "辛": None, "壬": None, "癸": None},
        "丙": {"辛": "元男", "甲": None, "乙": None, "丁": None, "戊": None, "己": None, "庚": None, "壬": None, "癸": None},
        "丁": {"辛": "元男", "甲": None, "乙": None, "丙": None, "戊": None, "己": None, "庚": None, "壬": None, "癸": None},
        "戊": {"乙": "七杀", "甲": None, "丙": None, "丁": None, "己": None, "庚": None, "辛": None, "壬": None, "癸": None},
        "己": {"乙": "七杀", "甲": None, "丙": None, "丁": None, "戊": None, "庚": None, "辛": None, "壬": None, "癸": None},
        "庚": {"丁": "正财", "甲": None, "乙": None, "丙": None, "戊": None, "己": None, "辛": None, "壬": None, "癸": None},
        "辛": {"丁": "正财", "甲": None, "乙": None, "丙": None, "戊": None, "己": None, "庚": None, "壬": None, "癸": None},
        "壬": {"己": "七杀", "甲": None, "乙": None, "丙": None, "丁": None, "戊": None, "庚": None, "辛": None, "癸": None},
        "癸": {"己": "七杀", "甲": None, "乙": None, "丙": None, "丁": None, "戊": None, "庚": None, "辛": None, "壬": None}
    }
    
    # 天干生克关系的副星映射
    SECONDARY_STAR_MAP: Dict[str, Dict[str, str]] = {
        "甲": {"甲": "比肩", "丙": "伤官", "戊": "正印", "庚": "劫财", "壬": "正官"},
        "乙": {"乙": "比肩", "丁": "伤官", "己": "正印", "辛": "劫财", "癸": "正官"},
        "丙": {"丙": "比肩", "戊": "伤官", "庚": "正印", "壬": "劫财", "甲": "正官"},
        "丁": {"丁": "比肩", "己": "伤官", "辛": "正印", "癸": "劫财", "乙": "正官"},
        "戊": {"戊": "比肩", "庚": "伤官", "壬": "正印", "甲": "劫财", "丙": "正官"},
        "己": {"己": "比肩", "辛": "伤官", "癸": "正印", "乙": "劫财", "丁": "正官"},
        "庚": {"庚": "比肩", "壬": "伤官", "甲": "正印", "丙": "劫财", "戊": "正官"},
        "辛": {"辛": "比肩", "癸": "伤官", "乙": "正印", "丁": "劫财", "己": "正官"},
        "壬": {"壬": "比肩", "甲": "伤官", "丙": "正印", "戊": "劫财", "庚": "正官"},
        "癸": {"癸": "比肩", "乙": "伤官", "丁": "正印", "己": "劫财", "辛": "正官"}
    }

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
            result.append((hidden_stems[0], HiddenStemStrength.STRONG.value))
        elif len(hidden_stems) == 2:
            for stem in hidden_stems:
                result.append((stem, HiddenStemStrength.MEDIUM.value))
        else:
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
    
    def get_main_star(self, target_stem: str) -> Optional[Dict[str, str]]:
        """获取主星"""
        if (self.heavenly_stem in BaziStar.MAIN_STAR_MAP and 
            target_stem in BaziStar.MAIN_STAR_MAP[self.heavenly_stem] and 
            BaziStar.MAIN_STAR_MAP[self.heavenly_stem][target_stem]):
            return {
                "star_name": BaziStar.MAIN_STAR_MAP[self.heavenly_stem][target_stem],
                "star_type": StarType.MAIN.value,
                "from_stem": self.heavenly_stem,
                "to_stem": target_stem
            }
        return None
    
    def get_secondary_stars(self, target_stem: str) -> List[Dict[str, str]]:
        """获取副星"""
        secondary_stars = []
        if (self.heavenly_stem in BaziStar.SECONDARY_STAR_MAP and 
            target_stem in BaziStar.SECONDARY_STAR_MAP[self.heavenly_stem]):
            secondary_stars.append({
                "star_name": BaziStar.SECONDARY_STAR_MAP[self.heavenly_stem][target_stem],
                "star_type": StarType.SECONDARY.value,
                "from_stem": self.heavenly_stem,
                "to_stem": target_stem
            })
        return secondary_stars
    
    def analyze(self) -> Dict[str, any]:
        """分析单柱天干地支与藏干"""
        # 获取基本信息
        basic_analysis = {
            "heavenly_stem": BaziHiddenStem.get_stem_with_element(self.heavenly_stem),
            "earthly_branch": self.earthly_branch,
            "hidden_stem_analysis": self.hidden_stem_analyzer.analyze_pillar_hidden_stems(self.earthly_branch)
        }
        
        # 分析主副星
        stars = []
        
        # 检查主星
        main_star = self.get_main_star(self.heavenly_stem)
        if main_star:
            stars.append(main_star)
        
        # 检查副星
        secondary_stars = self.get_secondary_stars(self.heavenly_stem)
        stars.extend(secondary_stars)
        
        # 对藏干检查主副星
        hidden_stems = self.hidden_stem_analyzer.get_hidden_stems(self.earthly_branch)
        for hidden_stem in hidden_stems:
            # 只添加副星，主星已经确定
            stars.extend(self.get_secondary_stars(hidden_stem))
        
        basic_analysis["stars"] = stars
        return basic_analysis