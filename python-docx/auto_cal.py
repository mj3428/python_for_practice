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

class Calculate:
    def __init__(self, path=PATH, kva=KVA):
        self.path = path
        self.kva = kva
        self.ele = ELECTRIC[str(kva)]

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
        A2 = df1.Ib
        df1['ibm3'], df1['ibm5'] = A2 * df1.Ib_H3 / 100, A2 * df1.Ib_H5 / 100
        df1['ibm7'], df1['ibm9'] = A2 * df1.Ib_H7 / 100, A2 * df1.Ib_H9 / 100
        A3 = df1.Ic
        df1['icm3'], df1['icm5'] = A3 * df1.Ic_H3 / 100, A3 * df1.Ic_H5 / 100
        df1['icm7'], df1['icm9'] = A3 * df1.Ic_H7 / 100, A3 * df1.Ic_H9 / 100
        max_vals2 = {'A3': df1.iam3.max(), 'A5': df1.iam5.max(), 'A7': df1.iam7.max(), 'A9':df1.iam9.max(),
                     'B3': df1.ibm3.max(), 'B5': df1.ibm5.max(), 'B7': df1.ibm7.max(), 'B9':df1.ibm9.max(),
                     'C3': df1.icm3.max(), 'C5': df1.icm5.max(), 'C7': df1.icm7.max(), 'C9': df1.icm9.max()}
        self.key_name = max(max_vals2, key=max_vals2.get)
        self.max_vals3 = max(max_vals2.values())
        self.min_vals = np.min(df1.PF, axis=0)
        self.max_vals4 = np.max([df1.LF, df1.I_UP], axis=1)
        max_values = (self.max_vals1[0], self.max_vals1[1], self.max_vals1[2], self.max_vals3, self.min_vals,
                      self.max_vals4[0], self.max_vals4[1])
        return max_values

    def quality(self):
        '''
        合格率
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
        qr_pf = len(df2.ix[df2.PF >= 0.9]) / freq2
        qr_lf = len(df2.ix[df2.LF < 85]) / freq2 #单位为%
        qrlist = (qr_u, qr_thdu, qr_i, qr_lf, qr_pf)
        

if __name__ == '__main__':
    calc = Calculate()
    #calc.calculate()
    calc.quality()
    #print(calc.freq)

