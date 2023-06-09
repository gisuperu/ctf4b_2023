# CoughingFox2

### 概要
暗号化されたフラグを暗号化プログラムや`cipher`とかを参考に復号する．
#### 与えられるもの
- cipher.txt : (cipher配列)
- main.py : 暗号化プログラム

---
## 解法
main.pyでフラグは文字ごとにbinaryに変換されて点数2の移動合計を取ったのち2乗してindexを加算し，得られた数値配列をシャッフルして`cipher`としている．
```
for i in range(len(flag)-1):
    c = ((flag[i] + flag[i+1]) ** 2 + i)
    cipher.append(c)

random.shuffle(cipher)
```
そのため以下の手順で復号していく
1. `cipher`の順番を戻す
2. 移動合計の配列に戻す
3. もとのフラグに戻す

### 1. `cipher`の順番を戻す
`cipher`で0から`len(cipher)`までの数字を引いた値が平方数であるかを確認してソートする(一応平方数になるcipher[i]が複数あったらどれが相応しいか全体で確認する必要があるが今回は複数なかったため省略)

### 2. 移動合計の配列に戻す
ソート済みになった`cipher`に対して平方根取ったりとかindex引いたりして移動合計の配列にする．

### 3. もとのフラグに戻す
フラグのフォーマットが`ctf4b{}`になっているため先頭文字が`c`とわかる．
そこから`c`をASCIIに直した後の10進数の値`99`を求めて，`99`を起点として全ての文字を10進数で復号していく．
最後に文字列にエンコードしてフラグを得る．

----