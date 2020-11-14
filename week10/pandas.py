import pandas as pd
import numpy as np
import pymysql
from snownlp import SnowNLP
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:123589@localhost:3306/test_py')

a = pymysql.connect(host='127.0.0.1',
                    port=3306, user='root'
                    , passwd='123589',
                    db='test_py', use_unicode=True,
                    charset="utf8mb4")

sql = "select * from phone_comment"


'''一个用到两份数据，一份是train.csv, 是泰坦尼克号的数据集； 另外一份是female.csv,只存在一个值--femal，用来用join 的操作
这两份数据都导入了数据库，进行sql和pandas的同步处理
'''

df = pd.read_sql(sql, con=a)
''' 2. 处理数据 '''
# 评论行去除列名空格和过行符
df.commnet_text = df.commnet_text.apply(lambda x: np.NaN if str(x).isspace() else x)
#df.columns = df.strip()
df = df[df['commnet_text'].notnull()]
df = df[ ['rank','title', 'commnet_text'] ]


df.dropna()
df.drop_duplicates()
#print(df)

def _sentiment(text):
    s = SnowNLP(text)
    return s.sentiments

def _is_good(num):
    if num >=0.5 :
        return 1
    else: return 0


text = df['commnet_text'].iloc[0]
s = SnowNLP(text)
#print(f'情感倾向: {s.sentiments} , 文本内容: {text}')

df["sentiment"] = df.commnet_text.apply(_sentiment)
df["is_good"] = df.sentiment.apply(_is_good)
print(df.head(10))

order = ['rank', 'title','commnet_text', 'sentiment','is_good']
df = df[order]
#
# df.to_sql('phone_sentiment', engine, index=False)
# print('Read from and write to Mysql table successfully!')

with engine.connect() as conn:
    #rst = conn.execute('DELETE FROM phone_sentiment ')
    pd.io.sql.to_sql(df, "phone_sentiment", con=conn, schema="test_py",if_exists='append',index =True)
    print('Read from and write to Mysql table successfully!')