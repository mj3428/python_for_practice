#!/usr/bin/env python
# encoding: utf-8
'''
@author: miaojue
@contact: major3428@foxmail.com
@software: pycharm
@file: auto_cal.py
@time: 2019-1-22 上午 9:05
@desc:
'''
from auto_config import *
import pandas as pd
import numpy as np
from random import choice

class Calculate:
    def __init__(self, path=PATH, kva=KVA, frequence=None):
        self.path = path
        self.kva = kva
        self.ele = ELECTRIC[str(kva)]
        self.freq = frequence
    def add_model(self):
        '''
        模型初始
        :return:
        '''
        df0 = pd.read_csv(self.path, index_col=0)
        df0.rename(columns={'采集时间': 'ds', 'A相电流': 'Ia', 'B相电流': 'Ib', 'C相电流': 'Ic',
                            'A相电流THD': 'Ia_THD', 'B相电流THD': 'Ib_THD', 'C相电流THD': 'Ic_THD',
                            'A相电压': 'Ua', 'B相电压': 'Ub', 'C相电压': 'Uc',
                            'A相电压THD': 'Ua_THD', 'B相电压THD': 'Ub_THD', 'C相电压THD': 'Uc_THD',
                            '总功率因数': 'PF', '三相无功功率': 'Q', '三相有功功率': 'P',
                            'A相电流H3': 'Ia_H3', 'A相电流H5': 'Ia_H5', 'A相电流H7': 'Ia_H7',
                            'A相电流H9': 'Ia_H9', 'A相电流H11': 'Ia_H11', 'A相电流H13': 'Ia_H13',
                            'A相电流H15': 'Ia_H15', 'A相电流H17': 'Ia_H17', 'A相电流H19': 'Ia_H19',
                            'A相电流H21': 'Ia_H21',
                            'B相电流H3': 'Ib_H3', 'B相电流H5': 'Ib_H5', 'B相电流H7': 'Ib_H7',
                            'B相电流H9': 'Ib_H9', 'B相电流H11': 'Ib_H11', 'B相电流H13': 'Ib_H13',
                            'B相电流H15': 'Ib_H15', 'B相电流H17': 'Ib_H17', 'B相电流H19': 'Ib_H19',
                            'B相电流H21': 'Ib_H21',
                            'C相电流H3': 'Ic_H3', 'C相电流H5': 'Ic_H5', 'C相电流H7': 'Ic_H7',
                            'C相电流H9': 'Ic_H9', 'C相电流H11': 'Ic_H11', 'C相电流H13': 'Ic_H13',
                            'C相电流H15': 'Ic_H15', 'C相电流H17': 'Ic_H17', 'C相电流H19': 'Ic_H19',
                            'C相电流H21': 'Ic_H21'
                            }, inplace=True)
        self.freq = len(df0.ds)
        df0['I_ave'] = (df0.Ia + df0.Ib + df0.Ic) / 3
        df0['U_ave'] = (df0.Ua + df0.Ub + df0.Uc) / 3
        df0['LF'] = np.sqrt(pow(df0.P, 2) + pow(df0.Q, 2)) / (self.kva * 10)
        df0['I_UP'] = df0.apply(lambda x: self.jungle(x), axis=1) * 100
        self.dforignal = df0
        df1 = df0.ix[df0.I_ave >= self.ele]
        df1 = df1.sort_values(by='ds')
        df1.reset_index(inplace=True, drop=True)  # 重新构造索引 drop=True替换原index
        return df1

    # 判断不平衡
    def jungle(self, a):
        if a['I_ave'] == 0:
            return 0
        else:
            value = max(abs(a['Ia'] - a['I_ave']), abs(a['Ib'] - a['I_ave']), abs(a['Ic'] - a['I_ave'])) / a['I_ave']
            return value

    def calculate(self):
        '''
        获取最大值
        :return:
        '''
        df1 = self.add_model()
        #print(df1.head(12))
        self.max_vals1 = np.max([[df1.Ua.max(), df1.Ub.max(), df1.Uc.max()],
                                 [df1.Ua_THD.max(), df1.Ub_THD.max(), df1.Uc_THD.max()],
                                 [df1.Ia.max(), df1.Ib.max(), df1.Ic.max()]], axis=1)
        A1 = df1.Ia
        df1['iam3'], df1['iam5'] = A1 * df1.Ia_H3 / 100, A1 * df1.Ia_H5 / 100
        df1['iam7'], df1['iam9'] = A1 * df1.Ia_H7 / 100, A1 * df1.Ia_H9 / 100
        df1['iam11'], df1['iam13'] = A1 * df1.Ia_H11 / 100, A1 * df1.Ia_H13 / 100
        df1['iam15'], df1['iam17'] = A1 * df1.Ia_H15 / 100, A1 * df1.Ia_H17 / 100
        df1['iam19'], df1['iam21'] = A1 * df1.Ia_H19 / 100, A1 * df1.Ia_H21 / 100
        A2 = df1.Ib
        df1['ibm3'], df1['ibm5'] = A2 * df1.Ib_H3 / 100, A2 * df1.Ib_H5 / 100
        df1['ibm7'], df1['ibm9'] = A2 * df1.Ib_H7 / 100, A2 * df1.Ib_H9 / 100
        df1['ibm11'], df1['ibm13'] = A1 * df1.Ib_H11 / 100, A1 * df1.Ib_H13 / 100
        df1['ibm15'], df1['ibm17'] = A1 * df1.Ib_H15 / 100, A1 * df1.Ib_H17 / 100
        df1['ibm19'], df1['ibm21'] = A1 * df1.Ib_H19 / 100, A1 * df1.Ib_H21 / 100
        A3 = df1.Ic
        df1['icm3'], df1['icm5'] = A3 * df1.Ic_H3 / 100, A3 * df1.Ic_H5 / 100
        df1['icm7'], df1['icm9'] = A3 * df1.Ic_H7 / 100, A3 * df1.Ic_H9 / 100
        df1['icm11'], df1['icm13'] = A1 * df1.Ic_H11 / 100, A1 * df1.Ic_H13 / 100
        df1['icm15'], df1['icm17'] = A1 * df1.Ic_H15 / 100, A1 * df1.Ic_H17 / 100
        df1['icm19'], df1['icm21'] = A1 * df1.Ic_H19 / 100, A1 * df1.Ic_H21 / 100
        self.max_vals2 = {'3': max(df1.iam3.max(), df1.ibm3.max(), df1.icm3.max()),
                      '5': max(df1.iam5.max(), df1.ibm5.max(), df1.icm5.max()),
                      '7': max(df1.iam7.max(), df1.ibm7.max(), df1.icm7.max()),
                      '9': max(df1.iam9.max(), df1.ibm9.max(), df1.icm9.max()),
                     '11': max(df1.iam11.max(), df1.ibm11.max(), df1.icm11.max()),
                     '13': max(df1.iam13.max(), df1.ibm13.max(), df1.icm13.max()),
                     '15': max(df1.iam15.max(), df1.ibm15.max(), df1.icm15.max()),
                     '17': max(df1.iam17.max(), df1.ibm17.max(), df1.icm17.max()),
                     '19': max(df1.iam19.max(), df1.ibm19.max(), df1.icm19.max()),
                     '21': max(df1.iam21.max(), df1.ibm21.max(), df1.icm21.max()),}
        ithd_gb = (62, 62, 44, 21, 28, 24, 12, 18, 16, 8.9)
        self.ithd_risk = []
        ithd_value = []
        for a, b in zip(self.max_vals2.values(), ithd_gb):
            if a > b:
                ithd_value.append(str(round(a, 1))+'A')
                self.ithd_risk.append(list(self.max_vals2.keys())[list(self.max_vals2.values()).index(a)])
        self.ithd_mv = '、'.join(ithd_value)
        #self.key_name = max(self.max_vals2, key=self.max_vals2.get)
        self.max_vals3 = max(self.max_vals2.values())
        self.min_vals = np.min(df1.PF, axis=0)
        self.max_vals4 = np.max([df1.LF, df1.I_UP], axis=1)
        max_values = (self.max_vals1[0], self.max_vals1[1], self.max_vals1[2], self.max_vals3, self.min_vals,
                      self.max_vals4[0], self.max_vals4[1])
        return max_values

    def quality(self):
        '''
        获取合格率
        :return:
        '''
        df2 = self.add_model()
        freq2 = len(df2.ds)
        qr_u = np.min([len(df2.ix[df2.Ua < 235.4]), len(df2.ix[df2.Ub < 235.4]),
                       len(df2.ix[df2.Uc < 235.4])], axis=0) / freq2
        qr_thdu = np.min([len(df2.ix[df2.Ua_THD < 5]), len(df2.ix[df2.Ub_THD < 5]), len(df2.ix[df2.Uc_THD < 5])],
                         axis=0) / freq2 #单位为%
        ele_n = self.kva * 1.44
        qr_i = np.min([len(df2.ix[df2.Ia < ele_n]), len(df2.ix[df2.Ib < ele_n]),
                       len(df2.ix[df2.Ic < ele_n])], axis=0) / freq2
        self.pf_mean = np.mean(df2.PF, axis=0)
        qr_pf = len(df2.ix[df2.PF >= 0.9]) / freq2
        self.lf_mean = np.mean(df2.LF, axis=0)
        qr_lf = len(df2.ix[df2.LF < 85]) / freq2 #单位为%
        self.unb_max = df2.I_UP.max()
        self.unb_maxtime = df2.ix[df2.I_UP == self.unb_max].ds.values[0]
        qr_unb = len(df2.ix[df2.I_UP <= 15.0]) / freq2
        qrlist = (qr_u, qr_thdu, qr_i, qr_pf, qr_lf, qr_unb)
        return qrlist

    def count_risk(self):
        '''
        获取超标次数
        :return:
        '''
        self.add_model()
        df3 = self.dforignal
        u_risk = np.max([len(df3.query('Ua > 235.4 or Ua < 198')),
                         len(df3.query('Ub > 235.4 or Ub < 198')),
                         len(df3.query('Uc > 235.4 or Uc < 198'))], axis=0)
        u_qr = 1.0 - (u_risk / self.freq)
        i_risk = np.max([len(df3.ix[df3.Ia > (self.kva * 1.44)]),
                         len(df3.ix[df3.Ib > (self.kva * 1.44)]),
                         len(df3.ix[df3.Ic > (self.kva * 1.44)])], axis=0)
        i_qr = 1.0 - (i_risk / self.freq)
        uthd_risk = np.max([len(df3.query('Ua_THD > 5')),
                            len(df3.query('Ub_THD > 5')),
                            len(df3.query('Uc_THD > 5'))], axis=0)
        uthd_qr = 1.0 - (uthd_risk / self.freq)
        pf_risk = len(df3.ix[df3.PF < 0.9])
        pf_qr = 1.0 - (pf_risk / self.freq)
        lf_risk = len(df3.ix[df3.LF > 85])
        lf_qr = 1.0 - (lf_risk / self.freq)
        unb_risk = len(df3.ix[df3.I_UP > 15])
        unb_qr = 1.0 - (unb_risk / self.freq)
        riskamount = (u_risk, uthd_risk, i_risk, pf_risk, lf_risk, unb_risk)
        self.qramount = (u_qr, uthd_qr, i_qr, pf_qr, lf_qr, unb_qr)

        return riskamount

    def group(self):
        self.add_model()
        df = self.dforignal
        df.ds = pd.to_datetime(df.ds, format='%Y-%m-%d %H:%M:%S')
        df4 = df.groupby([pd.Grouper(key='ds', freq='2H')])['Ua', 'Ub', 'Uc', 'Ia', 'Ib', 'Ic',
                'Ua_THD', 'Ub_THD', 'Uc_THD', 'Ia_THD', 'Ib_THD', 'Ic_THD', 'I_UP', 'LF',
                'PF', 'P', 'Q'].mean()
        df4.Ia_THD = df4.Ia_THD * df4.Ia / 100
        df4.Ib_THD = df4.Ib_THD * df4.Ib / 100
        df4.Ic_THD = df4.Ic_THD * df4.Ic / 100
        u_max = max(df4.Ua.max(), df4.Ub.max(), df4.Uc.max())
        u_min = min(df4.Ua.min(), df4.Ub.min(), df4.Uc.min())
        uthd_max = max(df4.Ua_THD.max(), df4.Ub_THD.max(), df4.Uc_THD.max())
        uthd_min = min(df4.Ua_THD.min(), df4.Ub_THD.min(), df4.Uc_THD.min())
        i_max = max(df4.Ia.max(), df4.Ib.max(), df4.Ic.max())
        i_min = min(df4.Ia.min(), df4.Ib.min(), df4.Ic.min())
        ithd_max = max(df4.Ia_THD.max(), df4.Ib_THD.max(), df4.Ic_THD.max())
        ithd_min = min(df4.Ia_THD.min(), df4.Ib_THD.min(), df4.Ic_THD.min())
        pf_max = df4.PF.max()
        pf_min = df4.PF.min()
        lf_max = df4.LF.max()
        lf_min = df4.LF.min()
        unb_max = df4.I_UP.max()
        unb_min = df4.I_UP.min()
        self.max_trend = (u_max, uthd_max, i_max, ithd_max, pf_max, lf_max, unb_max)
        self.min_trend = (u_min, uthd_min, i_min, ithd_min, pf_min, lf_min, unb_min)
        return self.max_trend

