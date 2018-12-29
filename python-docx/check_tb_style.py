styles = [s for s in document.styles if s.type == WD_STYLE_TYPE.TABLE]
for style in styles:
    print(style.name)
#若是要检查段落和字体类型，就WD_STYLE_TYPE.TABLE改成WD_STYLE_TYPE.PARAGRAPH
