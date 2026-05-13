# 選擇權 Greeks 進階組合判讀與風險管理

**來源**：知識庫整合 + 實戰經驗彙編
**日期**：2026-05-10
**主題**：操作策略 - 選擇權 Greeks 進階

---

## Greeks 進階組合判讀

### Delta-Gamma 二維判讀

單看 Delta 只知道「現在的敏感度」，加上 Gamma 才知道「未來敏感度怎麼變」。

**關鍵公式**：新 Delta ≈ 舊 Delta + Gamma × 價格變動量

實例：
- 大盤 20000，ATM Call Delta=0.5, Gamma=0.005
- 大盤漲 200 點 → 新 Delta ≈ 0.5 + 0.005 × 200 = 1.5
- 等等，0.005 是每點 Gamma，200 點變動太大需要拆分
- 實際：每漲 10 點 Delta 變 0.05，漲 100 點後 Delta ≈ 0.5 + 0.005×100 ≈ 0.55
- 這就是「Delta 跑起來了」——買方越賺越快

**Delta-Gamma 矩陣**：

| 位置 | Delta | Gamma | 解讀 |
|------|-------|-------|------|
| 深價內 | ≈1.0 | 極小 | 像期貨，方向確定但加速空間有限 |
| 價平 | ≈0.5 | 最大 | 加速最快，方向不確定但爆發力最強 |
| 深價外 | ≈0.1 | 極小 | 便宜但需要大波動才能啟動 |

### Delta-Theta 對沖思維

Delta 和 Theta 是選擇權最核心的「付費 vs 收租」對抗：

- **正 Delta + 負 Theta**：買方策略，方向對賺價差、時間流逝扣成本
- **負 Delta + 正 Theta**：賣方策略，收時間價值但方向錯虧價差
- **Delta Neutral + 正 Theta**：中性賣方策略，不管漲跌只收時間價值
- **Delta Neutral + 負 Theta**：中性買方策略，賭波動率擴張

**實戰黃金比例**：Theta/Gamma 比值
- 比值 > 1：賣方有利，時間價值收入 > Gamma 風險
- 比值 < 1：賣方不利，Gamma 風險 > Theta 收入
- 這就是為什麼高 IV 環境賣方有利——Theta 夠大足以覆蓋 Gamma 風險

### Vega-Theta 共同判讀

Vega 和 Theta 是一體兩面，同源於時間價值：

- **IV 擴張**：Vega 正的部位獲利，但 Theta 同時在扣時間價值
- **IV 收縮**：Vega 正的部位虧損，Theta 也加速扣時間價值，雙殺
- **賣方的甜蜜點**：IV 收縮 + 時間衰減，Vega 和 Theta 雙賺

**IV Percentile 導向策略**：

| IV Percentile | 策略方向 | Vega | Theta |
|--------------|---------|------|-------|
| > 70%（高） | 賣方策略 | 負（IV收縮獲利） | 正（時間衰減獲利） |
| 30-70%（中） | 組合策略 | 視方向 | 視策略 |
| < 30%（低） | 買方策略 | 正（IV擴張獲利） | 負（時間成本可接受） |

### 四大 Greeks 組合策略矩陣

| 策略 | Delta | Gamma | Vega | Theta | 適用情境 |
|------|-------|-------|------|-------|---------|
| 買 ATM Call | +0.5 | + | + | - | 看多+波動率低 |
| 買 ATM Put | -0.5 | + | + | - | 看空+波動率低 |
| 賣 ATM Call | -0.5 | - | - | + | 看空+波動率高 |
| 賣 ATM Put | +0.5 | - | - | + | 看多+波動率高 |
| 買 Straddle | 0 | ++ | ++ | -- | 不看方向+波動率低 |
| 賣 Straddle | 0 | -- | -- | ++ | 不看方向+波動率高 |
| 鐵兀鷹 | 0 | -- | -- | + | 不看方向+波動率高+限制風險 |
| 買日曆價差 | 0 | + | + | + | 不看方向+波動率低+收Theta |
| 賣日曆價差 | 0 | - | - | - | 不看方向+波動率高+賭IV收縮 |

## Greeks 動態管理

### Delta 中性動態調整

Delta Neutral 不是設好就忘，需要持續調整（Rebalance）：

1. **觸發調整條件**：|Portfolio Delta| > 門檻值（通常設定為總部位風險的 5-10%）
2. **調整方式**：
   - 買/賣標的（期貨或現貨）——最直接
   - 買/賣選擇權——同時影響其他 Greeks
   - 調整履約價或到期日——結構性調整
