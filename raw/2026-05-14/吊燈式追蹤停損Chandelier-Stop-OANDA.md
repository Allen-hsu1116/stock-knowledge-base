# 吊燈式追蹤停損（Chandelier stop）

**來源**：https://www.oanda.com/bvi-ft/lab-education/technical_analysis/chandelier-stop/
**日期**：2026-05-14
**主題**：操作策略

---

吊燈式追蹤停損（Chandelier stop）是根據過去一定期間的價格範圍來顯示停損單水平的出場類技術指標。

此追蹤停損的水平是以波動性作為基準，能顯示追隨趨勢下的有效停損水平。

在上升趨勢中停損水準在蠟燭線下方往上移，在下降趨勢中停損在蠟燭線上方往下移，其特徵就是會追隨趨勢走。

## 計算方法

多頭部位的停損：HH - Factor × EMA（Range Length）
空頭部位的停損：LL + Factor × EMA（Range Length）

- HH（Highest High）：多頭部位建倉以後的最高價
- LL（Lowest Low）：空頭部位建倉以後的最低價
- Factor值建議落在2.5～4.0之間
- EMA的週期建議使用10～20
- 若使用ATR，一般使用週期為14

## 特性

- 適合趨勢行情，不適合盤整市況
- 能跟隨趨勢進行停損，在趨勢出現時十分好用
- 空頭部位在市場下滑中雖然幾度出現反彈，但不會在該處清算，最後接觸到停損點時才進行清算

## 關鍵字

- 吊燈停損
- Chandelier Exit
- Chandelier Stop
- ATR
- 追蹤停損
- 出場指標