# -*- encoding: utf-8 -*-
"""
@File    : autopaint.py
@Time    : 2019-7-4 上午 10:22
@Author  : major
@Email   : major3428@foxmail.com
@Software: PyCharm
"""


import plotly.io as pio
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.offline as pltoff
import numpy as np
import pandas as pd
import arrow
import os
from detectconf import *


df = pd.read_excel(FILENAME, index_col=None)
for files in os.walk('./detect_pic/'):
    for i in range(2, 26):
        if 'Vharm' + str(i) + '.png' in files[2]:
            os.remove('./detect_pic/Vharm' + str(i) + '.png')
        if 'Iharm' + str(i) + '.png' in files[2]:
            os.remove('./detect_pic/Iharm' + str(i) + '.png')

print(df.head(10))
df['Time'] = df['Time'].apply(lambda x: x.replace('上午', 'AM').replace('下午', 'PM'))
# print(df.head(8))
df['Time'] = df['Time'].apply(lambda x: arrow.get(x, 'A H:mm:ss.S').format('HH:mm:ss'))
print(df.head(8))
ithd_gb = (62, 39, 62, 26, 44, 19, 21, 16, 28, 13, 24, 11, 12, 9.7, 18, 8.6, 16, 7.8, 8.9, 7.1, 14, 6.5, 12)
#print(df.columns[141: 140])
# df['Time'] = pd.to_datetime(df['Time'], format='%H:%M')

# 电压部分
trace0 = go.Scatter(
    x=df['Time'],
    y=df['Vrms ph-ph AB Max'],
    xaxis='x1',
    yaxis='y1',
    mode='lines',
    line=dict(width=1.5, color='#b04553'),
    showlegend=True,
    name='线电压最大值'
)
trace1 = go.Scatter(
    x=df['Time'],
    y=df['Vrms ph-ph AB Min'],
    xaxis='x1',
    yaxis='y1',
    mode='lines',
    line=dict(width=1.5, color='#af7bbd'),
    showlegend=True,
    name='线电压最小值'
)
trace2 = go.Scatter(
    x=df['Time'],
    y=df['Vrms ph-ph AB Avg'],
    xaxis='x1',
    yaxis='y1',
    mode='lines',
    line=dict(width=1.5, color='#3182BD'),
    showlegend=True,
    name='线电压平均值'
)

