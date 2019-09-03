# -*- encoding: utf-8 -*-
"""
@File    : ca_paint.py
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
from ca_detectconf import *


df0 = pd.read_excel(FILENAME,sheet_name='趋势图',index_col=None)
df1 = pd.read_excel(FILENAME,sheet_name='Vh 谐波%',index_col=None)
df2 = pd.read_excel(FILENAME,sheet_name='Ah 谐波RMS',index_col=None)
for files in os.walk('./detect_pic/'):
    for i in range(2, 13):
        if 'Vharm' + str(i) + '.png' in files[2]:
            os.remove('./detect_pic/Vharm' + str(i) + '.png')
        if 'Iharm' + str(i) + '.png' in files[2]:
            os.remove('./detect_pic/Iharm' + str(i) + '.png')

# df0['时间'] = df0['时间'].apply(lambda x: x.replace('上午', 'AM').replace('下午', 'PM'))
# print(df.head(8))
df0['时间'] = df0['时间'].apply(lambda x: arrow.get(x, 'HH:mm:ss').format('HH:mm:ss'))
df1['时间'] = df1['时间'].apply(lambda x: arrow.get(x, 'HH:mm:ss').format('HH:mm:ss'))
df2['时间'] = df2['时间'].apply(lambda x: arrow.get(x, 'HH:mm:ss').format('HH:mm:ss'))
#print(df.head(8))
ithd_gb = (62, 62, 44, 21, 28, 24, 12, 18, 16, 8.9, 14, 12)
#print(df.columns[141: 140])


# print(df.columns)
# 电压构建表与图
# table_trace0 = go.Table(
#     domain=dict(x=[0, 1],
#                 y=[0.7, 1.0]),
#     columnwidth=[1.2, 1.8, 1.8, 1.8],
#     columnorder=[0, 1, 2, 3, 4],
#     header = dict(height = 50,
#                   values = [['<b>项目名称</b>'],['<b>最大值</b>'],
#                             ['<b>最小值</b>'], ['<b>95%概率值</b>']],
#                   line = dict(color='rgb(50, 50, 50)'),
#                   align = ['left'] * 5,
#                   font = dict(color=['rgb(45, 45, 45)'] * 5, size=14),
#                   fill = dict(color='#C764B4')),
#     cells = dict(values = [['A相电压有效值', 'B相电压有效值', 'C相电压有效值'],
#                            np.max([df['Vrms ph-ph AB Avg'], df['Vrms ph-ph BC Avg'], df['Vrms ph-ph CA Avg']],axis=1),
#                            np.min([df['Vrms ph-ph AB Avg'], df['Vrms ph-ph BC Avg'], df['Vrms ph-ph CA Avg']],axis=1),
#                            np.percentile([df['Vrms ph-ph AB Avg'], df['Vrms ph-ph BC Avg'], df['Vrms ph-ph CA Avg']],
#                            95, axis=1)],
#                  line = dict(color='#506784'),
#                  align = ['left'] * 5,
#                  font = dict(color=['rgb(40, 40, 40)'] * 5, size=12),
#                  format = [None] + [", .2f"] * 3,
#                  # prefix = [None] * 2 + ['$', u'\u20BF'], 加前缀
#                  suffix=[None] * 4,
#                  height = 27,
#                  fill = dict(color=['rgb(235, 193, 238)', 'rgba(235, 235, 235, 0.65)']))
# )
# 电压部分
trace0 = go.Scatter(
    x=df0['时间'],
    y=df0['U1 RMS MAX'],
    xaxis='x1',
    yaxis='y1',
    mode='lines',
    line=dict(width=1.5, color='#b04553'),
    showlegend=True,
    name='线电压最大值'
)
trace1 = go.Scatter(
    x=df0['时间'],
    y=df0['U1 RMS MIN'],
    xaxis='x1',
    yaxis='y1',
    mode='lines',
    line=dict(width=1.5, color='#af7bbd'),
    showlegend=True,
    name='线电压最小值'
)
trace2 = go.Scatter(
    x=df0['时间'],
    y=df0['U1 RMS'],
    xaxis='x1',
    yaxis='y1',
    mode='lines',
    line=dict(width=1.5, color='#3182BD'),
    showlegend=True,
    name='线电压平均值'
)

trace3 = go.Scatter(
    x=df0['时间'],
    y=df0['U2 RMS MAX'],
    xaxis='x2',
    yaxis='y2',
    mode='lines',
    line=dict(width=1.5, color='#b04553'),
    showlegend=False,
    name='B相线电压最大值'
)
trace4 = go.Scatter(
    x=df0['时间'],
    y=df0['U2 RMS MIN'],
    xaxis='x2',
    yaxis='y2',
    mode='lines',
    line=dict(width=1.5, color='#af7bbd'),
    showlegend=False,
    name='B相线电压最小值'
)
trace5 = go.Scatter(
    x=df0['时间'],
    y=df0['U2 RMS'],
    xaxis='x2',
    yaxis='y2',
    mode='lines',
    line=dict(width=1.5, color='#3182BD'),
    showlegend=False,
    name='B相线电压平均值'
)
trace6 = go.Scatter(
    x=df0['时间'],
    y=df0['U3 RMS MAX'],
    xaxis='x3',
    yaxis='y3',
    mode='lines',
    line=dict(width=1.5, color='#b04553'),
    showlegend=False,
    name='C相线电压最大值'
)
trace7 = go.Scatter(
    x=df0['时间'],
    y=df0['U3 RMS MIN'],
    xaxis='x3',
    yaxis='y3',
    mode='lines',
    line=dict(width=1.5, color='#af7bbd'),
    showlegend=False,
    name='C相线电压最小值'
)
trace8 = go.Scatter(
    x=df0['时间'],
    y=df0['U3 RMS'],
    xaxis='x3',
    yaxis='y3',
    mode='lines',
    line=dict(width=1.5, color='#3182BD'),
    showlegend=False,
    name='C相线电压平均值'
)
# THD部分
trace9 = go.Scatter(
    x=df0['时间'],
    y=df0['V1 THD'],
    xaxis='x4',
    yaxis='y4',
    mode='lines',
    line=dict(width=1.5, color='MidnightBlue'),
    name='THDU_A相'
)
trace10 = go.Scatter(
    x=df0['时间'],
    y=df0['V2 THD'],
    xaxis='x5',
    yaxis='y5',
    mode='lines',
    line=dict(width=1.5, color='MidnightBlue'),
    name='THDU_B相'
)
trace11 = go.Scatter(
    x=df0['时间'],
    y=df0['V3 THD'],
    xaxis='x6',
    yaxis='y6',
    mode='lines',
    line=dict(width=1.5, color='MidnightBlue'),
    name='THDU_C相'
)
# 功率因数部分

trace14 = go.Scatter(
    x=df0['时间'],
    y=df0['PF1'],
    xaxis='x7',
    yaxis='y7',
    mode='lines',
    line=dict(width=1.5, color='#3182BD'),
    showlegend=True,
    name='功率因数平均值'
)


trace17 = go.Scatter(
    x=df0['时间'],
    y=df0['PF2'],
    xaxis='x8',
    yaxis='y8',
    mode='lines',
    line=dict(width=1.5, color='#3182BD'),
    showlegend=False,
    name='B相功率因数平均值'
)

trace20 = go.Scatter(
    x=df0['时间'],
    y=df0['PF3'],
    xaxis='x9',
    yaxis='y9',
    mode='lines',
    line=dict(width=1.5, color='#3182BD'),
    showlegend=False,
    name='C相功率因数平均值'
)

trace23 = go.Scatter(
    x=df0['时间'],
    y=df0['PF 平均'],
    xaxis='x10',
    yaxis='y10',
    mode='lines',
    line=dict(width=1.5, color='#3182BD'),
    showlegend=False,
    name='总功率因数平均值'
)


# 无功功率部分

trace26 = go.Scatter(
    x=df0['时间'],
    y=df0['var1'],
    xaxis='x11',
    yaxis='y11',
    mode='lines',
    line=dict(width=1.5, color='#3182BD'),
    showlegend=True,
    name='无功功率平均值'
)

trace29 = go.Scatter(
    x=df0['时间'],
    y=df0['var2'],
    xaxis='x12',
    yaxis='y12',
    mode='lines',
    line=dict(width=1.5, color='#3182BD'),
    showlegend=False,
    name='B相无功功率平均值'
)

trace32 = go.Scatter(
    x=df0['时间'],
    y=df0['var3'],
    xaxis='x13',
    yaxis='y13',
    mode='lines',
    line=dict(width=1.5, color='#3182BD'),
    showlegend=False,
    name='C相无功功率平均值'
)

trace35 = go.Scatter(
    x=df0['时间'],
    y=df0['var 合计'],
    xaxis='x14',
    yaxis='y14',
    mode='lines',
    line=dict(width=1.5, color='#3182BD'),
    showlegend=False,
    name='总无功功率平均值'
)
# THD电流部分
trace36 = go.Scatter(
    x=df0['时间'],
    y=df0['A1 THD'],
    xaxis='x15',
    yaxis='y15',
    mode='lines',
    line=dict(width=1.5, color='MidnightBlue'),
    name='THDI_A相'
)
trace37 = go.Scatter(
    x=df0['时间'],
    y=df0['A2 THD'],
    xaxis='x16',
    yaxis='y16',
    mode='lines',
    line=dict(width=1.5, color='MidnightBlue'),
    name='THDI_B相'
)
trace38 = go.Scatter(
    x=df0['时间'],
    y=df0['A3 THD'],
    xaxis='x17',
    yaxis='y17',
    mode='lines',
    line=dict(width=1.5, color='MidnightBlue'),
    name='THDI_C相'
)
# 电流
trace39 = go.Scatter(
    x=df0['时间'],
    y=df0['A1 RMS MAX'],
    xaxis='x18',
    yaxis='y18',
    mode='lines',
    line=dict(width=1.5, color='#b04553'),
    showlegend=True,
    name='电流最大值'
)
trace40 = go.Scatter(
    x=df0['时间'],
    y=df0['A1 RMS MIN'],
    xaxis='x18',
    yaxis='y18',
    mode='lines',
    line=dict(width=1.5, color='#af7bbd'),
    showlegend=True,
    name='电流最小值'
)
trace41 = go.Scatter(
    x=df0['时间'],
    y=df0['A1 RMS'],
    xaxis='x18',
    yaxis='y18',
    mode='lines',
    line=dict(width=1.5, color='#3182BD'),
    showlegend=True,
    name='电流平均值'
)

trace42 = go.Scatter(
    x=df0['时间'],
    y=df0['A2 RMS MAX'],
    xaxis='x19',
    yaxis='y19',
    mode='lines',
    line=dict(width=1.5, color='#b04553'),
    showlegend=False,
    name='B相线电流最大值'
)
trace43 = go.Scatter(
    x=df0['时间'],
    y=df0['A2 RMS MIN'],
    xaxis='x19',
    yaxis='y19',
    mode='lines',
    line=dict(width=1.5, color='#af7bbd'),
    showlegend=False,
    name='B相线电流最小值'
)
trace44 = go.Scatter(
    x=df0['时间'],
    y=df0['A2 RMS'],
    xaxis='x19',
    yaxis='y19',
    mode='lines',
    line=dict(width=1.5, color='#3182BD'),
    showlegend=False,
    name='B相线电流平均值'
)
trace45 = go.Scatter(
    x=df0['时间'],
    y=df0['A3 RMS MAX'],
    xaxis='x20',
    yaxis='y20',
    mode='lines',
    line=dict(width=1.5, color='#b04553'),
    showlegend=False,
    name='C相线电流最大值'
)
trace46 = go.Scatter(
    x=df0['时间'],
    y=df0['A3 RMS MIN'],
    xaxis='x20',
    yaxis='y20',
    mode='lines',
    line=dict(width=1.5, color='#af7bbd'),
    showlegend=False,
    name='C相线电流最小值'
)
trace47 = go.Scatter(
    x=df0['时间'],
    y=df0['A3 RMS'],
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
    cols_a = 'V1h' + str(n)
    cols_b = 'V2h' + str(n)
    cols_c = 'V3h' + str(n)
    maxValue = np.max([df1[cols_a], df1[cols_b], df1[cols_c]])
    if n % 2 == 1 and maxValue > 4:
        mustlist.append(n)
        print('%s次存在' % n)
    if n % 2 == 0 and maxValue > 2:
        mustlist.append(n)
        print('%s次存在' % n)
mustlist = list(set(mustlist))
for i in mustlist:
    cols_a = 'V1h' + str(i)
    cols_b = 'V2h' + str(i)
    cols_c = 'V3h' + str(i)
    thd_ua = go.Scatter(
        x=df1['时间'],
        y=df1[cols_a],
        xaxis='x10' + str(i),
        yaxis='y10' + str(i),
        mode='lines',
        line=dict(width=1.5, color='MidnightBlue'),
        name='A相' + str(i) +'次'
    )
    thd_ub = go.Scatter(
        x=df1['时间'],
        y=df1[cols_b],
        xaxis='x11' + str(i),
        yaxis='y11' + str(i),
        mode='lines',
        line=dict(width=1.5, color='MidnightBlue'),
        name='B相' + str(i) +'次'
    )
    thd_uc = go.Scatter(
        x=df1['时间'],
        y=df1[cols_c],
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
for a,b in zip(range(3, 26, 2), ithd_gb):
    coln_a = '(A)A1h' + str(a)
    coln_b = '(A)A2h' + str(a)
    coln_c = '(A)A3h' + str(a)
    trans_arrray0 = df2[coln_a]
    # print(trans_arrray0)
    trans_arrray1 = df2[coln_b]
    trans_arrray2 = df2[coln_c]
    maxIval = np.max([trans_arrray0, trans_arrray1, trans_arrray2])
    # maxIval = np.max(np.array([df[coln_a], df[coln_b], df[coln_c]]))
    # print(maxIval)
    if maxIval >= b or a in needlist:
        # print(trans_arrray0)
        thd_ia = go.Scatter(
            x=df2['时间'],
            y=trans_arrray0 / 100.0,
            xaxis='x20' + str(a),
            yaxis='y20' + str(a),
            mode='lines',
            line=dict(width=1.5, color='MidnightBlue'),
            name='A相' + str(a) +'次谐波电流'
        )
        thd_ib = go.Scatter(
            x=df2['时间'],
            y=trans_arrray1  / 100.0,
            xaxis='x21' + str(a),
            yaxis='y21' + str(a),
            mode='lines',
            line=dict(width=1.5, color='MidnightBlue'),
            name='B相' + str(a) +'次谐波电流'
        )
        thd_ic = go.Scatter(
            x=df2['时间'],
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
#PF
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
    yaxis7=dict(axis, **dict(domain=[0.69, 0.95], title='AN(PF)', anchor='x7', hoverformat='.2f')),
    yaxis8=dict(axis, **dict(domain=[0.44 + 0.02, 0.67], title='BN(PF)',anchor='x8', hoverformat='.2f')),
    yaxis9=dict(axis, **dict(domain=[0.21+0.02, 2 * 0.21 + 0.02], anchor='x9', title='CN(PF)', hoverformat='.2f')),
    yaxis10=dict(axis, **dict(domain=[0.0, 0.21], anchor='x10', title='合计(PF)', hoverformat='.2f')),
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
    title=dict(text='电流有效值变化趋势图(单位: V)', font=dict(size=20)),
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
fig2 = dict(data=[trace14,  trace17,  trace20, trace23], layout=layout2)
fig3 = dict(data=[trace26, trace29, trace32, trace35], layout=layout3)
fig4 = dict(data=[trace36, trace37, trace38], layout=layout4)
fig5 = dict(data=[trace39, trace40, trace41, trace42, trace43, trace44, trace45,
                  trace46, trace47], layout=layout5)
pio.write_image(fig0, './detect_pic/Virms_line.png', scale=3)
pio.write_image(fig1, './detect_pic/THDU.png', scale=3)
pio.write_image(fig2, './detect_pic/cos_phi.png', scale=3)
pio.write_image(fig3, './detect_pic/reactive.png', scale=3)
pio.write_image(fig4, './detect_pic/THDI.png', scale=3)
pio.write_image(fig5, './detect_pic/current.png', scale=3)
