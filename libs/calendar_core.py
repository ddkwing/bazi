from math import floor, pi
from typing import List, Tuple, Optional, Union
from libs.calendar_base import CalendarBase
from math import sin, cos, tan, sqrt, atan

class CalendarCore(CalendarBase):
    def __init__(self):
        super().__init__()

    def VE(self, yy: int) -> Optional[float]:
        if yy < -8000 or yy > 8001:
            return None
            
        if 1000 <= yy <= 8001:
            m = (yy - 2000) / 1000
            return 2451623.80984 + 365242.37404 * m + 0.05169 * m * m - 0.00411 * m * m * m - 0.00057 * m * m * m * m
            
        m = yy / 1000
        return 1721139.29189 + 365242.1374 * m + 0.06134 * m * m + 0.00111 * m * m * m - 0.00071 * m * m * m * m

    def Perturbation(self, jd: float) -> float:
        t = (jd - 2451545) / 36525
        s = 0
        for k in range(24):
            s += self.ptsa[k] * cos(self.ptsb[k] * 2 * pi / 360 + self.ptsc[k] * 2 * pi / 360 * t)
        
        w = 35999.373 * t - 2.47
        l = 1 + 0.0334 * cos(w * 2 * pi / 360) + 0.0007 * cos(2 * w * 2 * pi / 360)
        return 0.00001 * s / l

    def DeltaT(self, yy: int, mm: int) -> float:
        y = yy + (mm - 0.5) / 12

        if y <= -500:
            u = (y - 1820) / 100
            dt = -20 + 32 * u * u
        elif y < 500:
            u = y / 100
            dt = 10583.6 - 1014.41 * u + 33.78311 * u * u - 5.952053 * u * u * u - \
                 0.1798452 * u * u * u * u + 0.022174192 * u * u * u * u * u + \
                 0.0090316521 * u * u * u * u * u * u
        elif y < 1600:
            u = (y - 1000) / 100
            dt = 1574.2 - 556.01 * u + 71.23472 * u * u + 0.319781 * u * u * u - \
                 0.8503463 * u * u * u * u - 0.005050998 * u * u * u * u * u + \
                 0.0083572073 * u * u * u * u * u * u
        elif y < 1700:
            t = y - 1600
            dt = 120 - 0.9808 * t - 0.01532 * t * t + t * t * t / 7129
        elif y < 1800:
            t = y - 1700
            dt = 8.83 + 0.1603 * t - 0.0059285 * t * t + 0.00013336 * t * t * t - \
                 t * t * t * t / 1174000
        elif y < 1860:
            t = y - 1800
            dt = 13.72 - 0.332447 * t + 0.0068612 * t * t + 0.0041116 * t * t * t - \
                 0.00037436 * t * t * t * t + 0.0000121272 * t * t * t * t * t - \
                 0.0000001699 * t * t * t * t * t * t + \
                 0.000000000875 * t * t * t * t * t * t * t
        elif y < 1900:
            t = y - 1860
            dt = 7.62 + 0.5737 * t - 0.251754 * t * t + 0.01680668 * t * t * t - \
                 0.0004473624 * t * t * t * t + t * t * t * t * t / 233174
        elif y < 1920:
            t = y - 1900
            dt = -2.79 + 1.494119 * t - 0.0598939 * t * t + 0.0061966 * t * t * t - \
                 0.000197 * t * t * t * t
        elif y < 1941:
            t = y - 1920
            dt = 21.20 + 0.84493 * t - 0.0761 * t * t + 0.0020936 * t * t * t
        elif y < 1961:
            t = y - 1950
            dt = 29.07 + 0.407 * t - t * t / 233 + t * t * t / 2547
        elif y < 1986:
            t = y - 1975
            dt = 45.45 + 1.067 * t - t * t / 260 - t * t * t / 718
        elif y < 2005:
            t = y - 2000
            dt = 63.86 + 0.3345 * t - 0.060374 * t * t + 0.0017275 * t * t * t + \
                 0.000651814 * t * t * t * t + 0.00002373599 * t * t * t * t * t
        elif y < 2050:
            t = y - 2000
            dt = 62.92 + 0.32217 * t + 0.005589 * t * t
        elif y < 2150:
            u = (y - 1820) / 100
            dt = -20 + 32 * u * u - 0.5628 * (2150 - y)
        else:
            u = (y - 1820) / 100
            dt = -20 + 32 * u * u

        if y < 1955 or y >= 2005:
            dt -= 0.000012932 * (y - 1955) * (y - 1955)
            
        return dt / 60

    def MeanJQJD(self, yy: int) -> List[float]:
        print(f"MeanJQJD called with year: {yy}")
        jd = self.VE(yy)
        if not jd:
            return []
            
        ty = self.VE(yy + 1) - jd
        num = 26  # 24 + 2
        ath = 2 * pi / 24
        tx = (jd - 2451545) / 365250
        e = 0.0167086342 - 0.0004203654 * tx - 0.0000126734 * tx * tx + \
            0.0000001444 * tx * tx * tx - 0.0000000002 * tx * tx * tx * tx + \
            0.0000000003 * tx * tx * tx * tx * tx
        tt = yy / 1000
        vp = 111.25586939 - 17.0119934518333 * tt - 0.044091890166673 * tt * tt - \
             4.37356166661345E-04 * tt * tt * tt + 8.16716666602386E-06 * tt * tt * tt * tt
        rvp = vp * 2 * pi / 360
        
        peri = []
        for i in range(num):
            flag = 0
            th = ath * i + rvp
            
            if pi < th <= 3 * pi:
                th = 2 * pi - th
                flag = 1
            elif th > 3 * pi:
                th = 4 * pi - th
                flag = 2
                
            f1 = 2 * atan(sqrt((1 - e) / (1 + e)) * tan(th / 2))
            f2 = (e * sqrt(1 - e * e) * sin(th)) / (1 + e * cos(th))
            f = (f1 - f2) * ty / 2 / pi
            
            if flag == 1:
                f = ty - f
            elif flag == 2:
                f = 2 * ty - f
                
            peri.append(f)
            
        return [jd + p - peri[0] for p in peri]

    def GetAdjustedJQ(self, yy: int, start: int, end: int) -> List[float]:
        print(f"GetAdjustedJQ called with year: {yy}, start: {start}, end: {end}")
        if not (0 <= start <= 25) or not (0 <= end <= 25):
            return []
            
        jq = []
        jqjd = self.MeanJQJD(yy)
        print(f"MeanJQJD returned: {jqjd}")
        
        if not jqjd:  # 检查是否获取到结果
            return []
            
        for k in range(start, end + 1):
            if k >= len(jqjd):
                break
            ptb = self.Perturbation(jqjd[k])
            dt = self.DeltaT(yy, floor((k + 1) / 2) + 3)
            jq.append(jqjd[k] + ptb - dt / 60 / 24 + 1 / 3)
        
        print(f"GetAdjustedJQ returning: {jq}")
        return jq

    def GetPureJQsinceSpring(self, yy: int) -> List[float]:
        print(f"GetPureJQsinceSpring called with year: {yy}")
        jdpjq = []
        
        # 求出含指定年立春开始之3个节气JD值,以前一年的年值代入
        dj = self.GetAdjustedJQ(yy - 1, 19, 23)
        print(f"First GetAdjustedJQ returned: {dj}")
        
        if dj:  # 只有在获取到结果时才处理
            for i in range(19, 24, 2):
                if i < len(dj):
                    jdpjq.append(dj[i])
        
        # 求出指定年节气之JD值
        dj = self.GetAdjustedJQ(yy, 0, 25)
        print(f"Second GetAdjustedJQ returned: {dj}")
        
        if dj:  # 只有在获取到结果时才处理
            for i in range(0, 26, 2):
                if i < len(dj):
                    jdpjq.append(dj[i])
        
        print(f"Final jdpjq: {jdpjq}")
        return jdpjq

    def GetZQsinceWinterSolstice(self, yy: int) -> List[float]:
        jdzq = []
        
        dj = self.GetAdjustedJQ(yy - 1, 18, 23)
        jdzq.extend([dj[18], dj[20], dj[22]])
        
        dj = self.GetAdjustedJQ(yy, 0, 23)
        jdzq.extend(dj[i] for i in range(0, 24, 2))
        
        return jdzq