trace3 = go.Scatter(
    x=df['Time'],
    y=df['Vrms ph-ph BC Max'],
    xaxis='x2',
    yaxis='y2',
    mode='lines',
    line=dict(width=1.5, color='#b04553'),
    showlegend=False,
    name='B相线电压最大值'
)
trace4 = go.Scatter(
    x=df['Time'],
    y=df['Vrms ph-ph BC Min'],
    xaxis='x2',
    yaxis='y2',
    mode='lines',
    line=dict(width=1.5, color='#af7bbd'),
    showlegend=False,
    name='B相线电压最小值'
)
trace5 = go.Scatter(
    x=df['Time'],
    y=df['Vrms ph-ph BC Avg'],
    xaxis='x2',
    yaxis='y2',
    mode='lines',
    line=dict(width=1.5, color='#3182BD'),
    showlegend=False,
    name='B相线电压平均值'
)
trace6 = go.Scatter(
    x=df['Time'],
    y=df['Vrms ph-ph CA Max'],
    xaxis='x3',
    yaxis='y3',
    mode='lines',
    line=dict(width=1.5, color='#b04553'),
    showlegend=False,
    name='C相线电压最大值'
)
trace7 = go.Scatter(
    x=df['Time'],
    y=df['Vrms ph-ph CA Min'],
    xaxis='x3',
    yaxis='y3',
    mode='lines',
    line=dict(width=1.5, color='#af7bbd'),
    showlegend=False,
    name='C相线电压最小值'
)
trace8 = go.Scatter(
    x=df['Time'],
    y=df['Vrms ph-ph CA Avg'],
    xaxis='x3',
    yaxis='y3',
    mode='lines',
    line=dict(width=1.5, color='#3182BD'),
    showlegend=False,
    name='C相线电压平均值'
)
# THD部分
trace9 = go.Scatter(
    x=df['Time'],
    y=df['THD V AN Avg'],
    xaxis='x4',
    yaxis='y4',
    mode='lines',
    line=dict(width=1.5, color='MidnightBlue'),
    name='THDU_A相'
)
trace10 = go.Scatter(
    x=df['Time'],
    y=df['THD V BN Avg'],
    xaxis='x5',
    yaxis='y5',
    mode='lines',
    line=dict(width=1.5, color='MidnightBlue'),
    name='THDU_B相'
)
trace11 = go.Scatter(
    x=df['Time'],
    y=df['THD V CN Avg'],
    xaxis='x6',
    yaxis='y6',
    mode='lines',
    line=dict(width=1.5, color='MidnightBlue'),
    name='THDU_C相'
)
# 功率因数部分
trace12 = go.Scatter(
    x=df['Time'],
    y=df['Cos Phi AN Max'],
    xaxis='x7',
    yaxis='y7',
    mode='lines',
    line=dict(width=1.5, color='#b04553'),
    showlegend=True,
    name='功率因数最大值'
)
trace13 = go.Scatter(
    x=df['Time'],
    y=df['Cos Phi AN Min'],
    xaxis='x7',
    yaxis='y7',
    mode='lines',
    line=dict(width=1.5, color='#af7bbd'),
    showlegend=True,
    name='功率因数最小值'
)
trace14 = go.Scatter(
    x=df['Time'],
    y=df['Cos Phi AN Avg'],
    xaxis='x7',
    yaxis='y7',
    mode='lines',
    line=dict(width=1.5, color='#3182BD'),
    showlegend=True,
    name='功率因数平均值'
)

trace15 = go.Scatter(
    x=df['Time'],
    y=df['Cos Phi BN Max'],
    xaxis='x8',
    yaxis='y8',
    mode='lines',
    line=dict(width=1.5, color='#b04553'),
    showlegend=False,
    name='B相功率因数最大值'
)
trace16 = go.Scatter(
    x=df['Time'],
    y=df['Cos Phi BN Min'],
    xaxis='x8',
    yaxis='y8',
    mode='lines',
    line=dict(width=1.5, color='#af7bbd'),
    showlegend=False,
    name='B相功率因数最小值'
)
trace17 = go.Scatter(
    x=df['Time'],
    y=df['Cos Phi BN Avg'],
    xaxis='x8',
    yaxis='y8',
    mode='lines',
    line=dict(width=1.5, color='#3182BD'),
    showlegend=False,
    name='B相功率因数平均值'
)
trace18 = go.Scatter(
    x=df['Time'],
    y=df['Cos Phi CN Max'],
    xaxis='x9',
    yaxis='y9',
    mode='lines',
    line=dict(width=1.5, color='#b04553'),
    showlegend=False,
    name='C相功率因数最大值'
)
trace19 = go.Scatter(
    x=df['Time'],
    y=df['Cos Phi CN Min'],
    xaxis='x9',
    yaxis='y9',
    mode='lines',
    line=dict(width=1.5, color='#af7bbd'),
    showlegend=False,
    name='C相功率因数最小值'
)
trace20 = go.Scatter(
    x=df['Time'],
    y=df['Cos Phi CN Avg'],
    xaxis='x9',
    yaxis='y9',
    mode='lines',
    line=dict(width=1.5, color='#3182BD'),
    showlegend=False,
    name='C相功率因数平均值'
)
trace21 = go.Scatter(
    x=df['Time'],
    y=df['Cos Phi Total Max'],
    xaxis='x10',
    yaxis='y10',
    mode='lines',
    line=dict(width=1.5, color='#b04553'),
    showlegend=False,
    name='总功率因数最大值'
)
trace22 = go.Scatter(
    x=df['Time'],
    y=df['Cos Phi Total Min'],
    xaxis='x10',
    yaxis='y10',
    mode='lines',
    line=dict(width=1.5, color='#af7bbd'),
    showlegend=False,
    name='总功率因数最小值'
)
trace23 = go.Scatter(
    x=df['Time'],
    y=df['Cos Phi Total Avg'],
    xaxis='x10',
    yaxis='y10',
    mode='lines',
    line=dict(width=1.5, color='#3182BD'),
    showlegend=False,
    name='总功率因数平均值'
)


