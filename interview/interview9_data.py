'''
MySQL索引种类
MySQL目前主要有以下几种索引类型：
1.普通索引
2.唯一索引
3.主键索引
4.组合索引
5.全文索引
CREATE TABLE table_name[col_name data type]
[unique|fulltext][index|key][index_name](col_name[length])[asc|desc]
1.unique|fulltext为可选参数，分别表示唯一索引、全文索引
2.index和key为同义词，两者作用相同，用来指定创建索引
3.col_name为需要创建索引的字段列，该列必须从数据表中该定义的多个列中选择
4.index_name指定索引的名称，为可选参数，如果不指定，默认col_name为索引值
5.length为可选参数，表示索引的长度，只有字符串类型的字段才能指定索引长度
6.asc或desc指定升序或降序的索引值存储
1.普通索引
（1）直接创建索引 CREATE INDEX index_name ON table(column(length)
2.唯一索引
与前面的普通索引类似，不同的就是：索引列的值必须唯一，但允许有空值。如果是组合索引，则列值的组合必须唯一
（1）创建唯一索引 CREATE UNIQUE INDEX indexName ON table(column(length))
3.主键索引
是一种特殊的唯一索引，一个表只能有一个主键，不允许有空值。一般是在建表的时候同时创建主键索引：
CREATE TABLE `table` (
    `id` int(11) NOT NULL AUTO_INCREMENT ,
    `title` char(255) NOT NULL ,
    PRIMARY KEY (`id`)
);
4.组合索引
指多个字段上创建的索引，只有在查询条件中使用了创建索引时的第一个字段，索引才会被使用。使用组合索引时遵循最左前缀集合
ALTER TABLE `table` ADD INDEX name_city_age (name,city,age); 
5.全文索引
主要用来查找文本中的关键字，而不是直接与索引中的值相比较。fulltext索引跟其它索引大不相同，它更像是一个搜索引擎，而不是简单的where语句的参数匹配。
fulltext索引配合match against操作使用，而不是一般的where语句加like。
它可以在create table，alter table ，create index使用，不过目前只有char、varchar，text 列上可以创建全文索引。
值得一提的是，在数据量较大时候，现将数据放入一个没有全局索引的表中，
然后再用CREATE index创建fulltext索引，要比先为一张表建立fulltext然后再将数据写入的速度快很多。
（1）创建表的适合添加全文索引
CREATE TABLE `table` (
    `id` int(11) NOT NULL AUTO_INCREMENT ,
    `title` char(255) CHARACTER NOT NULL ,
    `content` text CHARACTER NULL ,
    `time` int(10) NULL DEFAULT NULL ,
    PRIMARY KEY (`id`),
    FULLTEXT (content)
);


索引在什么情况下遵循最左前缀的规则？
我们想在a,b,c三个字段上建立一个联合索引，我们可以选择自己想要的优先级，a、b、c,或者是b、a、c 或者是c、a、b等顺序。
为什么数据库会让我们选择字段的顺序呢？不都是三个字段的联合索引么？这里就引出了数据库索引的最左前缀原理.
索引index1:(a,b,c)有三个字段，我们在使用sql语句来查询的时候，会发现很多情况下不按照我们想象的来走索引.
select * from table where c = '1'          这个sql语句是不会走index1索引的
select * from table where b =‘1’ and c ='2' 这个语句也不会走index1索引。
什么语句会走index1索引呢？
select * from table where a = '1'  
select * from table where a = '1' and b = ‘2’  
select * from table where a = '1' and b = ‘2’  and c='3'
索引index1:(a,b,c)，只会走a、a,b、a,b,c 三种类型的查询，其实这里说的有一点问题，a,c也走，但是只走a字段索引，不会走c字段
特殊情况说明下，select * from table where a = '1' and b > ‘2’  and c='3' 这种类型的也只会有a与b走索引，c不会走
原因如下：
索引是有序的，index1索引在索引文件中的排列是有序的，首先根据a来排序，然后才是根据b来排序，最后是根据c来排序，
像select * from table where a = '1' and b > ‘2’  and c='3' 这种类型的sql语句，在a、b走完索引后，c肯定是无序了，所以c就没法走索引


主键和外键的区别？
定义主键和外键主要是为了维护关系数据库的完整性，总结一下：
1.主键是能确定一条记录的唯一标识，比如，一条记录包括身份正号，姓名，年龄。

身份证号是唯一能确定你这个人的，其他都可能有重复，所以，身份证号是主键。 
2.外键用于与另一张表的关联。是能确定另一张表记录的字段，用于保持数据的一致性。


MySQL常见的函数？
https://blog.csdn.net/sinat_38899493/article/details/78710482


列举 创建索引但是无法命中索引的8种情况？
1、如果条件中有or，即使其中有条件带索引也不会使用(这也是为什么尽量少用or的原因）
   注意：要想使用or，又想让索引生效，只能将or条件中的每个列都加上索引
2、对于多列索引，不是使用的第一部分(第一个)，则不会使用索引
3、like查询是以%开头
4、如果列类型是字符串，那一定要在条件中将数据使用引号引用起来,否则不使用索引
5、如果mysql估计使用全表扫描要比使用索引快,则不使用索引
6-8、其他略


如何开启慢日志查询？
有2种方式，一是修改mysql的配置文件，二是通过set global语句来实现。
1、修改配置文件，Windows 的配置文件为 my.ini，一般在 MySQL 的安装目录下。linux 的配置文件为my.cnf ，一般在 /etc 目录下。

在linux下，vim /etc/my.cnf，在[mysqld]内容项下增加
slow_query_log = ON
long_query_time = 2
我这里设置慢查询时间long_query_time 设置的是2s，认为超过2秒即为慢查询

2、二是通过set global语句来实现，可以在mysql -uroot -p登录后，输入：
SET GLOBAL slow_query_log = 'ON';
就可以立即开始慢日志记录，如果想指定时间和文件位置，可以追加配置：
SET GLOBAL long_query_time = X;
X默认是10s，也就是说超过10s的查询会被记入慢日志。


数据库导入导出命令（结构+数据）？
1,导出dbname库所有表结构
mysqldump -uroot -ppasswd -d dbname >db.sql;

2,导出dbname库test表结构
mysqldump -uroot -ppasswd -d dbname test>db.sql;

3,导出dbname库结构和数据
mysqldump -uroot -ppasswd  dbname >db.sql;

4,导出dbname库test表结构和数据
mysqldump -uroot -ppasswd dbname test>db.sql;
(以上均为操作系统命令,不是mysql命令)


数据库优化方案？
https://blog.csdn.net/u013628152/article/details/82184809


数据库中char与varchar类型的区别
在建立数据库表结构的时候，为了给一个String类型的数据定义一个数据库的数据库类型，一般参考的都是char或者varchar，
这两种选择有时候让人很纠结，今天想总结一下它们两者的区别，明确一下两者的区别。

首先明确的是，char的长度是不可变的，而varchar的长度是可变的，也就是说，
定义一个char[10]和varchar[10],如果存进去的是‘csdn’,那么char所占的长度依然为10，除了字符‘csdn’外，
后面跟六个空格，而varchar就立马把长度变为4了，取数据的时候，char类型的要用trim()去掉多余的空格，而varchar是不需要的。

尽管如此，char的存取数度还是要比varchar要快得多，因为其长度固定，方便程序的存储与查找；
但是char也为此付出的是空间的代价，因为其长度固定，所以难免会有多余的空格占位符占据空间，可谓是以空间换取时间效率，而varchar是以空间效率为首位的。

再者，char的存储方式是，对英文字符（ASCII）占用1个字节，对一个汉字占用两个字节；
而varchar的存储方式是，对每个英文字符占用2个字节，汉字也占用2个字节。
两者的存储数据都非unicode的字符数据。


Mysql的执行计划
https://www.cnblogs.com/xinysu/p/7860609.html


在对name做了唯一索引前提下，简述以下区别： 
select * from tb where name = ‘Oldboy-Wupeiqi’ 
select * from tb where name = ‘Oldboy-Wupeiqi’ limit 1

在mysql中limit可以实现快速分页，但是如果数据到了几百万时我们的limit必须优化才能有效的合理的实现分页了，否则可能卡死你的服务器哦。
当一个表数据有几百万的数据的时候成了问题！
如 * from table limit 0,10 这个没有问题 当 limit 200000,10 的时候数据读取就很慢，可以按照一下方法解决第一页会很快
当一个数据库表过于庞大，LIMIT offset, length中的offset值过大，则SQL查询语句会非常缓慢，你需增加order by，并且order by字段需要建立索引。
如果使用子查询去优化LIMIT的话，则子查询必须是连续的，某种意义来讲，子查询不应该有where条件，where会过滤数据，使数据失去连续性。
如果你查询的记录比较大，并且数据传输量比较大，比如包含了text类型的field，则可以通过建立子查询。
SELECT id,title,content FROM items WHERE id IN (SELECT id FROM items ORDER BY id limit 900000, 10);
如果limit语句的offset较大，你可以通过传递pk键值来减小offset = 0，这个主键最好是int类型并且auto_increment
SELECT * FROM users WHERE uid > 456891 ORDER BY uid LIMIT 0, 10;

这条语句，大意如下:
SELECT * FROM users WHERE uid >=  (SELECT uid FROM users ORDER BY uid limit 895682, 1) limit 0, 10;
如果limit的offset值过大，用户也会翻页疲劳，你可以设置一个offset最大的，超过了可以另行处理，一般连续翻页过大，
用户体验很差，则应该提供更优的用户体验给用户。


