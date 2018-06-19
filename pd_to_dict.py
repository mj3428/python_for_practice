#对group by后的内容进行操作，如转换成字典

piece=dict(list(df.groupby('key1')))
piece

{'a':       data1     data2 key1 key2
 0 -0.233405 -0.756316    a  one
 1 -0.232103 -0.095894    a  two
 4  1.056224  0.736629    a  one, 'b':       data1     data2 key1 key2
 2  0.200875  0.598282    b  one
 3 -1.437782  0.107547    b  two}

piece['a']


#groupby默认是在axis=0上进行分组的，通过设置也可以在其他任何轴上进行分组.
df = pd.DataFrame({'key1':list('aabba'),
                  'key2': ['one','two','one','two','one'],
                  'data1': np.random.randn(5),
                  'data2': np.random.randn(5)})
df
grouped=df.groupby(df.dtypes, axis=1)
dict(list(grouped))

{dtype('float64'):       data1     data2
 0 -0.233405 -0.756316
 1 -0.232103 -0.095894
 2  0.200875  0.598282
 3 -1.437782  0.107547
 4  1.056224  0.736629, dtype('O'):   key1 key2
 0    a  one
 1    a  two
 2    b  one
 3    b  two
 4    a  one
 

#axis=0代表列，axis=1代表行

#换句话说：

#使用0值表示沿着每一列或行标签\索引值向下执行方法
#使用1值表示沿着每一行或者列标签模向执行对应的方法

#详情链接：https://blog.csdn.net/youngbit007/article/details/54288603