# 无功功率部分
trace24 = go.Scatter(
    x=df['Time'],
    y=df['Reactive Power AN Max'],
    xaxis='x11',
    yaxis='y11',
    mode='lines',
    line=dict(width=1.5, color='#b04553'),
    showlegend=True,
    name='无功功率最大值'
)
trace25 = go.Scatter(
    x=df['Time'],
    y=df['Reactive Power AN Min'],
    xaxis='x11',
    yaxis='y11',
    mode='lines',
    line=dict(width=1.5, color='#af7bbd'),
    showlegend=True,
    name='无功功率最小值'
)
trace26 = go.Scatter(
    x=df['Time'],
    y=df['Reactive Power AN Avg'],
    xaxis='x11',
    yaxis='y11',
    mode='lines',
    line=dict(width=1.5, color='#3182BD'),
    showlegend=True,
    name='无功功率平均值'
)

trace27 = go.Scatter(
    x=df['Time'],
    y=df['Reactive Power BN Max'],
    xaxis='x12',
    yaxis='y12',
    mode='lines',
    line=dict(width=1.5, color='#b04553'),
    showlegend=False,
    name='B相无功功率最大值'
)
trace28 = go.Scatter(
    x=df['Time'],
    y=df['Reactive Power BN Min'],
    xaxis='x12',
    yaxis='y12',
    mode='lines',
    line=dict(width=1.5, color='#af7bbd'),
    showlegend=False,
    name='B相无功功率最小值'
)
trace29 = go.Scatter(
    x=df['Time'],
    y=df['Reactive Power BN Avg'],
    xaxis='x12',
    yaxis='y12',
    mode='lines',
    line=dict(width=1.5, color='#3182BD'),
    showlegend=False,
    name='B相W无功功率平均值'
)
trace30 = go.Scatter(
    x=df['Time'],
    y=df['Reactive Power CN Max'],
    xaxis='x13',
    yaxis='y13',
    mode='lines',
    line=dict(width=1.5, color='#b04553'),
    showlegend=False,
    name='C相无功功率最大值'
)
trace31 = go.Scatter(
    x=df['Time'],
    y=df['Reactive Power CN Min'],
    xaxis='x13',
    yaxis='y13',
    mode='lines',
    line=dict(width=1.5, color='#af7bbd'),
    showlegend=False,
    name='C相无功功率最小值'
)
trace32 = go.Scatter(
    x=df['Time'],
    y=df['Reactive Power CN Avg'],
    xaxis='x13',
    yaxis='y13',
    mode='lines',
    line=dict(width=1.5, color='#3182BD'),
    showlegend=False,
    name='C相无功功率平均值'
)
trace33 = go.Scatter(
    x=df['Time'],
    y=df['Reactive Power Total Max'],
    xaxis='x14',
    yaxis='y14',
    mode='lines',
    line=dict(width=1.5, color='#b04553'),
    showlegend=False,
    name='总无功功率最大值'
)
trace34 = go.Scatter(
    x=df['Time'],
    y=df['Reactive Power Total Min'],
    xaxis='x14',
    yaxis='y14',
    mode='lines',
    line=dict(width=1.5, color='#af7bbd'),
    showlegend=False,
    name='总无功功率最小值'
)
trace35 = go.Scatter(
    x=df['Time'],
    y=df['Reactive Power Total Avg'],
    xaxis='x14',
    yaxis='y14',
    mode='lines',
    line=dict(width=1.5, color='#3182BD'),
    showlegend=False,
    name='总无功功率平均值'
)
# THD电流部分
trace36 = go.Scatter(
    x=df['Time'],
    y=df['THD A A Avg'],
    xaxis='x15',
    yaxis='y15',
    mode='lines',
    line=dict(width=1.5, color='MidnightBlue'),
    name='THDI_A相'
)
trace37 = go.Scatter(
    x=df['Time'],
    y=df['THD A B Avg'],
    xaxis='x16',
    yaxis='y16',
    mode='lines',
    line=dict(width=1.5, color='MidnightBlue'),
    name='THDI_B相'
)
trace38 = go.Scatter(
    x=df['Time'],
    y=df['THD A C Avg'],
    xaxis='x17',
    yaxis='y17',
    mode='lines',
    line=dict(width=1.5, color='MidnightBlue'),
    name='THDI_C相'
)
# 电流
trace39 = go.Scatter(
    x=df['Time'],
    y=df['Current A Max'],
    xaxis='x18',
    yaxis='y18',
    mode='lines',
    line=dict(width=1.5, color='#b04553'),
    showlegend=True,
    name='电流最大值'
)
trace40 = go.Scatter(
    x=df['Time'],
    y=df['Current A Min'],
    xaxis='x18',
    yaxis='y18',
    mode='lines',
    line=dict(width=1.5, color='#af7bbd'),
    showlegend=True,
    name='电流最小值'
)
trace41 = go.Scatter(
    x=df['Time'],
    y=df['Current A Avg'],
    xaxis='x18',
    yaxis='y18',
    mode='lines',
    line=dict(width=1.5, color='#3182BD'),
    showlegend=True,
    name='电流平均值'
)

