# Super继承
super()是py的内置函数，可以用来调用父类的方法，这在方法被重载时非常有用，super函数的语法 ：super([type[,object-or-type]])  
用法：  
- 在单继承结构中，super可以隐式地返回父类
- 支持多继承（唯一合理使用多继承）
# 私有化
- 类的私有属性: __private_attrs 两个下划线开头，不能在类的外部使用，内部使用方法：self.__private_attrs  
- 类的私有方法：__private_methods两个下划线开头，不能在类的外部使用，内部使用方法:self.__private_methods  
但也并非完全不能调用，而是用：下划线类名+两个下划线+属性/方法 才能调用
