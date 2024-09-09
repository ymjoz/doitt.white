# unittest

> 如何使用測試
> 來源: [碼農高天介紹如何寫測試](https://youtu.be/n6DljHXv1do?si=W_7_hORfLZddXFU-)

## one

```bash
py -m unittest -v # 看細一點,也可以不加上-v
```

- 指定測試特定function

```bash
py -m unittest tests.test_risk.TestRisk.test_init -v
```

```bash
py -m unittest tests.test_risk.TestRisk.test_add_numbers -v
```

```bash
py -m unittest tests.test_risk # 指定測試test_risk 這個python
```

## two,使用coverage

- coverage 命令
  
```bash
pip install coverage
```

- coverage 命令示例

```bash
coverage run -m unittest -v # 測試覆蓋率且看細一點
coverage report # 看測試報告
```