trace42 = go.Scatter(
    x=df['Time'],
    y=df['Current B Max'],
    xaxis='x19',
    yaxis='y19',
    mode='lines',
    line=dict(width=1.5, color='#b04553'),
    showlegend=False,
    name='B相线电流最大值'
)
trace43 = go.Scatter(
    x=df['Time'],
    y=df['Current B Min'],
    xaxis='x19',
    yaxis='y19',
    mode='lines',
    line=dict(width=1.5, color='#af7bbd'),
    showlegend=False,
    name='B相线电流最小值'
)
trace44 = go.Scatter(
    x=df['Time'],
    y=df['Current B Avg'],
    xaxis='x19',
    yaxis='y19',
    mode='lines',
    line=dict(width=1.5, color='#3182BD'),
    showlegend=False,
    name='B相线电流平均值'
)
trace45 = go.Scatter(
    x=df['Time'],
    y=df['Current C Max'],
    xaxis='x20',
    yaxis='y20',
    mode='lines',
    line=dict(width=1.5, color='#b04553'),
    showlegend=False,
    name='C相线电流最大值'
)
trace46 = go.Scatter(
    x=df['Time'],
    y=df['Current C Min'],
    xaxis='x20',
    yaxis='y20',
    mode='lines',
    line=dict(width=1.5, color='#af7bbd'),
    showlegend=False,
    name='C相线电流最小值'
)
trace47 = go.Scatter(
    x=df['Time'],
    y=df['Current C Avg'],
    xaxis='x20',
    yaxis='y20',
    mode='lines',
    line=dict(width=1.5, color='#3182BD'),
    showlegend=False,
    name='C相线电流平均值'
)

axis=dict(
    showline=True,
    zeroline=False,
    showgrid=True,
    mirror=True,
    ticklen=4,
    gridcolor='#ffffff',
    tickfont=dict(size=10)
)
#谐波电压分次
mustlist = [3, 5, 7]# 必画次数
for n in range(2, 12):
    cols_a = 'Volts Harmonics' + str(n) + ' AN Avg'
    cols_b = 'Volts Harmonics' + str(n) + ' BN Avg'
    cols_c = 'Volts Harmonics' + str(n) + ' CN Avg'
    maxValue = np.max([df[cols_a], df[cols_b], df[cols_c]])
    if n % 2 == 1 and maxValue > 4:
        mustlist.append(n)
        print('%s次存在' % n)
    if n % 2 == 0 and maxValue > 2:
        mustlist.append(n)
        print('%s次存在' % n)
