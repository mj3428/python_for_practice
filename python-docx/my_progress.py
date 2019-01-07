#!/usr/bin/env python
# encoding: utf-8
'''
@author: mj
@contact: major3428@foxmail.com
@software: pycharm
@file: test.py
@time: 2018-10-16 下午 2:54
@desc:
'''

from docx import Document
from docx.shared import Cm, RGBColor, Inches
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.enum.style import WD_STYLE_TYPE
from docx.shared import Pt

from docx.shared import Inches
import numpy as np
import pandas as pd
from docx.oxml.ns import qn
import datetime


#参数配置
com_name = '恒生印染' #公司名
transformer = '东1#' #变压器名
KVA = 1600000 #变压器容量
startday = '2018年11月23日' #起始时间
endday = '2018年12月4日' #结束时间
freq = 1085 #数据条数
highrisk = 99 #高危数
hiddenrisk = 120 #隐患数
now = datetime.datetime.now() #当前时间的datetime
document = Document('./text/demo.docx')

#开始写
#for i in range(0,5):
    #document.add_paragraph('')
#pic = document.add_picture('./pic/poweryun.png', height=Cm(3.43), width=Cm(9.83))
#南德电气1.82×6.07 电能卫士3.43×9.83
#last_paragraph = document.paragraphs[-1]
#last_paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER  # 图片居中设置

style_T1 = document.styles.add_style('T1', WD_STYLE_TYPE.PARAGRAPH) #创建T1样式
style_T1.paragraph_format.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER #居中
document.styles['T1'].font.name = u'宋体' #T1样式使用字体
document.styles['T1']._element.rPr.rFonts.set(qn('w:eastAsia'), u'宋体')
document.styles['T1'].font.size = Pt(26)
document.styles['T1'].font.bold = True

style_T2 = document.styles.add_style('T2', WD_STYLE_TYPE.PARAGRAPH) #创建T2样式
style_T2.paragraph_format.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER #居中
document.styles['T2'].font.name = u'宋体' #T2样式使用字体
document.styles['T2']._element.rPr.rFonts.set(qn('w:eastAsia'), u'宋体')
document.styles['T2'].font.size = Pt(22)
document.styles['T2'].font.bold = True

document.paragraphs[10].style = 'T1'
document.paragraphs[10].add_run(text=com_name+'有限公司')
document.paragraphs[11].clear()
document.paragraphs[11].style = 'T2'
document.paragraphs[11].add_run(text=transformer+'变压器')
document.paragraphs[12].style = 'T2'
document.paragraphs[12].add_run(text='电能健康分析评估报告\n')

#插入印章
#picture = document.add_picture('./pic/poweryun_seal.png', height=Cm(4.00), width=Cm(4.32))
#创建日期样式
style_D1 = document.styles.add_style('Date1', WD_STYLE_TYPE.PARAGRAPH) #创建Date1样式
style_D1.paragraph_format.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER #居中
document.styles['Date1'].font.name = u'宋体' #T1样式使用字体
document.styles['Date1']._element.rPr.rFonts.set(qn('w:eastAsia'), u'宋体')
document.styles['Date1'].font.size = Pt(14)
document.paragraphs[14].clear()
document.paragraphs[14].style = 'Date1'
document.paragraphs[14].add_run(text=now.strftime('%Y')+'年 '+now.strftime('%m')+'月')

#document.add_page_break() #插入分页符
last = document.paragraphs[-1]
last.style = 'Heading 1'
last.add_run(text='一、监测概况及问题')
document.add_heading('1.1电能参数体检结果', level=2)
result = ['—', '↑', '↑', '↑', '—', '↑', '—']
max_value = ['243.9V', '10.1%', '98.6%', '730A', '0.96', '113.5%', '11.9%']
records = (('电压数据', result[0], max_value[0], '205~235V', '《GB/T 12325-2008》'),
          ('谐波电压数据', result[1], max_value[1], '＜5%', '《GB/T14549-1993》'),
          ('电流数据', result[2], max_value[2], '＜In100%', '《JGJ16-2008》'),
          ('谐波电流数据', result[3], max_value[3], '＜各分次国标限值', 'GB/T14549-1993》'),
          ('功率因数', result[4], max_value[4], '0.9~1.0', '《JGJ16-2008》'),
          ('负荷率', result[5], max_value[5], '＜额定容量85%', '《JGJ16-2008》'),
          ('三相电流不平衡度', result[6], max_value[6], '＜15%', '《GB/T 1094-2013》'))
table = document.add_table(rows=1, cols=5)
hdr_cells = table.rows[0].cells
hdr_cells[0].text = '体检项目'
hdr_cells[1].text = '体检结果'
hdr_cells[2].text = '体检值(MAX)'
hdr_cells[3].text = '参考值'
hdr_cells[4].text = '参考标准'
for sty, res, mv, ran, txt in records:
    row_cells = table.add_row().cells
    row_cells[0].text = sty
    row_cells[1].text = res
    row_cells[2].text = mv
    row_cells[3].text = ran
    row_cells[4].text = txt

widths = [3.99, 2.64, 3.15, 3.53, 4.11]
for i in range(0, 5):
    for cell in table.columns[i].cells:
        cell.width = Cm(widths[i])

