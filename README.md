### Reference
Please go to official help documentation from [here.](https://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1472017492_58YV5)
### Prerequisite

1. apply an server instance. 
2. 安装/更新需要用到的软件:

- 安装python2.7版本以上 

- ==python3.x is not supported==

- 安装web.py

- 安装libxml2, libxslt, lxml python

3. In file `handle.py` please take care below code, token should be replaced by value you specified:
```python
    def GET(self):
        try:
            data = web.input()
            if len(data) == 0:
                return "hello, this is handle view"
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            token = "xxxx" #请按照公众平台官网\基本配置中信息填写

```
### Usage
Clone file into your home package in server, and run below code in shell:
`sudo python main.py 80`, other ports is not supported.