mustlist = list(set(mustlist))
for i in mustlist:
    cols_a = 'Volts Harmonics' + str(i) + ' AN Avg'
    cols_b = 'Volts Harmonics' + str(i) + ' BN Avg'
    cols_c = 'Volts Harmonics' + str(i) + ' CN Avg'
    thd_ua = go.Scatter(
        x=df['Time'],
        y=df[cols_a],
        xaxis='x10' + str(i),
        yaxis='y10' + str(i),
        mode='lines',
        line=dict(width=1.5, color='MidnightBlue'),
        name='A相' + str(i) +'次'
    )
    thd_ub = go.Scatter(
        x=df['Time'],
        y=df[cols_b],
        xaxis='x11' + str(i),
        yaxis='y11' + str(i),
        mode='lines',
        line=dict(width=1.5, color='MidnightBlue'),
        name='B相' + str(i) +'次'
    )
    thd_uc = go.Scatter(
        x=df['Time'],
        y=df[cols_c],
        xaxis='x12' + str(i),
        yaxis='y12' + str(i),
        mode='lines',
        line=dict(width=1.5, color='MidnightBlue'),
        name='C相' + str(i) +'次'
    )

    lay = dict(
        width=1799,
        height=1088,
        autosize=False,
        title=dict(text=str(i) + '次电压谐波含有率(单位:%)', font=dict(size=20)),
        margin = dict(t=40),
        showlegend=False,
        plot_bgcolor='rgba(235, 235, 235, 0.65)'
    )
    lay['xaxis10'+str(i)] =dict(axis, **dict(domain=[0, 1], anchor='y10'+str(i), showticklabels=False))
    lay['xaxis11'+str(i)] = dict(axis, **dict(domain=[0, 1], anchor='y11'+str(i), showticklabels=False))
    lay['xaxis12'+str(i)] = dict(axis, **dict(domain=[0, 1], anchor='y12'+str(i)))
    lay['yaxis10'+str(i)] = dict(axis, **dict(domain=[2 * 0.30 + 0.02 + 0.02, 0.95], title='AN H1(%)',
                                                   anchor='x10'+str(i), hoverformat='.2f'))
    lay['yaxis11'+str(i)] = dict(axis, **dict(domain=[0.30 + 0.02, 2 * 0.30 + 0.02], title='BN H1(%)',
                                                      anchor='x11'+str(i), hoverformat='.2f'))
    lay['yaxis12'+str(i)] = dict(axis, **dict(domain=[0.0, 0.30], anchor='x12'+str(i),
                                                      title='CN H1(%)', hoverformat='.2f'))
    figthd = dict(data=[thd_ua, thd_ub, thd_uc], layout=lay)
    pio.write_image(figthd, './detect_pic/Vharm' + str(i) +'.png', scale=3)