3. **調整頻率**：日內 vs 每日 vs 每週，越頻繁手續費越高但風險越低

**Gamma Scalping 本質**：在 Delta Neutral 基礎上，利用 Gamma 獲利
- 跌時 Buy（Delta 變負）→ 漲時 Sell（Delta 變正）→ 自動低買高賣
- 每次調整都在收割 Gamma 利潤
- 前提：Gamma 夠大（ATM 或接近到期）+ 波動率夠高

### Vega 風險管理

Vega 是選擇權最不可控的風險因子：

1. **IV 不是價格的函數**：股價可以預測趨勢，IV 卻可能因事件突然飆升
2. **Vega 集中風險**：單一到期日的 Vega 集中，事件風險放大
3. **管理方式**：
   - 限制單一策略 Vega ≤ 總部位 20%
   - 分散到期日：不同月份的 Vega 分散事件風險
   - 用遠月選擇權對沖近月 Vega：遠月 Vega 大但 Gamma 小

### Greeks 時間演化

Greeks 隨時間推移會自然變化：

| Greek | 趨近到期 | 實戰意義 |
|-------|---------|---------|
| Delta | 價內→1，價外→0 | 越接近到期，Delta越兩極化 |
| Gamma | 價平急速放大 | 這就是到期前Gamma爆炸的原因 |
| Theta | 價平加速衰減 | 賣方最後幾天Theta最大 |
| Vega | 逐漸縮小 | 遠月Vega大，近月Vega小 |

## 風險管理框架

### Greeks 風險限額設定

| 參數 | 建議限額 | 計算方式 |
|------|---------|---------|
| Delta | ≤ 帳戶淨值的 5% | Delta × 點值 |
| Gamma | 當日最大虧損 ≤ 2% | Gamma × (3%波動)² |
| Vega | ≤ 帳戶淨值的 10% | Vega × IV變動5% |
| Theta | 日收入目標 0.5-1% | Theta / 帳戶淨值 |

### 壓力測試情境

| 情境 | 檢查項目 |
|------|---------|
| 標的漲跌 3% | Delta + Gamma 損益 |
| IV 突增 20% | Vega 損益 |
| IV 突降 20% | Vega 損益（反向） |
| 跳空缺口 | Gamma 損益（非連續價格） |
| 黑天鵝（漲跌 10%+） | 全部 Greeks 極端損益 |

### 希臘字母對沖優先序

當多個 Greeks 同時需要調整時，處理優先序：

1. **Delta 優先**：方向風險最大，先歸零 Delta
2. **Gamma 其次**：非線性風險，超過門檻必須處理
3. **Vega 第三**：波動率風險，用遠月對沖成本較低
4. **Theta 最後**：時間衰減是可預期的，不需要「對沖」

## 進階觀念

### Vanna 和 Charm：二階 Greeks

- **Vanna** = ∂Delta/∂IV = ∂Vega/∂S：IV 變動對 Delta 的影響
  - IV 上升 → 價外 Delta 變大，價內 Delta 變小
  - 這就是為什麼暴跌時 Put Delta 會加速變大（IV飆升 + 價格下跌雙重效果）

- **Charm** = ∂Delta/∂t：時間流逝對 Delta 的影響
  - 價內選擇權 Delta 趨近 1
  - 價外選擇權 Delta 趨近 0
  - 這就是為什麼賣價外選擇權最後幾天特別安穩

### Greeks 在不同市況的表現

| 市況 | 最佳 Greeks 策略 | 最差 Greeks 策略 |
|------|----------------|----------------|
| 低波動+緩漲 | 買 Call（+Delta,+Vega） | 賣 Put（+Delta,+Vega風險） |
| 低波動+緩跌 | 買 Put（-Delta,+Vega） | 賣 Call（-Delta,+Vega風險） |
| 低波動+盤整 | 買 Straddle（0,+Vega） | 賣 Straddle（0,-Vega） |
| 高波動+急漲 | 賣 Put+買 Call | 買 Put（Vega虧損） |
| 高波動+急跌 | 賣 Call+買 Put | 買 Call（Vega虧損） |
| 高波動+盤整 | 賣 Iron Condor | 買 Straddle（Theta虧損） |

---

## 關鍵字

- 選擇權 Greeks
- Delta Gamma 組合判讀
- Vega Theta 對沖思維
- Delta Neutral 動態調整
- Gamma Scalping
- Greeks 風險限額
- 壓力測試
- Vanna Charm 二階 Greeks