## 关于dataframe中条件筛选中的速度
一定是布尔型的数组查询筛选更快  
少用.apply及for loop循环  
且ix会比loc更快  
尽可能使用生成器
