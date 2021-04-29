import urllib.request
import urllib.parse
import json

# 发送 GET 请求
url = "https://api.bilibili.com/x/web-interface/ranking/v2"
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    data = response.read()
    json_data = data.decode()
    # print(json_data)
    data_dict = json.loads(json_data)
    print('响应状态', data_dict['code'])
    print('响应消息', data_dict['message'])
    print('响应数据', data_dict['data'])

# 下载图片
url = "https://i0.hdslb.com/bfs/vc/b24c872ae1ef34ebe794d1631a50b57fbdb0a482.png"
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    data = response.read()
    f_name = 'download.png'
    with open(f_name, 'wb') as f:
        f.write(data)
        print('下载图片成功')

# 发送 POST 请求
param_dict = {'rid': '0', 'type': 'all'}
# url编码
param_str = urllib.parse.urlencode(param_dict)
print(param_str)    # name=bob&id=10
# 转换为字节序列
param_bytes = param_str.encode()

req = urllib.request.Request(url, data=param_bytes)  # 发送POST请求
with urllib.request.urlopen(req) as response:
    data = response.read()
    json_data = data.decode()
    # print(json_data)