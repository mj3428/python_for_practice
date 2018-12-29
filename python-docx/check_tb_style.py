styles = [s for s in document.styles if s.type == WD_STYLE_TYPE.TABLE]
for style in styles:
    print(style.name)
