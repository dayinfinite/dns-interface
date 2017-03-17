#  dns-interface
> 实现简单ddns api接口
# 调用方式
``` bash 
$ curl -l  -H "Content-Type:application/json" -X POST "http://127.0.0.1:5000/api/dns" -d '{"token":"49a693a","opcode":"del","records":[{"domain":"tmp-20160101.sina.com","ip":"10.89.55.21"}]}'
```
