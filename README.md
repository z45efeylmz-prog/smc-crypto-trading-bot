# ⚡ Automated SMC & SFP Crypto Trading Bot (Python)

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![API Powered](https://img.shields.io/badge/Powered%20By-RapidAPI%20SMC%20Hunter-00E676.svg)](https://rapidapi.com/ZiyaefeYilmaz/api/smc-liquidity-sweep-sfp-hunter)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Binance Futures](https://img.shields.io/badge/Exchange-Binance%20Futures-F0B90B.svg)](https://binance.com)

An institutional-grade, open-source crypto trading bot powered by the **Smart Money Concepts (SMC) & Swing Failure Pattern (SFP) Liquidity Hunter API**. 

Instead of lagging retail indicators (RSI, MACD, Bollinger Bands), this bot tracks **institutional liquidity sweeps, fakeout rejections, and Consequent Encroachment (50% wick retests)** across high-liquidity crypto pairs (BTC, ETH, SOL, APT, DOGE, SUI, AVAX).

---

## 🎯 How It Works (The Institutional Edge)

```
       [Liquidity Sweep / SFP Trap]
               ▲
               │  Upper Rejection Wick (>= 35%)
         ┌─────┴─────┐
         │           │
   ──────┼───────────┼────── [12-Bar Pivot High Level]
         │           │
         └─────┬─────┘
               │  ◄──── 50% Consequent Encroachment (CE) Limit Entry!
               ▼
   Target: 3.5R Asymmetric Take Profit
```

1. **Pivot Sweep Detection:** Detects when price spikes above/below key 12-bar pivot swing levels.
2. **Trap Confirmation:** Price fails to close beyond the level and creates an aggressive rejection wick ($\ge 35\%$ of candle range).
3. **Consequent Encroachment (CE):** Automatically calculates the optimal limit order entry at 50% of the rejection wick.
4. **Asymmetric 3.5R Execution:** Places automatic stops at the wick extreme and targets a 3.5x risk-to-reward ratio.

---

## 🚀 60-Second Quickstart

### 1. Clone the Repository
```bash
git clone https://github.com/z45efeylmz-prog/smc-crypto-trading-bot.git
cd smc-crypto-trading-bot
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Get Your Free RapidAPI Key
1. Go to the [SMC Liquidity Sweep & SFP Hunter API on RapidAPI](https://rapidapi.com/ZiyaefeYilmaz/api/smc-liquidity-sweep-sfp-hunter).
2. Click **Subscribe to Test** (Free Tier includes 100 free requests/month).
3. Copy your `X-RapidAPI-Key` from the dashboard.

### 4. Run the Bot
Set your API key and launch the bot in Paper Trading (Simulation) mode:

```bash
# On Linux / macOS
export RAPIDAPI_KEY="your_rapidapi_key_here"
python bot.py

# On Windows (PowerShell)
$env:RAPIDAPI_KEY="your_rapidapi_key_here"
python bot.py
```

---

## 📊 Live Terminal Output

```text
====================================================================
  ⚡ SMC & SFP INSTITUTIONAL CRYPTO TRADING BOT ⚡
  Smart Money Liquidity Hunter | Consequent Encroachment (CE)
  RapidAPI: https://rapidapi.com/ZiyaefeYilmaz/api/smc-liquidity-sweep-sfp-hunter
====================================================================
Mode: SIMULATION (PAPER TRADING)

[*] Starting real-time SMC Liquidity Scanner across 7 pairs...

--- [2026-11-03 23:15:00] Scanning Crypto Liquidity Levels... ---
  [APTUSDT] Price: 8.618 | Resistance: 8.6298 | Support: 8.6068 (Monitoring)
  [DOGEUSDT] Price: 0.158 | Resistance: 0.1612 | Support: 0.1541 (Monitoring)

══════════════════════════════════════════════════════════
🎯 INSTITUTIONAL SMC SETUP DETECTED: SOLUSDT SHORT
══════════════════════════════════════════════════════════
  • Setup Type:       BEARISH_LIQUIDITY_SWEEP_SFP
  • Swept Pivot:      189.45
  • Limit Entry (CE): 188.92
  • Invalidation (SL):189.64
  • Target (TP 3.5R): 186.40
  • Risk / Reward:    1 : 3.50
  • Conviction Score: 94.0%
──────────────────────────────────────────────────────────
📝 [PAPER TRADE EXECUTED] Simulated Limit SHORT order placed at 188.92. SL: 189.64, TP: 186.40
```

---

## ⚙️ Configuration Options

Inside `bot.py` or your `.env` file:

| Parameter | Default | Description |
| :--- | :--- | :--- |
| `PAPER_TRADING` | `True` | Set `False` to execute real live orders on exchange. |
| `SCAN_INTERVAL_SECONDS` | `180` | Delay between scans (180s = every 3 min, perfect for Pro plan). |
| `SYMBOLS` | `["APTUSDT", ...]` | Pairs to monitor. Set `[]` to automatically scan Top 20 liquid cryptos. |

---

## 🛡️ Upgrading for 24/7 Production Use

The **Free Tier** on RapidAPI is designed for development and testing. 

For 24/7 automated production trading across multiple symbols, upgrade to the **Pro Plan ($29/month)** on [RapidAPI SMC Hunter](https://rapidapi.com/ZiyaefeYilmaz/api/smc-liquidity-sweep-sfp-hunter) for **15,000 monthly requests** and ultra-low latency sub-100ms response times.

---

## ⚖️ Disclaimer

*This software is for educational and quantitative research purposes only. Cryptocurrency trading involves substantial risk of loss. Always test thoroughly in Paper Trading mode before allocating real capital.*
