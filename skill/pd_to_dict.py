对group by后的内容进行操作，如转换成字典

piece=dict(list(df.groupby('key1')))
piece

{'a':       data1     data2 key1 key2
 0 -0.233405 -0.756316    a  one
 1 -0.232103 -0.095894    a  two
 4  1.056224  0.736629    a  one, 'b':       data1     data2 key1 key2
 2  0.200875  0.598282    b  one
 3 -1.437782  0.107547    b  two}


piece['a']