#谐波电流分次
needlist = (3, 5, 7)
maxIval = {}
for a,b in zip(range(3, 26, 1), ithd_gb):
    coln_a = 'Amps Harmonics' + str(a) + ' A Avg'
    coln_b = 'Amps Harmonics' + str(a) + ' B Avg'
    coln_c = 'Amps Harmonics' + str(a) + ' C Avg'
    trans_arrray0 = np.array(df[coln_a] * df['Current A Avg'])
    # print(trans_arrray0)
    trans_arrray1 = np.array(df[coln_b] * df['Current B Avg'])
    trans_arrray2 = np.array(df[coln_c] * df['Current C Avg'])
    maxIval = np.max([trans_arrray0, trans_arrray1, trans_arrray2]) / 100.0
    # maxIval = np.max(np.array([df[coln_a], df[coln_b], df[coln_c]]))
    # print(maxIval)
    if maxIval >= b or a in needlist:
        # print(trans_arrray0)
        thd_ia = go.Scatter(
            x=df['Time'],
            y=trans_arrray0 / 100.0,
            xaxis='x20' + str(a),
            yaxis='y20' + str(a),
            mode='lines',
            line=dict(width=1.5, color='MidnightBlue'),
            name='A相' + str(a) +'次谐波电流'
        )
        thd_ib = go.Scatter(
            x=df['Time'],
            y=trans_arrray1  / 100.0,
            xaxis='x21' + str(a),
            yaxis='y21' + str(a),
            mode='lines',
            line=dict(width=1.5, color='MidnightBlue'),
            name='B相' + str(a) +'次谐波电流'
        )
        thd_ic = go.Scatter(
            x=df['Time'],
            y=trans_arrray2  / 100.0,
            xaxis='x22' + str(a),
            yaxis='y22' + str(a),
            mode='lines',
            line=dict(width=1.5, color='MidnightBlue'),
            name='C相' + str(a) +'次谐波电流'
            )

        layo = dict(
            width=1799,
            height=1088,
            autosize=False,
            title=dict(text=str(a) + '次谐波电流(单位:A)', font=dict(size=20)),
            margin = dict(t=40),
            showlegend=False,
            plot_bgcolor='rgba(235, 235, 235, 0.65)'
            )
        layo['xaxis20'+str(a)] =dict(axis, **dict(domain=[0, 1], anchor='y20'+str(a), showticklabels=False))
        layo['xaxis21'+str(a)] = dict(axis, **dict(domain=[0, 1], anchor='y21'+str(a), showticklabels=False))
        layo['xaxis22'+str(a)] = dict(axis, **dict(domain=[0, 1], anchor='y22'+str(a)))
        layo['yaxis20'+str(a)] = dict(axis, **dict(domain=[2 * 0.30 + 0.02 + 0.02, 0.95], title='AN rms(A)',
                                                       anchor='x20'+str(a), hoverformat='.2f'))
        layo['yaxis21'+str(a)] = dict(axis, **dict(domain=[0.30 + 0.02, 2 * 0.30 + 0.02], title='BN rms(A)',
                                                          anchor='x21'+str(a), hoverformat='.2f'))
        layo['yaxis22'+str(a)] = dict(axis, **dict(domain=[0.0, 0.30], anchor='x22'+str(a),
                                                          title='CN rms(A)', hoverformat='.2f'))
        figthdi = dict(data=[thd_ia, thd_ib, thd_ic], layout=layo)
        pio.write_image(figthdi, './detect_pic/Iharm' + str(a) +'.png', scale=3)


