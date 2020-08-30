# 这里仅以python为例子，其他语言都类似的，仅需http get请求接口即可
import requests
import  random
import json

#获取代理ip
targetUrl = "http://piping.mogumiao.com/proxy/api/get_ip_al?appKey=564f926cdc724d4f9eff46a451da392c&count=20&expiryDate=0&format=1&newLine=2"

resp = requests.get(targetUrl).text
print(resp)
ip = json.loads(resp)["msg"]
#print(type(ip))
ip_l = []
for i in ip:
    #print(i)
    ip_l.append('{}:{}'.format(i["ip"], i['port']))

print(ip_l)
with open('proxies.txt', 'a') as f:
    for proxy in ip_l:
        f.write('http://'+proxy + '\n')
#
# IPPOOL=[
#     {"ipaddr":"61.129.70.131:8080"},
#     {"ipaddr":"61.152.81.193:9100"},
#     {"ipaddr":"120.204.85.29:3128"},
#     {"ipaddr":"219.228.126.86:8123"},
#     {"ipaddr":"61.152.81.193:9100"},
#     {"ipaddr":"218.82.33.225:53853"},
#     {"ipaddr":"223.167.190.17:42789"}
# ]
# try:
#     print(IPPOOL["ipadder"])
# except Exception as e:
#     print(e)
# print(random.choice(IPPOOL)["ipaddr"])
import json

'''
dumps()：将字典转换为JSON格式的字符串
loads()：将JSON格式的字符串转化为字典
dump() ：将字典转换为JSON格式的字符串，并将转化后的结果写入文件
load() ：从文件读取JSON格式的字符串，并将其转化为字典


d1 = {'父亲': '张三', '母亲': '李四', '子女': {'老大': '张五', '老二': '张六'}}

print("\n字典：\n")
print(d1)

# 将字典转换为JSON格式的字符串
j1 = json.dumps(d1, ensure_ascii=False, indent=2)
print("\n将字典转换为JSON格式的字符串：\n")
print(j1)

# 将JSON格式的字符串转换为字典
d2 = json.loads(j1)
print("\n将JSON格式的字符串转换为字典：\n")
print(d2)

# 将字典内容保存为JSON格式的文件
filename = 'test1.json'
with open(filename, 'w', encoding='UTF-8') as f:
    json.dump(d1, f, ensure_ascii=False, indent=2)

# 读取JSON格式文件的内容并转换为字典
with open(filename, 'r', encoding='UTF-8') as f:
    d3 = json.load(f)
print("\n读取JSON格式文件的内容并转换为字典：\n")
print(d3)


'''