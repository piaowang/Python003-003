import pandas as pd
import pymysql

a = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123589', db='test_py', use_unicode=True,
                    charset="utf8mb4")

sql = 'select * from train'
sql1 = 'select * from female'

'''一个用到两份数据，一份是train.csv, 是泰坦尼克号的数据集； 另外一份是female.csv,只存在一个值--femal，用来用join 的操作
这两份数据都导入了数据库，进行sql和pandas的同步处理
'''

train = pd.read_sql(sql, con=a)
gril_sex =  pd.read_sql(sql1, con=a)
# print(train)

# 1. SELECT * FROM data;
# print(train[:])

# 2. SELECT * FROM data LIMIT 10;
# print(train[:].head(10))

# 3. SELECT id FROM data;  //id 是 data 表的特定一列
# print(train['Fare'].head(10))

# 4. SELECT COUNT(id) FROM data;
# print(train['Fare'].count())

# 5. SELECT * FROM data WHERE id<1000 AND age>30;
# tips[(tips['time'] == 'Dinner') & (tips['tip'] > 5.00)]
'''
train = train.fillna(0)
train['Age']= train['Age'].astype("float64")
#train.info()
print(train[(train['Age'] > 20) & (train['Age'] < 30)])
'''

#6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
#print(train.groupby('Sex')['Pclass'].nunique())

#7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
#print(gril_sex)
#print(pd.merge(train, gril_sex, left_on='Sex',right_on='Gril_sex'))

#8. SELECT * FROM table1 UNION SELECT * FROM table2;
'''
train_a = train['Sex']
train_b = train['Sex']
train_c = pd.concat([train_a,train_b]).drop_duplicates()
print(train_a.size)
print(train_c.size)

'''


#9. DELETE FROM table1 WHERE id=10;
#删除操作可以细分为删除行的操作和删除列的操作。对于删除行操作，pandas的删除行可以转换为选择不符合条件进行操作
#print(train[train['Embarked']!='C'])

#10. ALTER TABLE table1 DROP COLUMN column_name;
#对于删除列的操作。pandas需要使用drop方法
print(train.drop(['Embarked'],inplace=True,axis=1))
print(train)