#U
layout0 = dict(
    width=1799,
    height=1088,
    autosize=False,
    title=dict(text='电压有效值变化趋势图(单位: V)', font=dict(size=20)),
    margin = dict(t=40),
    # showlegend=True,
    xaxis1=dict(axis, **dict(domain=[0, 1], anchor='y1', showticklabels=False),), # 显示x轴的刻度labels
    xaxis2=dict(axis, **dict(domain=[0, 1], anchor='y2', showticklabels=False)),
    xaxis3=dict(axis, **dict(domain=[0, 1], anchor='y3')),
    yaxis1=dict(axis, **dict(domain=[2 * 0.30 + 0.02 + 0.02, 0.95], title='AB(V)', anchor='x1', hoverformat='.2f')),
    yaxis2=dict(axis, **dict(domain=[0.30 + 0.02, 2 * 0.30 + 0.02], title='BC(V)',anchor='x2', hoverformat='.2f')),
    # tickprefix='$' 轴前加上单位
    yaxis3=dict(axis, **dict(domain=[0.0, 0.30], anchor='x3', title='CA(V)', hoverformat='.2f')),
    # tickprefix=u'\u20BF' 轴前加上单位
    plot_bgcolor='rgba(235, 235, 235, 0.65)'
)
#THDU
layout1 = dict(
    width=1799,
    height=1088,
    autosize=False,
    # title=dict(text='电容器投入时电压谐波THDU总含有率变化趋势图(单位:%)', font=dict(size=20)),
    margin = dict(t=40),
    showlegend=False,
    xaxis4=dict(axis, **dict(domain=[0, 1], anchor='y4', showticklabels=False),), # 显示x轴的刻度labels
    xaxis5=dict(axis, **dict(domain=[0, 1], anchor='y5', showticklabels=False)),
    xaxis6=dict(axis, **dict(domain=[0, 1], anchor='y6')),
    yaxis4=dict(axis, **dict(domain=[2 * 0.30 + 0.02 + 0.02, 0.95], title='AN H1(%)', anchor='x4', hoverformat='.2f')),
    yaxis5=dict(axis, **dict(domain=[0.30 + 0.02, 2 * 0.30 + 0.02], title='BN H1(%)',anchor='x5', hoverformat='.2f')),
    yaxis6=dict(axis, **dict(domain=[0.0, 0.30], anchor='x6', title='CN H1(%)', hoverformat='.2f')),
    plot_bgcolor='rgba(235, 235, 235, 0.65)'
)
#COS PHI
layout2 = dict(
    width=1799,
    height=1088,
    autosize=False,
    title=dict(text='功率因数值变化趋势图', font=dict(size=20)),
    margin = dict(t=40),
    # showlegend=True,
    xaxis7=dict(axis, **dict(domain=[0, 1], anchor='y7', showticklabels=False),), # 显示x轴的刻度labels
    xaxis8=dict(axis, **dict(domain=[0, 1], anchor='y8', showticklabels=False)),
    xaxis9=dict(axis, **dict(domain=[0, 1], anchor='y9', showticklabels=False)),
    xaxis10=dict(axis, **dict(domain=[0, 1], anchor='y10')),
    yaxis7=dict(axis, **dict(domain=[0.69, 0.95], title='AN(cosφ)', anchor='x7', hoverformat='.2f')),
    yaxis8=dict(axis, **dict(domain=[0.44 + 0.02, 0.67], title='BN(cosφ)',anchor='x8', hoverformat='.2f')),
    yaxis9=dict(axis, **dict(domain=[0.21+0.02, 2 * 0.21 + 0.02], anchor='x9', title='CN(cosφ)', hoverformat='.2f')),
    yaxis10=dict(axis, **dict(domain=[0.0, 0.21], anchor='x10', title='合计(cosφ)', hoverformat='.2f')),
    # tickprefix=u'\u20BF' 轴前加上单位
    plot_bgcolor='rgba(235, 235, 235, 0.65)'
    )
# Reactive Power
layout3 = dict(
    width=1799,
    height=1088,
    autosize=False,
    title=dict(text='无功功率值变化趋势图', font=dict(size=20)),
    margin = dict(t=40),
    # showlegend=True,
    xaxis11=dict(axis, **dict(domain=[0, 1], anchor='y11', showticklabels=False),), # 显示x轴的刻度labels
    xaxis12=dict(axis, **dict(domain=[0, 1], anchor='y12', showticklabels=False)),
    xaxis13=dict(axis, **dict(domain=[0, 1], anchor='y13', showticklabels=False)),
    xaxis14=dict(axis, **dict(domain=[0, 1], anchor='y14')),
    yaxis11=dict(axis, **dict(domain=[0.69, 0.95], title='AN(kvar)', anchor='x11', hoverformat='.2f')),
    yaxis12=dict(axis, **dict(domain=[0.44 + 0.02, 0.67], title='BN(kvar)',anchor='x12', hoverformat='.2f')),
    yaxis13=dict(axis, **dict(domain=[0.21+0.02, 2 * 0.21 + 0.02], anchor='x13', title='CN(kvar)', hoverformat='.2f')),
    yaxis14=dict(axis, **dict(domain=[0.0, 0.21], anchor='x14', title='合计(kvar)', hoverformat='.2f')),
    # tickprefix=u'\u20BF' 轴前加上单位
    plot_bgcolor='rgba(235, 235, 235, 0.65)'
    )
