#修改单元格内的段落及字体

#方法1
cell = table.cell(0, 0)
cell.text = 'Shift'
cell_font = cell.text_frame.paragraphs[0].runs[0].font
cell_font.size = Pt(10)

#方法2
cells[0].text = 'Some text'   #Write the text to the cell
#Modify the paragraph alignment, 
first paragraph cells[0].paragraphs[0].paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
#or
row_cells[0].text = ''
row_cells[0].paragraphs[0].add_run('Total').bold = True
row_cells[0].paragraphs[0].paragraph_format.alignment = WD_ALIGN_PARAGRAPH.RIGHT
