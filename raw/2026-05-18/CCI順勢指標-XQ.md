# CCI指標 - XQ官方部落格

**來源**：https://www.xq.com.tw/xstrader/cci%E6%8C%87%E6%A8%99/
**日期**：2026-05-18
**主題**：技術分析

---

CCI指標的原文是 Commodity Channel Index，直譯的話就是「商品通道指標」。這個指標是由Donald R. Lamber所發明的。

這個指標的計算過程如下：

1. 先計算出典型價格：TP t = ( 最高價t + 最低價t + 收盤價t ) / 3

2. 求算典型價格的簡單平均值：MA t = ( TPt + TPt-1 + ... + TP t-n+1 ) / n

3. MA t 與TPt 離差絕對值的n日加總：MD t = (|MAt－TPt| + |MAt-1－TPt-1| + ... + |MAt-n+1－TPt-n+1|) / n

4. CCI公式：CCI t = ( TP t－MA t ) / ( 0.015 * MD t )

這個CCI公式的設計，當典型價格等於其平均值時，CCI值會等於零。所以這個公式的原始設計比較像是在使用乖離率的觀念，因為只有當最後股價在極短期內作劇烈的向上或向下運動時，CCI值才會出現突然向上或向下大幅擺盪的極端值。這個公式的發明者為了將CCI指標值限定在一定的範圍內波動，所以特別將分母部份乘上0.015的參數值。

XQ腳本：
```
// XQ: CCI指標
input: Length1(14), Length2(28), Length3(42);
SetInputName(1, "天數一");
SetInputName(2, "天數二");
SetInputName(3, "天數三");
Plot1(CommodityChannel(Length1), "CCI1");
Plot2(CommodityChannel(Length2), "CCI2");
Plot3(CommodityChannel(Length3), "CCI3");
```

---

## 關鍵字

- CCI指標
- 商品通道指標
- 乖離率
- 典型價格
- XQ腳本