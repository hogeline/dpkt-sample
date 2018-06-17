# dpkt-sample
dpktを使ったパケット解析を行うプログラムです．
入力はpcapファイル，出力は通信元と通信先，送信データをターミナル上に表示します．

### 実行方法
dpktのインストール方法

```
$ wget https://github.com/kbandla/dpkt/archive/v1.9.0.tar.gz
$ tar zxvf v1.9.0.tar.gz
$ sudo python3 setup.py build
$ sudo python3 setup.py install
```

サンプルプログラム実行方法

```
$ python3 pcapAnalyze.py
```

実行結果

```
> 1.1.23.3 to 1.1.12.1 : 63527 [Byte]
> 1.1.12.1 to 1.1.23.3 : 117702 [Byte]
```

このように実行されれば成功です．
