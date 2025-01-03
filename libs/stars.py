from libs.start_check import StarsCheck
from libs.chinese_calendar import ChineseCalendar

class Stars:
    def __init__(self):
        self.star_name = [
            ['kong_wang', '空亡'],
            ['tian_yi', '天乙'],
            ['tai_ji', '太极'],
            ['tian_yi2', '天医'],
            ['tian_de', '天德'],
            ['yue_de', '月德'],
            ['lu_shen', '禄神'],
            ['yang_ren', '羊刃'],
            ['gu_luan', '孤鸾'],
            ['san_qi', '三奇'],
            ['tian_xie', '天赦'],
            ['de_xiu', '德秀'],
            ['kui_gang', '魁罡'],
            ['jing_shen', '金神'],
            ['tian_luo', '天罗'],
            ['di_wang', '地网'],
            ['wen_chang', '文昌'],
            ['jin_yu', '金舆'],
            ['fu_xing', '福星'],
            ['guo_yin', '国印'],
            ['tian_chu', '天厨'],
            ['xue_tang', '学堂'],
            ['hong_yang', '红艳'],
            ['liu_xia', '流霞'],
            ['jiang_xing', '将星'],
            ['hua_gai', '华盖'],
            ['yi_ma', '驿马'],
            ['jie_sha', '劫煞'],
            ['wang_shen', '亡神'],
            ['yuan_chen', '元辰(大耗)'],
            ['gu_chen', '孤辰'],
            ['gua_su', '寡宿'],
            ['zhai_sha', '灾煞'],
            ['liu_e', '六厄'],
            ['gou_sha', '勾煞'],
            ['jiao_sha', '绞煞'],
            ['tong_zi', '童子'],
            ['ci_guan', '词馆'],
            ['hong_lian', '红鸾'],
            ['tian_xi', '天喜'],
            ['tao_hua', '桃花'],
            ['gan_lu', '干禄'],
            ['shi_ling', '十灵'],
            ['shi_e', '十恶大败']
        ]

    def get_stars(self, info):
        star_checker = StarsCheck()
        star = [[] for _ in range(4)]  # year, month, day, hour
        
        for key, value in enumerate(self.star_name):
            method = getattr(star_checker, value[0])
            method(info, star, key, value)
            
        info['star'] = star
        return info

    def get_info(self, gender, year, month, day, hour, minute=0, second=0):
        """Get information based on Gregorian calendar
        
        Args:
            gender: 0 for male, 1 for female
            year: year in Gregorian calendar
            month: month (1-12)
            day: day (1-31)
            hour: hour (0-23)
            minute: minute (0-59), defaults to 0
            second: second (0-59), defaults to 0
            
        Returns:
            dict: Information containing stars and other data
        """
        calendar = ChineseCalendar()
        info = calendar.get_info(gender, year, month, day, hour, minute, second)
        return self.get_stars(info)