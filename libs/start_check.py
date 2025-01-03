class StarsCheck:
    def kong_wang(self, info, star, key, value):
        kong_wang = info['xw']['index']
        dz = info['dz']
        for i in range(4):
            if dz[i] in kong_wang:
                star[i][key] = value

    def ci_guan(self, info, star, key, value):
        dz = info['dz']
        na_yin = info['na_yin'][0]
        mapping = {0: 2, 1: 5, 2: 5, 3: 8, 4: 11}
        find = mapping.get(na_yin[1])
        
        if find is not None:
            for i in range(1, 4):
                if dz[i] == find:
                    star[i][key] = value

    def hong_lian(self, info, star, key, value):
        dz = info['dz']
        find = (15 - dz[0]) % 12
        
        for i in range(1, 4):
            if dz[i] == find:
                star[i][key] = value

    def tian_xi(self, info, star, key, value):
        dz = info['dz']
        find = (21 - dz[0]) % 12
        
        for i in range(1, 4):
            if dz[i] == find:
                star[i][key] = value

    def tao_hua(self, info, star, key, value):
        dz = info['dz']
        day = info['dz'][2]
        year = info['dz'][0]
        mapping = [9,6,3,0,9,6,3,0,9,6,3,0]
        
        for i in range(4):
            if i != 2 and dz[i] == mapping[day]:
                star[i][key] = value
            if i != 0 and dz[i] == mapping[year]:
                star[i][key] = value

    def gan_lu(self, info, star, key, value):
        day = info['tg'][2]
        mapping = [2,3,5,6,None,None,8,9,11,0]
        dz = info['dz']
        find = mapping[day]
        
        if find is not None:
            for i in range(4):
                if dz[i] == find:
                    star[i][key] = value

    def shi_ling(self, info, star, key, value):
        mapping = ['0-8','1-9','2-0','3-1','4-6','5-1','6-2','7-3','8-6','9-7']
        find = f"{info['tg'][2]}-{info['dz'][2]}"
        
        if find in mapping:
            star[2][key] = value

    def shi_e(self, info, star, key, value):
        mapping = ['0-8','1-9','2-0','3-1','4-6','5-1','6-2','7-3','8-6','9-7']
        find = f"{info['tg'][2]}-{info['dz'][2]}"
        
        if find in mapping:
            star[2][key] = value

    def jie_sha(self, info, star, key, value):
        dz = info['dz']
        day = info['dz'][2]
        year = info['dz'][0]
        mapping = [5,2,11,8,5,2,10,8,5,2,11,8]
        
        for i in range(4):
            if i != 2 and dz[i] == mapping[day]:
                star[i][key] = value
            if i != 0 and dz[i] == mapping[year]:
                star[i][key] = value

    def wang_shen(self, info, star, key, value):
        dz = info['dz']
        day = info['dz'][2]
        year = info['dz'][0]
        mapping = [11,8,5,2,11,8,5,2,11,8,5,2]
        
        for i in range(4):
            if i != 2 and dz[i] == mapping[day]:
                star[i][key] = value
            if i != 0 and dz[i] == mapping[year]:
                star[i][key] = value

    def yuan_chen(self, info, star, key, value):
        dz = info['dz']
        chong = dz[0] + 6
        shunxu = dz[0] + info['sex'] % 2
        target = chong - 1 if shunxu == 0 else chong + 1
        
        for i in range(1, 4):
            if dz[i] == target:
                star[i][key] = value

    def gu_chen(self, info, star, key, value):
        dz = info['dz']
        mapping = [2,2,5,5,5,8,8,8,11,11,11,2]
        target = mapping[dz[0]]
        
        for i in range(1, 4):
            if dz[i] == target:
                star[i][key] = value

    def gua_su(self, info, star, key, value):
        dz = info['dz']
        mapping = [10,10,1,1,1,4,4,4,7,7,7,10]
        target = mapping[dz[0]]
        
        for i in range(1, 4):
            if dz[i] == target:
                star[i][key] = value

    def zhai_sha(self, info, star, key, value):
        dz = info['dz']
        year = info['dz'][0]
        mapping = [6,3,0,9,6,3,0,9,6,3,0,9]
        
        for i in range(1, 4):
            if dz[i] == mapping[year]:
                star[i][key] = value

    def liu_e(self, info, star, key, value):
        dz = info['dz']
        year = info['dz'][0]
        mapping = [3,0,9,6,3,0,9,6,3,0,9,6]
        
        for i in range(1, 4):
            if dz[i] == mapping[year]:
                star[i][key] = value

    def gou_sha(self, info, star, key, value):
        dz = info['dz']
        hit = (info['sex'] + dz[0]) % 2
        if hit == 0:
            target = (dz[0] + 12 - 3) % 12
            for i in range(1, 4):
                if dz[i] == target:
                    star[i][key] = value

    def jiao_sha(self, info, star, key, value):
        dz = info['dz']
        hit = (info['sex'] + dz[0]) % 2
        if hit == 0:
            target = (dz[0] + 3) % 12
            for i in range(1, 4):
                if dz[i] == target:
                    star[i][key] = value

    def tong_zi(self, info, star, key, value):
        dz = info['dz']
        na_yin = info['na_yin'][0][1]
        target = []
        
        if 1 < dz[1] <= 4:
            target = [0, 2]
        elif 4 < dz[1] <= 7:
            target = [3, 7, 4]
            
        if na_yin in [0, 3]:
            target.extend([6, 3])
        elif na_yin in [1, 4]:
            target.extend([9, 10])
        elif na_yin == 3:
            target.extend([4, 5])
            
        for i in range(2, 4):
            if dz[i] in target:
                star[i][key] = value

    def xue_tang(self, info, star, key, value):
        tg = info['tg']
        dz = info['dz']
        na_yin = info['na_yin'][0]
        mapping = {0: 11, 1: 2, 2: 8, 3: 5, 4: 8}
        find = mapping.get(na_yin[1])
        
        if find is not None:
            for i in range(1, 4):
                if dz[i] == find:
                    star[i][key] = value

    def hong_yang(self, info, star, key, value):
        dz = info['dz']
        mapping = {0: 6, 1: 8, 2: 2, 3: 7, 4: 4, 5: 4, 
                  6: 10, 7: 9, 8: 0, 9: 8}
        find = mapping.get(info['tg'][2])
        
        if find is not None:
            for i in range(4):
                if dz[i] == find:
                    star[i][key] = value

    def liu_xia(self, info, star, key, value):
        dz = info['dz']
        mapping = {0: 9, 1: 10, 2: 7, 3: 8, 4: 5, 5: 6, 
                  6: 4, 7: 3, 8: 11, 9: 2}
        find = mapping.get(info['tg'][2])
        
        if find is not None:
            for i in range(4):
                if dz[i] == find:
                    star[i][key] = value

    def jiang_xing(self, info, star, key, value):
        dz = info['dz']
        day = info['dz'][2]
        year = info['dz'][0]
        mapping = [0,9,6,3,0,9,6,3,0,9,6,3]
        
        for i in range(4):
            if i != 2 and dz[i] == mapping[day]:
                star[i][key] = value
            if i != 0 and dz[i] == mapping[year]:
                star[i][key] = value

    def hua_gai(self, info, star, key, value):
        dz = info['dz']
        day = info['dz'][2]
        year = info['dz'][0]
        mapping = [4,1,10,7,4,1,10,7,4,1,10,7]
        
        for i in range(4):
            if i != 2 and dz[i] == mapping[day]:
                star[i][key] = value
            if i != 0 and dz[i] == mapping[year]:
                star[i][key] = value

    def yi_ma(self, info, star, key, value):
        dz = info['dz']
        day = info['dz'][2]
        year = info['dz'][0]
        mapping = [2,11,8,5,2,11,8,5,2,11,8,5]
        
        for i in range(4):
            if i != 2 and dz[i] == mapping[day]:
                star[i][key] = value
            if i != 0 and dz[i] == mapping[year]:
                star[i][key] = value

    def tian_yi(self, info, star, key, value):
        tg = info['tg']
        dz = info['dz']
        mapping = {
            0: [1, 7], 1: [0, 8], 2: [9, 11], 3: [9, 11], 
            4: [1, 7], 5: [0, 8], 6: [6, 2], 7: [6, 2],
            8: [3, 5], 9: [3, 5]
        }
        tian_yi = mapping[tg[0]] + mapping[tg[2]]
        for i in range(4):
            if dz[i] in tian_yi:
                star[i][key] = value

    def tai_ji(self, info, star, key, value):
        tg = info['tg']
        dz = info['dz']
        mapping = {
            0: [0, 6], 1: [0, 6], 2: [3, 9], 3: [3, 9],
            4: [4, 10, 1, 7], 5: [4, 10, 1, 7], 6: [2, 11],
            7: [2, 11], 8: [5, 7], 9: [5, 7]
        }
        tai_ji = mapping[tg[0]] + mapping[tg[2]]
        for i in range(4):
            if dz[i] in tai_ji:
                star[i][key] = value

    def tian_yi2(self, info, star, key, value):
        dz = info['dz']
        tian_yi = (info['dz'][1] + 12 - 1) % 12
        for i in range(4):
            if i == 1:
                continue
            if tian_yi == dz[i]:
                star[i][key] = value

    def tian_de(self, info, star, key, value):
        dz = info['dz']
        tg = info['tg']
        tiande_map = {
            0: [1, 5], 1: [0, 6], 2: [0, 3], 3: [1, 8],
            4: [0, 8], 5: [0, 7], 6: [1, 11], 7: [0, 0],
            8: [0, 9], 9: [1, 2], 10: [0, 2], 11: [0, 1]
        }
        tiande = tiande_map[dz[1]]
        check = tg if tiande[0] == 0 else dz
        for i in range(4):
            if check[i] == tiande[1]:
                star[i][key] = value

    def yue_de(self, info, star, key, value):
        tg = info['tg']
        dz = info['dz']
        mapping = [8, 6, 2, 0, 8, 6, 2, 0, 8, 6, 2, 0]
        yue_de = mapping[dz[1]]
        for i in range(4):
            if yue_de == tg[i]:
                star[i][key] = value

    def lu_shen(self, info, star, key, value):
        tg = info['tg']
        dz = info['dz']
        mapping = [2, 3, 5, 6, 5, 6, 8, 9, 11, 0]
        day = tg[2]
        tmp = mapping[day]
        for i in range(4):
            if tmp == dz[i]:
                star[i][key] = value

    def yang_ren(self, info, star, key, value):
        tg = info['tg']
        dz = info['dz']
        day = tg[2]
        mapping = {0: 3, 2: 6, 4: 6, 6: 9, 8: 0}
        if day in mapping:
            tmp = mapping[day]
            for i in range(4):
                if tmp == dz[i]:
                    star[i][key] = value

    def jin_yu(self, info, star, key, value):
        dz = info['dz']
        find = None
        day_tg = info['tg'][2]
        mapping = {0: 4, 1: 5, 2: 7, 3: 8, 4: 7, 5: 8, 
                  6: 10, 7: 11, 8: 1, 9: 2}
        find = mapping.get(day_tg)
        
        if find is not None:
            for i in range(4):
                if dz[i] == find:
                    star[i][key] = value

    def fu_xing(self, info, star, key, value):
        tg = info['tg']
        dz = info['dz']
        find = []
        
        if tg[2] in [0, 2] or tg[0] in [0, 2]:
            find = [0, 2]
        if tg[2] in [1, 9] or tg[0] in [1, 9]:
            find.extend([3, 1])
        if tg[2] in [4] or tg[0] in [4]:
            find.append(8)
        if tg[2] in [5] or tg[0] in [5]:
            find.append(7)
        if tg[2] in [3] or tg[0] in [3]:
            find.append(11)
        if tg[2] in [6] or tg[0] in [6]:
            find = [6]
        if tg[2] in [7] or tg[0] in [7]:
            find = [5]
        if tg[2] in [8] or tg[0] in [8]:
            find = [4]
            
        if find:
            for i in range(4):
                if dz[i] in find:
                    star[i][key] = value

    def guo_yin(self, info, star, key, value):
        tg = info['tg']
        dz = info['dz']
        mapping = {0: 10, 1: 11, 2: 1, 3: 2, 4: 1, 5: 2, 
                  6: 4, 7: 5, 8: 7, 9: 8}
        find = []
        
        if tg[0] in mapping:
            find.append(mapping[tg[0]])
        if tg[2] in mapping:
            find.append(mapping[tg[2]])
            
        for i in range(4):
            if dz[i] in find:
                star[i][key] = value

    def tian_chu(self, info, star, key, value):
        tg = info['tg']
        dz = info['dz']
        mapping = {0: 5, 1: 6, 2: 0, 3: 5, 4: 6, 5: 8, 
                  6: 2, 7: 6, 8: 9, 9: 11}
        find = []
        
        if tg[0] in mapping:
            find.append(mapping[tg[0]])
        if tg[2] in mapping:
            find.append(mapping[tg[2]])
            
        for i in range(4):
            if dz[i] in find:
                star[i][key] = value

    def gu_luan(self, info, star, key, value):
        tg = info['tg']
        dz = info['dz']
        mapping = ['1-5', '3-5', '7-11', '4-8', '0-2', '4-6', '8-0', '2-6']
        day = f"{tg[2]}-{dz[2]}"
        hour = f"{tg[2]}-{dz[3]}"
        if day in mapping and hour in mapping:
            star[2][key] = value

    def san_qi(self, info, star, key, value):
        tg = info['tg']
        tg_str = '-'.join(map(str, tg))
        mapping = ['0-4-6', '6-4-0', '1-2-3', '3-2-1', '8-9-6', '6-9-8']
        for sanqi in mapping:
            v = tg_str.find(sanqi)
            if v != -1:
                if v == 2:
                    star[3][key] = value
                else:
                    star[0][key] = value
                star[1][key] = value
                star[2][key] = value
                break

    def tian_xie(self, info, star, key, value):
        dz = info['dz']
        tg = info['tg']
        if dz[1] in [2, 3, 4]:
            if tg[2] == 4 and dz[2] == 2:
                star[2][key] = value
        elif dz[1] in [5, 6, 7]:
            if tg[2] == 0 and dz[2] == 6:
                star[2][key] = value
        elif dz[1] in [8, 9, 10]:
            if tg[2] == 4 and dz[2] == 8:
                star[2][key] = value
        elif dz[1] in [11, 0, 1]:
            if tg[2] == 0 and dz[2] == 0:
                star[2][key] = value

    def de_xiu(self, info, star, key, value):
        dz = info['dz']
        tg = info['tg']
        if dz[1] in [2, 6, 10]:
            if 2 in tg and 3 in tg:
                xiu = [i for i in range(len(tg)) if tg[i] in [2, 3]]
        elif dz[1] in [8, 0, 4]:
            if (2 in tg and 7 in tg) or (0 in tg and 5 in tg):
                xiu = [i for i in range(len(tg)) if tg[i] in [8, 9, 4, 5]]
        elif dz[1] in [5, 9, 1]:
            if 1 in tg and 6 in tg:
                xiu = [i for i in range(1, len(tg)) if tg[i] == 6]
                xiu.extend([i for i in range(len(tg)) if tg[i] == 7])
        elif dz[1] in [11, 3, 7]:
            if 3 in tg and 8 in tg:
                xiu = [i for i in range(len(tg)) if tg[i] in [0, 1]]
        
        if 'xiu' in locals():
            for i in xiu:
                star[i][key] = value

    def kui_gang(self, info, star, key, value):
        day = f"{info['tg'][2]}-{info['dz'][2]}"
        mapping = ['8-4', '7-10', '7-4', '4-10']
        if day in mapping:
            star[2][key] = value

    def jing_shen(self, info, star, key, value):
        mapping = ['1-1', '5-5', '8-8']
        fire = [2, 5, 6, 7, 10]
        day = f"{info['tg'][2]}-{info['dz'][2]}"
        if day in mapping:
            if info['dz'][1] in fire:
                value[1] += '(带火)'
            else:
                value[1] += '(无火)'
            star[2][key] = value
        elif info['tg'][2] in [0, 1]:
            hour = f"{info['tg'][3]}-{info['dz'][3]}"
            if hour in mapping:
                if info['dz'][1] in fire:
                    value[1] += '(带火)'
                else:
                    value[1] += '(无火)'
                star[2][key] = value

    def tian_luo(self, info, star, key, value):
        if info['dz'][2] in [10, 11]:
            mapping = [f"{i}-{j}" for i, j in zip([4,5,2,3,0,1,4,5,2,3,0,1], range(12))]
            year = f"{info['tg'][0]}-{info['dz'][0]}"
            if year in mapping:
                star[2][key] = value

    def di_wang(self, info, star, key, value):
        if info['dz'][2] in [4, 5]:
            tg_list1 = [2,4,0,1,8,9,2,3,0,1,8,9]
            tg_list2 = [6,7,4,5,2,3,7,8,4,5,2,3]
            mapping = [f"{i}-{j}" for i, j in zip(tg_list1 + tg_list2, list(range(12))*2)]
            year = f"{info['tg'][0]}-{info['dz'][0]}"
            if year in mapping:
                star[2][key] = value

    def wen_chang(self, info, star, key, value):
        tg = info['tg']
        dz = info['dz']
        find = None
        if tg[2] in [0] or tg[0] in [0]:
            find = 5
        elif tg[2] in [1] or tg[0] in [1]:
            find = 6
        elif tg[2] in [2] or tg[0] in [2]:
            find = 8
        elif tg[2] in [3] or tg[0] in [3]:
            find = 9
        elif tg[2] in [4] or tg[0] in [4]:
            find = 8
        elif tg[2] in [5] or tg[0] in [5]:
            find = 9
        elif tg[2] in [6] or tg[0] in [6]:
            find = 11
        elif tg[2] in [7] or tg[0] in [7]:
            find = 0
        elif tg[2] in [8] or tg[0] in [8]:
            find = 2
        elif tg[2] in [9] or tg[0] in [9]:
            find = 3

        if find is not None:
            for i in range(4):
                if dz[i] == find:
                    star[i][key] = value