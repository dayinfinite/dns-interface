#  dns-interface
> 实现简单ddns api接口
# 调用方式
``` bash
$ curl -l  -H "Content-Type:application/json" -X POST "http://127.0.0.1:5000/api/dns" -d '{"token":"49a693a","opcode":"del","records":[{"domain":"tmp-20160101.test.com","ip":"172.16.3.22"}]}'
```

## 1. 接口说明

调用方法： POST
调用地址： http://127.0.0.1:5000/api/dns

数据传输采用post json body方式：
```json
{
  "token":"49a693a",
  "opcode":"DEL",
  "records":{"domain":"tmp.test.com","ip":"172.16.3.134"}
}

action 为可以提供的操作

新增： ADD
删除： DEL
```

## 2. 数据返回格式
```json
{
  "msg": "success",
  "reason": "",
  "status": "200"
}
```
### 2.1 status_code说明

- 200 --> 操作成功
- 400 --> 提交数据格式不正确
- 403 --> 权限不足
- 500 --> 请求错误

### 2.2 msg说明

说明操作是否成功

### 2.3 reason说明

操作成功为空，操作失败，说明失败原因