# THDI
layout4 = dict(
    width=1799,
    height=1088,
    autosize=False,
    title=dict(text='电流谐波总含有率变化趋势图(单位:%)', font=dict(size=20)),
    margin = dict(t=40),
    showlegend=False,
    xaxis15=dict(axis, **dict(domain=[0, 1], anchor='y15', showticklabels=False),), # 显示x轴的刻度labels
    xaxis16=dict(axis, **dict(domain=[0, 1], anchor='y16', showticklabels=False)),
    xaxis17=dict(axis, **dict(domain=[0, 1], anchor='y17')),
    yaxis15=dict(axis, **dict(domain=[2 * 0.30 + 0.02 + 0.02, 0.95], title='AN H1(%)', anchor='x15', hoverformat='.2f')),
    yaxis16=dict(axis, **dict(domain=[0.30 + 0.02, 2 * 0.30 + 0.02], title='BN H1(%)',anchor='x16', hoverformat='.2f')),
    yaxis17=dict(axis, **dict(domain=[0.0, 0.30], anchor='x17', title='CN H1(%)', hoverformat='.2f')),
    plot_bgcolor='rgba(235, 235, 235, 0.65)'
)
# I
layout5 = dict(
    width=1799,
    height=1088,
    autosize=False,
    title=dict(text='电流有效值变化趋势图(单位: A)', font=dict(size=20)),
    margin = dict(t=40),
    # showlegend=True,
    xaxis18=dict(axis, **dict(domain=[0, 1], anchor='y18', showticklabels=False),), # 显示x轴的刻度labels
    xaxis19=dict(axis, **dict(domain=[0, 1], anchor='y19', showticklabels=False)),
    xaxis20=dict(axis, **dict(domain=[0, 1], anchor='y20')),
    yaxis18=dict(axis, **dict(domain=[2 * 0.30 + 0.02 + 0.02, 0.95], title='A(A)', anchor='x18', hoverformat='.2f')),
    yaxis19=dict(axis, **dict(domain=[0.30 + 0.02, 2 * 0.30 + 0.02], title='B(A)',anchor='x19', hoverformat='.2f')),
    yaxis20=dict(axis, **dict(domain=[0.0, 0.30], anchor='x20', title='C(A)', hoverformat='.2f')),
    # tickprefix=u'\u20BF' 轴前加上单位
    plot_bgcolor='rgba(235, 235, 235, 0.65)'
)
# data = [table_trace0, trace0, trace1, trace2]
fig0 = dict(data=[trace0, trace1, trace2, trace3, trace4, trace5,
                  trace6, trace7, trace8], layout=layout0)
fig1 = dict(data=[trace9, trace10, trace11], layout=layout1)
fig2 = dict(data=[trace12, trace13, trace14, trace15, trace16, trace17, trace18,
                  trace19, trace20, trace21, trace22, trace23], layout=layout2)
fig3 = dict(data=[trace24, trace25, trace26, trace27, trace28, trace29, trace30,
                  trace31, trace32, trace33, trace34, trace35], layout=layout3)
fig4 = dict(data=[trace36, trace37, trace38], layout=layout4)
fig5 = dict(data=[trace39, trace40, trace41, trace42, trace43, trace44, trace45,
                  trace46, trace47], layout=layout5)
pio.write_image(fig0, './detect_pic/Virms_line.png', scale=3)
pio.write_image(fig1, './detect_pic/THDU.png', scale=3)
pio.write_image(fig2, './detect_pic/cos_phi.png', scale=3)
pio.write_image(fig3, './detect_pic/reactive.png', scale=3)
pio.write_image(fig4, './detect_pic/THDI.png', scale=3)
pio.write_image(fig5, './detect_pic/current.png', scale=3)
