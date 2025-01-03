from math import floor, sin, cos, pi, atan, sqrt, tan
from typing import List, Tuple, Dict, Optional, Union
from libs.calendar_core import CalendarCore
class ChineseCalendar(CalendarCore):
    def __init__(self):
        super().__init__()

    def TrueNewMoon(self, k: int) -> float:
        jdt = 2451550.09765 + k * self.synmonth
        t = (jdt - 2451545) / 36525
        t2 = t * t
        t3 = t2 * t
        t4 = t3 * t
        
        pt = jdt + 0.0001337 * t2 - 0.00000015 * t3 + 0.00000000073 * t4
        m = 2.5534 + 29.10535669 * k - 0.0000218 * t2 - 0.00000011 * t3
        mprime = 201.5643 + 385.81693528 * k + 0.0107438 * t2 + 0.00001239 * t3 - 0.000000058 * t4
        f = 160.7108 + 390.67050274 * k - 0.0016341 * t2 - 0.00000227 * t3 + 0.000000011 * t4
        omega = 124.7746 - 1.5637558 * k + 0.0020691 * t2 + 0.00000215 * t3
        es = 1 - 0.002516 * t - 0.0000074 * t2
        
        apt1 = -0.4072 * sin(pi / 180 * mprime)
        apt1 += 0.17241 * es * sin(pi / 180 * m)
        apt1 += 0.01608 * sin(pi / 180 * 2 * mprime)
        apt1 += 0.01039 * sin(pi / 180 * 2 * f)
        apt1 += 0.00739 * es * sin(pi / 180 * (mprime - m))
        apt1 -= 0.00514 * es * sin(pi / 180 * (mprime + m))
        apt1 += 0.00208 * es * es * sin(pi / 180 * (2 * m))
        apt1 -= 0.00111 * sin(pi / 180 * (mprime - 2 * f))
        apt1 -= 0.00057 * sin(pi / 180 * (mprime + 2 * f))
        apt1 += 0.00056 * es * sin(pi / 180 * (2 * mprime + m))
        apt1 -= 0.00042 * sin(pi / 180 * 3 * mprime)
        apt1 += 0.00042 * es * sin(pi / 180 * (m + 2 * f))
        apt1 += 0.00038 * es * sin(pi / 180 * (m - 2 * f))
        apt1 -= 0.00024 * es * sin(pi / 180 * (2 * mprime - m))
        apt1 -= 0.00017 * sin(pi / 180 * omega)
        apt1 -= 0.00007 * sin(pi / 180 * (mprime + 2 * m))
        apt1 += 0.00004 * sin(pi / 180 * (2 * mprime - 2 * f))
        apt1 += 0.00004 * sin(pi / 180 * (3 * m))
        apt1 += 0.00003 * sin(pi / 180 * (mprime + m - 2 * f))
        apt1 += 0.00003 * sin(pi / 180 * (2 * mprime + 2 * f))
        apt1 -= 0.00003 * sin(pi / 180 * (mprime + m + 2 * f))
        apt1 += 0.00003 * sin(pi / 180 * (mprime - m + 2 * f))
        apt1 -= 0.00002 * sin(pi / 180 * (mprime - m - 2 * f))
        apt1 -= 0.00002 * sin(pi / 180 * (3 * mprime + m))
        apt1 += 0.00002 * sin(pi / 180 * (4 * mprime))

        apt2 = 0.000325 * sin(pi / 180 * (299.77 + 0.107408 * k - 0.009173 * t2))
        apt2 += 0.000165 * sin(pi / 180 * (251.88 + 0.016321 * k))
        apt2 += 0.000164 * sin(pi / 180 * (251.83 + 26.651886 * k))
        apt2 += 0.000126 * sin(pi / 180 * (349.42 + 36.412478 * k))
        apt2 += 0.00011 * sin(pi / 180 * (84.66 + 18.206239 * k))
        apt2 += 0.000062 * sin(pi / 180 * (141.74 + 53.303771 * k))
        apt2 += 0.00006 * sin(pi / 180 * (207.14 + 2.453732 * k))
        apt2 += 0.000056 * sin(pi / 180 * (154.84 + 7.30686 * k))
        apt2 += 0.000047 * sin(pi / 180 * (34.52 + 27.261239 * k))
        apt2 += 0.000042 * sin(pi / 180 * (207.19 + 0.121824 * k))
        apt2 += 0.00004 * sin(pi / 180 * (291.34 + 1.844379 * k))
        apt2 += 0.000037 * sin(pi / 180 * (161.72 + 24.198154 * k))
        apt2 += 0.000035 * sin(pi / 180 * (239.56 + 25.513099 * k))
        apt2 += 0.000023 * sin(pi / 180 * (331.55 + 3.592518 * k))
        
        return pt + apt1 + apt2

    def MeanNewMoon(self, jd: float) -> Tuple[int, float]:
        kn = floor((jd - 2451550.09765) / self.synmonth)
        jdt = 2451550.09765 + kn * self.synmonth
        t = (jdt - 2451545) / 36525
        thejd = (jdt + 0.0001337 * t * t - 0.00000015 * t * t * t + 
                 0.00000000073 * t * t * t * t)
        return kn, thejd

    def Solar2Julian(self, yy: int, mm: int, dd: int, hh: int = 0, mt: int = 0, ss: int = 0) -> Optional[float]:
        print(f"Solar2Julian input: year={yy}, month={mm}, day={dd}, hour={hh}, minute={mt}, second={ss}")
        
        if not self.ValidDate(yy, mm, dd):
            print("Invalid date")
            return None
            
        if not (0 <= hh < 24):
            print("Invalid hour")
            return None
            
        if not (0 <= mt < 60):
            print("Invalid minute")
            return None
            
        if not (0 <= ss < 60):
            print("Invalid second")
            return None
                
        yp = yy + floor((mm - 3) / 10)
        print(f"Calculated yp: {yp}")
        
        if yy > 1582 or (yy == 1582 and mm > 10) or (yy == 1582 and mm == 10 and dd >= 15):
            init = 1721119.5
            jdy = floor(yp * 365.25) - floor(yp / 100) + floor(yp / 400)
            print(f"Post 1582: init={init}, jdy={jdy}")
        elif yy < 1582 or (yy == 1582 and mm < 10) or (yy == 1582 and mm == 10 and dd <= 4):
            init = 1721117.5
            jdy = floor(yp * 365.25)
            print(f"Pre 1582: init={init}, jdy={jdy}")
        else:
            print("Date falls in 1582 gap")
            return None
                
        mp = floor(mm + 9) % 12
        jdm = mp * 30 + floor((mp + 1) * 34 / 57)
        jdd = dd - 1
        jdh = (hh + (mt + ss / 60) / 60) / 24
        
        result = jdy + jdm + jdd + jdh + init
        print(f"Calculated components: mp={mp}, jdm={jdm}, jdd={jdd}, jdh={jdh}")
        print(f"Final Julian date: {result}")
        return float(result)

    def Julian2Solar(self, jd: float) -> Tuple[int, int, int, int, int, int]:
        jd = float(jd)
        
        if jd >= 2299160.5:
            y4h = 146097
            init = 1721119.5
        else:
            y4h = 146100
            init = 1721117.5
            
        jdr = floor(jd - init)
        yh = y4h / 4
        cen = floor((jdr + 0.75) / yh)
        d = floor(jdr + 0.75 - cen * yh)
        ywl = 1461 / 4
        jy = floor((d + 0.75) / ywl)
        d = floor(d + 0.75 - ywl * jy + 1)
        ml = 153 / 5
        mp = floor((d - 0.5) / ml)
        d = floor((d - 0.5) - 30.6 * mp + 1)
        y = (100 * cen) + jy
        m = (mp + 2) % 12 + 1
        
        if m < 3:
            y = y + 1
            
        sd = floor((jd + 0.5 - floor(jd + 0.5)) * 24 * 60 * 60 + 0.00005)
        mt = floor(sd / 60)
        ss = sd % 60
        hh = floor(mt / 60)
        mt = mt % 60
        
        return floor(y), floor(m), floor(d), hh, mt, ss

    def GetSolarDays(self, yy: int, mm: int) -> int:
        if yy < -1000 or yy > 3000 or mm < 1 or mm > 12:
            return 0
            
        ndf1 = -(yy % 4 == 0)
        ndf2 = ((yy % 400 == 0) - (yy % 100 == 0)) and (yy > 1582)
        ndf = ndf1 + ndf2
        
        return 30 + ((abs(mm - 7.5) + 0.5) % 2) - int(mm == 2) * (2 + ndf)

    def ValidDate(self, yy: int, mm: int, dd: int) -> bool:
        print(f"ValidDate check for: year={yy}, month={mm}, day={dd}")
        
        if yy < -1000 or yy > 3000:
            print("Year out of range")
            return False
                
        if mm < 1 or mm > 12:
            print("Month out of range")
            return False
                
        if yy == 1582 and mm == 10 and 5 <= dd < 15:
            print("Date in 1582 gap")
            return False
        
        # 闰年判断    
        ndf1 = -(yy % 4 == 0)
        ndf2 = ((yy % 400 == 0) - (yy % 100 == 0)) and (yy > 1582)
        ndf = ndf1 + ndf2
        
        # 月份天数判断
        dom = 30 + ((abs(mm - 7.5) + 0.5) % 2) - int(mm == 2) * (2 + ndf)
        print(f"Day limit for month {mm}: {dom}")
        
        if dd <= 0 or dd > dom:
            if not (ndf == 0 and mm == 2 and dd == 29):
                print("Day out of range")
                return False
        
        print("Date is valid")
        return True

    def GetZodiac(self, mm: int, dd: int) -> Optional[int]:
        if mm < 1 or mm > 12 or dd < 1 or dd > 31:
            return None
            
        dds = [20,19,21,20,21,22,23,23,23,24,22,22]
        kn = mm - 1
        
        if dd < dds[kn]:
            kn = ((kn + 12) - 1) % 12
            
        return int(kn)

    def GetWeek(self, yy: int, mm: int, dd: int) -> Optional[int]:
        jd = self.Solar2Julian(yy, mm, dd, 12)
        if jd is None:
            return None
            
        return (((floor(jd + 1) % 7)) + 7) % 7

    def wuXingPingFen(self, info: Dict, noNaYin: bool = False) -> List[int]:
        wxFen = [0, 0, 0, 0, 0]
        
        for tg in info['tg']:
            fen = 6 if tg % 2 == 1 else 9
            wx = self.GetTgWx(tg)
            wxFen[wx] += fen
            
        for dz in info['dz_cg']:
            dz = dz['index']
            count = len(dz)
            fen_block = [18] if count == 1 else [11, 7] if count == 2 else [9, 6, 3]
            
            for i, tg in enumerate(dz):
                fen = 12 if tg % 2 == 1 else 18
                wx = self.GetTgWx(tg)
                wxFen[wx] += fen * fen_block[i] / 18
                
        if not noNaYin:
            for nayin in info['na_yin']:
                wxFen[nayin[1]] += nayin[2] / 20
                
        return wxFen

    def GetInfo(self, gd: int, yy: int, mm: int, dd: int, hh: int, mt: int = 0, ss: int = 0) -> Dict:
        """公历年排盘"""
        if gd not in [0, 1]:
            return {}
            
        ret = {
            'sex': gd,
            'big_tg': [], 
            'big_dz': [],
            'big': [],
            'big_start_time': [],
            'big_god': [],
            'big_cs': [],
            'years_info': []
        }
        
        # 获取四柱
        tg, dz, jd, jq, ix = self.GetGanZhi(yy, mm, dd, hh, mt, ss)
        # 带有中文的日志打印
        print(f"tg: {tg}, dz: {dz}, jd: {jd}, jq: {jq}, ix: {ix}")
        
        # 检查返回值是否有效
        if not tg or not dz or len(tg) < 4 or len(dz) < 4:
            return ret  # 返回空结果
            
        # 只有在有效数据时才继续计算
        xiong_wang = self.GetXiongWang(tg[2], dz[2])
        pn = tg[0] % 2

        if (gd == 0 and pn == 0) or (gd == 1 and pn == 1):  # 起大运.阴阳年干:0阳年1阴年
            span = jq[ix + 1] - jd  # 往后数一个节,计算时间跨度
            
            for i in range(1, 13):  # 大运干支
                ret['big_tg'].append((tg[1] + i) % 10)
                ret['big_dz'].append((dz[1] + i) % 12)
        else:  # 阴男阳女逆排,往前数一个节
            span = jd - jq[ix]
            
            for i in range(1, 13):  # 确保是正数
                ret['big_tg'].append((tg[0] + 20 - i) % 10)
                ret['big_dz'].append((dz[0] + 24 - i) % 12)

        days = int(span * 4 * 30)
        y = int(days / 360)
        m = int(days % 360 / 30)
        d = int(days % 360 % 30)

        ret.update({
            'tg': tg,
            'dz': dz,
            'bazi': [[self.ctg[tg[i]], self.cdz[dz[i]]] for i in range(4)],
            'sc': self.GetCTPart(hh, mt),
            'dz_cg': [],
            'na_yin': [],
            'xw': xiong_wang,
            'day_cs': [],
            'year_cs': [],
            'month_cs': [],
            'hour_cs': [],
            'self_qi': [],
            'start_desc': f"{y}年{m}月{d}天起运",
            'xz': self.cxz[self.GetZodiac(mm, dd)] if self.GetZodiac(mm, dd) is not None else "",
            'sx': self.csa[dz[0]]
        })
        start_jdtime = jd + span * 120
        ret['start_time'] = self.Julian2Solar(start_jdtime)

        for i in range(12):
            ret['big'].append(self.ctg[ret['big_tg'][i]] + self.cdz[ret['big_dz'][i]])
            ret['big_cs'].append(self.GetCs(tg[2], ret['big_dz'][i]))
            ret['big_god'].append(self.GetTenGod(tg[2], ret['big_tg'][i]))
            ret['big_start_time'].append(self.Julian2Solar(start_jdtime + i * 10 * 365))

        j = 0
        for i in range(1, 121):
            if (yy + i) < ret['start_time'][0]:
                continue
                
            t = (tg[0] + i) % 10
            d = (dz[0] + i) % 12
            tmp_year_dzcg = self.dzcg[d]
            tmp_year_god = [self.GetTenGod(tg[2], cg) for cg in tmp_year_dzcg]
            
            ret['years_info'].append({
                'year': yy + i - 1,
                'index': [t, d],
                'char': self.ctg[t] + self.cdz[d],
                'cg': tmp_year_dzcg,
                'cs': self.GetCs(tg[2], d),
                'tg_god': self.GetTenGod(tg[2], t),
                'dz_god': tmp_year_god
            })

        ret['wx_fen'] = self.wuXingPingFen(ret)
        return ret

    def GetCTPart(self, hh: int, mt: int) -> Dict:
        des = ['时头', '时中', '时尾']
        hh = int(hh)
        mt = int(mt)
        shi_chen = int((hh + 1) / 2) % 12
        part = 0
        
        if hh % 2:
            if mt > 40:
                part = 1
        else:
            if mt < 20:
                part = 1
            else:
                part = 2
                
        return {'index': [shi_chen, part], 'char': self.cdz[shi_chen] + des[part]}

    def naYin(self, tg: int, dz: int) -> List:
        if tg % 2 == 1:
            tg -= 1
            dz -= 1
            
        map_data = {
            0: {
                0: ['海中金', 3, 18], 2: ['大溪水', 4, 6], 4: ['佛灯火', 1, 1],
                6: ['沙中金', 3, 9], 8: ['井泉水', 4, 2], 10: ['山头火', 1, 6]
            },
            2: {
                0: ['涧下水', 4, 1], 2: ['炉中火', 1, 2], 4: ['沙中土', 2, 2],
                6: ['天河水', 4, 9], 8: ['山下火', 1, 4], 10: ['房上土', 2, 6]
            },
            4: {
                0: ['霹雳火', 1, 9], 2: ['城头土', 2, 9], 4: ['大林木', 0, 18],
                6: ['天上火', 1, 18], 8: ['大驿土', 2, 18], 10: ['平地木', 0, 9]
            },
            6: {
                0: ['壁上土', 2, 4], 2: ['松柏木', 0, 6], 4: ['白腊金', 3, 2],
                6: ['路边土', 2, 1], 8: ['石榴木', 0, 1], 10: ['钗钏金', 3, 4]
            },
            8: {
                0: ['桑松木', 0, 2], 2: ['金箔金', 3, 1], 4: ['长流水', 4, 4],
                6: ['杨柳木', 0, 4], 8: ['剑锋金', 3, 6], 10: ['大海水', 4, 18]
            }
        }
        return map_data[tg][dz]

    def GetXiongWang(self, day_tg_int: int, day_dz_int: int) -> Dict:
        xw_start = (day_dz_int - day_tg_int - 2) % 12
        xw_end = (xw_start + 1) % 12
        return {
            'index': [xw_start, xw_end],
            'char': self.cdz[xw_start] + self.cdz[xw_end]
        }

    def GetTenGod(self, day_tg_int: int, other_tg_int: int) -> Dict:
        l2_index = (day_tg_int + other_tg_int) % 2
        day_wx = self.GetTgWx(day_tg_int)
        other_wx = self.GetTgWx(other_tg_int)
        l1_index = (other_wx - day_wx) % 5
        return {
            'index': [l1_index, l2_index],
            'char': self.ten_god[l1_index][l2_index]
        }

    def GetTgWx(self, tg: int) -> int:
        return (tg if tg % 2 else tg) // 2

    def getSanHe(self, dz: int) -> Dict:
        fir = dz % 4 * 3
        sec = (fir + 4) % 12
        thr = (sec + 4) % 12
        ju_array = [4, 0, 1, 3]
        return {
            'sanhe': [fir, sec, thr],
            'ju': ju_array[fir // 3]
        }

    def getChong(self, dz: int) -> int:
        return (dz + 6) % 12

    def getXingFrom(self, dz: int) -> int:
        xing_map = [3, 7, 5, 0, 4, 8, 6, 10, 2, 9, 1, 11]
        return xing_map[dz]

    def getLiuHe(self, dz: int) -> Dict:
        tmp = 12 if dz == 0 else dz
        he = (13 - tmp) % 12
        hua = [2, 2, 0, 1, 3, 4, 2]
        ju = hua[dz] if dz < he else hua[he]
        return {'index': he, 'ju': ju}

    def getChuan(self, dz: int) -> int:
        return (19 - dz) % 12

    def getPo(self, dz: int) -> int:
        map_data = [9, 4, 11, 6, 1, 8, 6, 10, 5, 0, 2, 11]
        return map_data[dz]

    def GetCs(self, tg: int, dz: int) -> Dict:
        cs_dz_index = self.cs_tg2dz[tg]
        if tg % 2 == 0:
            move_num = (dz - cs_dz_index) % 12
        else:
            move_num = (cs_dz_index - dz) % 12
            
        return {'index': move_num, 'char': self.cs[move_num]}

    def GetGong(self, year_tg: int, month_dz: int, hour_dz: int) -> Dict:
        gong_dz = (29 - month_dz - hour_dz) % 12
        xi = 1 if gong_dz < 2 else 0
        gong_tg = ((year_tg % 5) * 2 + gong_dz + 12 * xi) % 10
        return {
            'index': [gong_tg, gong_dz],
            'char': self.ctg[gong_tg] + self.cdz[gong_dz]
        }

    def getSelfQi(self, tg: int, dz: int) -> Dict:
        biao = [
            [2,3,5,6,5,6,8,9,11,0],
            [3,None,6,None,7,None,9,None,0,None],
            [11,11,2,2,2,2,4,4,8,8],
            [7,7,10,10,10,4,1,1,4,4],
            [4,4,7,7,None,None,10,10,1,1],
            [6,6,9,9,9,9,0,0,3,3],
            [8,8,11,11,11,11,2,2,5,5]
        ]
        
        index = -1
        for i in range(7):
            if biao[i][tg] == dz:
                index = i
                break
                
        return {'index': index, 'char': '--' if index == -1 else self.selfQi[index]}
    

    def GetGanZhi(self, yy: int, mm: int, dd: int, hh: int, mt: int = 0, ss: int = 0) -> tuple:
        print(f"GetGanZhi called with: year={yy}, month={mm}, day={dd}, hour={hh}, minute={mt}, second={ss}")
        
        # 多加一秒避免精度问题
        jd = self.Solar2Julian(yy, mm, dd, hh, mt, max(1, ss))
        print(f"Solar2Julian returned: {jd}")
        
        if jd is None:  # 修改判断条件
            print("Solar2Julian returned None")
            return [], [], 0, [], 0
        
        tg = []
        dz = []
        
        # 取得自立春开始的节,该数组长度固定为16
        jq = self.GetPureJQsinceSpring(yy)
        print(f"GetPureJQsinceSpring returned jq: {jq}")
        print(f"Current JD: {jd}")
        
        # 严格检查节气数组
        if not jq or len(jq) < 13:  # 只需要13个节气
            print("Not enough JieQi data")
            return [], [], 0, [], 0
        
        # 检查立春
        if jd < jq[1]:  # jq[1]为立春,约在2月5日前後
            print(f"Before LiChun, adjusting year to: {yy-1}")
            yy = yy - 1  # 若小于jq[1],则属于前一个节气年
            jq = self.GetPureJQsinceSpring(yy)  # 取得自立春开始的节
            if not jq or len(jq) < 13:  # 再次检查节气数组
                print("Not enough JieQi data after year adjustment")
                return [], [], 0, [], 0
        
        ygz = ((yy + 4712 + 24) % 60 + 60) % 60
        tg.append(ygz % 10)  # 年干
        dz.append(ygz % 12)  # 年支
        
        # 比较求算节气月,求出月干支
        ix = 0
        print(f"Searching for JieQi matching JD: {jd}")
        for j in range(len(jq)):  # 确保不超出数组范围
            print(f"Comparing with JieQi[{j}]: {jq[j]}")
            if jq[j] >= jd:  # 已超过指定时刻,故应取前一个节气
                ix = j - 1
                print(f"Found matching JieQi at index: {ix}")
                break
            ix = j  # 如果没有找到大于jd的节气，使用最后一个节气
        
        # 数组0为前一年的小寒所以这里再减一
        tmm = ((yy + 4712) * 12 + (ix - 1) + 60) % 60
        mgz = (tmm + 50) % 60
        tg.append(mgz % 10)  # 月干
        dz.append(mgz % 12)  # 月支
        
        # 计算日柱之干支,加0.5是将起始点从正午改为从0点开始
        jda = jd + 0.5
        # 将jd的小数部份化为秒,并加上起始点前移的一小时(3600秒),取其整数值
        thes = ((jda - floor(jda)) * 86400) + 3600
        # 将秒数化为日数,加回到jd的整数部份
        dayjd = floor(jda) + thes / 86400
        dgz = (floor(dayjd + 49) % 60 + 60) % 60
        tg.append(dgz % 10)  # 日干
        dz.append(dgz % 12)  # 日支
        
        # 区分早晚子时,日柱前移一柱
        if self.zwz and (hh >= 23):
            tg[2] = (tg[2] + 10 - 1) % 10
            dz[2] = (dz[2] + 12 - 1) % 12
        
        # 计算时柱之干支
        dh = dayjd * 12
        hgz = (floor(dh + 48) % 60 + 60) % 60
        tg.append(hgz % 10)  # 时干
        dz.append(hgz % 12)  # 时支
        
        return tg, dz, jd, jq, ix