class Talk:
    def __init__(self):
        self.untext = ['不合格。', '未达标。', '不达标。', '不理想。']
        self.switchDic = {0: '健康；结果合格。',
                          1: '偶尔超出标准；结果合格。',
                          2: '超标现象明显；结果' + choice(self.untext),
                          3: '超标严重；结果' + choice(self.untext)
                          }
        self.rankDic = {0: 'green',
                        1: 'yellow',
                        2: 'red',
                        3: 'red'}
        self.result = []
    def utalk(self, args):
        if args > 0.92 and args <= 1.0:
            rank = 0
        elif args >0.82 and args <= 0.92:
            rank = 1
        elif args > 0.67 and args <= 0.82:
            rank = 2
        elif args <=0.67:
            rank = 3
        else:
            return None
        self.result.append(self.rankDic[rank])
        return self.switchDic[rank] + '在监测点离变压器较近时，电压值会偏高，在远距离输电时会存在压降，末端电压会' \
                                      '有所下降，合理的提高变压器电压可避免末端回路电压偏低。'

    def uthdtalk(self, args):
        if args > 0.92 and args <= 1.0:
            rank = 0
        elif args >0.82 and args <= 0.92:
            rank = 1
        elif args > 0.67 and args <= 0.82:
            rank = 2
        elif args <=0.67:
            rank = 3
        else:
            return None
        self.result.append(self.rankDic[rank])
        return self.switchDic[rank]

    def pftalk(self, args):
        if args > 0.91 and args <= 1.0:
            rank = 0
        elif args > 0.85 and args <= 0.91:
            rank = 1
        elif args <= 0.85:
            rank = 2
        else:
            return None
        self.result.append(self.rankDic[rank])
        talkDic = {0: '健康且符合要求。',
                   1: '基本符合要求，可能会有力调电费罚款，应加强对功率因数的巡查监管，避免可能带来的经济损失。',
                   2: '不达标，且有较大可能会有力调电费罚款，亟需治理。'}
        return talkDic[rank]

    def unbtalk(self, args):
        if args > 0.95 and args <= 1.0:
            rank = 0
        elif args >0.85 and args <= 0.95:
            rank = 1
        elif args > 0.67 and args <= 0.85:
            rank = 2
        elif args <=0.67:
            rank = 3
        else:
            return None
        self.result.append(self.rankDic[rank])
        return self.switchDic[rank]

    def lftalk(self, args):
        if args <= 85:
            rank = 0
        elif args >85 and args <= 100:
            rank = 1
        elif args > 100:
            rank = 2
        elif args > 110 and args <=150:
            rank = 3
        else:
            return None
        self.result.append(self.rankDic[rank])
        talkDic = {0: '健康且符合要求。',
                   1: '负载较重，超出额定电流的百分之85，应多留意变压器的负载。',
                   2: '不达标，有发生过1级过载现象；负载过大，变压器存在超载隐患，长期如此会对变压器产生损害。',
                   3: '不达标，或是有异常值，异常值一般与现场特殊负载有关；'
                      '或是有2级过载现象，若2级过载，已严重损害变压器；需要尽快排查解决问题。'}
        return talkDic[rank]

    def ithdtalk(self, args):
        if len(args) < 1:
            rank = 0
        elif len(args) >=1 and len(args) <= 2:
            rank = 1
        elif len(args) > 2:
            rank = 2
        else:
            return None
        self.strs = '、'.join(args)
        talkDic = {0: '正常健康；各分次谐波电流皆符合要求。',
                   1: '中以第%s次谐波电流为主，谐波电流不达标。' % self.strs,
                   2: '不达标，有多次谐波电流的最大值超过了标准，分别为第%s次。' % self.strs,}
        self.result.append(self.rankDic[rank])
        return talkDic[rank]



if __name__ == '__main__':
    calc = Calculate()
    talk = Talk()
    calc.calculate()
    quality = calc.quality()
    #print(calc.pf_mean)
    #talk.pftalk(calc.pf_mean)
    conclusion = (talk.utalk(quality[0]), talk.uthdtalk(quality[1]), talk.lftalk(calc.max_vals4[0]),
                  talk.pftalk(calc.pf_mean), talk.lftalk(calc.max_vals4[0]), talk.unbtalk(quality[5]))
    result = talk.result
    print(result)
    calc.count_risk()
    #talk.utalk(quality[0])
    #print(calc.quality())
    #print(calc.freq)

