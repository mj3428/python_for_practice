# Super继承
super()是py的内置函数，可以用来调用父类的方法，这在方法被重载时非常有用，super函数的语法 ：super([type[,object-or-type]])  
用法：  
- 在单继承结构中，super可以隐式地返回父类
- 支持多继承（唯一合理使用多继承）
# 私有化
- 类的私有属性: __private_attrs 两个下划线开头，不能在类的外部使用，内部使用方法：self.__private_attrs    
- 类的私有方法：__private_methods两个下划线开头，不能在类的外部使用，内部使用方法:self.__private_methods    
但也并非完全不能调用，而是用：下划线类名+两个下划线+属性/方法 才能调用  

# 表单form  
表单元素虽然时HTML标签的一种，但不同与其他元素，表单元素提供了浏览器与服务器端交互的功能，是动态网站的重要实现手段。通过表单元素，
用户能够对服务器端数据进行增删改查操作。
表单元素指的是不同类型的input元素，如文本框，单选框，复选框，文件上传按钮等，如<input type="submit" name="confirm" value="提交">

# HTML元素引用CSS样式
两种方法：  
- 使用style属性直接将CSS样式应用在HTML元素上，这种样式表叫作“内联样式Inline style”
  语法：`<element style="property1:value1;property2:value2...propertyN:valueN"/>`property是CSS样式属性名，value是样式属性值。  
- 在HTML元素外部声明CSS样式并应用在元素上
  语法: `selector {property1:value1;property2:value2...propertyN:valueN}`