for i in range(0, 8):
    for j in range(0, 5):
        cell = table.cell(i, j)
        cell_font = cell.paragraphs[0].runs[0].font
        cell_font.color.rgb = RGBColor(0x36, 0x5f, 0x91)
        cell.paragraphs[0].paragraph_format.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
        cell.paragraphs[0].paragraph_format.left_indent = -Cm(1.0)
#cell.font.color.rgb = RGBColor(0x36, 0x5f, 0x91)
table.style = 'ListCLF'
note = document.add_paragraph("注：（1）‘", style='N1')
fine = note.add_run("—")
fine.bold = True
fine.font.name = 'Arial'
fine.font.color.rgb = RGBColor(0x00, 0xB0, 0x50)
goon = document.paragraphs[-1].add_run("’为标准内，‘")
high = document.paragraphs[-1].add_run("↑")
high.bold = True
high.font.size = Pt(12)
high.font.color.rgb = RGBColor(0xff, 0x00, 0x00)
document.paragraphs[-1].add_run("’为超出标准，‘")
medium = document.paragraphs[-1].add_run("↑")
medium.bold = True
medium.font.size = Pt(12)
medium.font.color.rgb = RGBColor(0xff, 0xff, 0x00)
document.paragraphs[-1].add_run("’为已达临界标准")
document.add_paragraph("（2）以上依据原始导出数据分析，见附件一或用户由平台自行导出", style='N1')
document.add_heading('1.2体检结论说明', level=2)
document.add_paragraph('此结论为%s变压器体检结果，' % transformer +
                        '变压器容量为%dKVA。' % (KVA / 1000) +
                       '%s到%s共采集了%d次数据，高危共计%d次，隐患共120次。' % (startday, endday, highrisk, hiddenrisk) +
                       '以各体检项目在该时段内发生次数及超出各项标准次数进行分析得出：', style='Normal')
document.add_paragraph().add_run('电压体检结论：').bold = True
document.paragraphs[-1].add_run('该变压器在此数据时段内电压值偶尔超出标准，电压数据基本符合要求；' 
                                '谐波电压含量80%以上都超出标准，电网谐波电压含量不合格；')
document.add_paragraph().add_run('电流体检结论：').bold = True
document.paragraphs[-1].add_run('变压器低压侧电流值基本在左右，' 
                                '偶尔会超出变压器额定电流值超载运行，基本属于重载情况；' 
                                '各分次最大谐波电流值都有明显超出标准情况，在均值下5次、7次、11次超出标准，谐波电流不合格；')
document.add_paragraph().add_run('功率因数体检结论：').bold = True
document.paragraphs[-1].add_run('功率因数在0.9~1之间的占比为XX%，功率因数保持良好，功率因数合格；')
document.add_paragraph().add_run('负荷率体检结论：').bold = True
document.paragraphs[-1].add_run('该变压器容量为XXKVA，额定电流约XXA，' 
                                '变压器负荷率基本在XX%左右运行，已超出标准限值，' 
                                '监测期间有发生1级过载（100%~110%）和2级过载（110%~150%），' 
                                '如变压器长期在此状态下工作将会发生安全隐患，变压器负荷率较大；')
document.add_paragraph().add_run('三相电流不平衡体检结论：').bold = True
document.paragraphs[-1].add_run('三相电流不平衡度均在15%以内，概率为XX%，' 
                                '在XX月XX号XX分时发生过一次23%的情况，此时为用电负荷大量下降，' 
                                '属于小电流短暂超标，三相电流不平衡度达标。')
document.add_paragraph().add_run('注：本报告分析数据来源为XXXX年XX月XX日到XXXX年XX月XX日的监测数据。' 
                                 '共采集了XX次（正常情况下15分钟为一个周期点，异常情况即时事件推送）。').bold = True
document.add_page_break() #插入分页符
document.add_heading('1.3体检不正常项目说明', level=2)
document.add_heading('1.3.1谐波电压', level=3)
document.add_paragraph('...')
document.add_heading('1.3.2谐波电流', level=3)
document.add_paragraph('...')
document.add_page_break() #插入分页符
document.add_heading('二、专项体检数据分析说明', level=2)
document.add_paragraph('数据点为%s变压器，变压器容量%dKVA。'% (transformer, KVA / 1000) +
                       '从%s到%s共采集了%d次数据，'%(startday, endday, freq) +
                       '结合各项标准，此时段内存在谐波电压含量、谐波电流含量、负荷率超标隐患。' 
                       '此时段电压数据超出标准限值约XX次；谐波电压含量超出标准限值约XX次；'
                       '电流超出变压器额定电流值约XX次；功率因数超出标准限值约XX次；'
                       '变压器负荷率85%以上约XX次；三相电流不平衡超出标准限值XX次。', style='Normal')
document.add_heading('2.1电压数据', level=2)
document.add_heading('2.1.1 电压数据体检分析', level=3)
document.add_paragraph('根据国家标准《GB/T 12325-2008》中规定单相220V供电电压允许偏差为标称系统电压的+7％、-10%。'
                       '由此计算出电压标准上限值为235.4V。从以下分析中可以看出A、B、C三相电压达标率为XX%左右，基本符合标准。')
document.add_paragraph('1）电压趋势图', level=4)

document.save('./text/test.docx')
