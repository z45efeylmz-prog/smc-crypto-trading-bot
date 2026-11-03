"""
=============================================================================
SMC & SFP Institutional Crypto Trading Bot (Binance / Bybit / Paper Trading)
=============================================================================
Powered by RapidAPI: SMC Liquidity Sweep & SFP Hunter Engine
Documentation & API Key: https://rapidapi.com/ZiyaefeYilmaz/api/smc-liquidity-sweep-sfp-hunter
=============================================================================
"""

import os
import time
import json
import requests
from typing import Dict, Any, Optional

# Optional Colorama for sleek terminal styling
try:
    from colorama import init, Fore, Style
    init(autoreset=True)
    GREEN = Fore.GREEN
    RED = Fore.RED
    CYAN = Fore.CYAN
    YELLOW = Fore.YELLOW
    BOLD = Style.BRIGHT
    RESET = Style.RESET_ALL
except ImportError:
    GREEN = RED = CYAN = YELLOW = BOLD = RESET = ""

# ─────────────────────────────────────────────────────────────
# CONFIGURATION
# ─────────────────────────────────────────────────────────────
# Get your RapidAPI Key from: https://rapidapi.com/ZiyaefeYilmaz/api/smc-liquidity-sweep-sfp-hunter
RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY", "YOUR_RAPIDAPI_KEY_HERE")
RAPIDAPI_HOST = "smc-liquidity-sweep-sfp-hunter.p.rapidapi.com"
API_URL = "https://smc-liquidity-sweep-sfp-hunter.p.rapidapi.com/api/v1/signals/smc-liquidity"

# Simulation / Paper Trading Mode (Set False for Live Binance Trading)
PAPER_TRADING = True
SCAN_INTERVAL_SECONDS = 180  # Scan every 3 minutes (10-20 calls/hr, perfectly fits Pro Plan)

# Target assets to monitor (Leave empty [] to scan Top 20 liquid cryptos automatically)
SYMBOLS = ["APTUSDT", "DOGEUSDT", "SOLUSDT", "BTCUSDT", "ETHUSDT", "SUIUSDT", "AVAXUSDT"]

def print_banner():
    banner = f"""
{CYAN}{BOLD}====================================================================
  ⚡ SMC & SFP INSTITUTIONAL CRYPTO TRADING BOT ⚡
  Smart Money Liquidity Hunter | Consequent Encroachment (CE)
  RapidAPI: https://rapidapi.com/ZiyaefeYilmaz/api/smc-liquidity-sweep-sfp-hunter
===================================================================={RESET}
Mode: {YELLOW}{'SIMULATION (PAPER TRADING)' if PAPER_TRADING else 'LIVE BINANCE EXECUTION'}{RESET}
    """
    print(banner)

def query_smc_signal(symbol: Optional[str] = None) -> Optional[Dict[str, Any]]:
    """Queries the RapidAPI SMC Hunter Engine."""
    headers = {
        "x-rapidapi-key": RAPIDAPI_KEY,
        "x-rapidapi-host": RAPIDAPI_HOST
    }
    params = {}
    if symbol:
        params["symbol"] = symbol

    try:
        response = requests.get(API_URL, headers=headers, params=params, timeout=10)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 403:
            print(f"{RED}[!] Error: Invalid RapidAPI Key or Quota exceeded. Check your subscription.{RESET}")
        else:
            print(f"{YELLOW}[!] RapidAPI returned status {response.status_code}: {response.text[:100]}{RESET}")
    except Exception as e:
        print(f"{RED}[!] Network error connecting to RapidAPI: {e}{RESET}")
    return None

def execute_trade(signal: Dict[str, Any]):
    """Executes paper trade or live order on exchange."""
    sym = signal.get("symbol")
    direction = signal.get("direction")
    entry = signal.get("consequent_encroachment_entry") or signal.get("current_price")
    sl = signal.get("stop_loss")
    tp = signal.get("take_profit_3_5R")
    rr = signal.get("risk_reward", "1 : 3.50")
    conf = signal.get("institutional_confidence", 85.0)

    print(f"\n{GREEN}{BOLD}══════════════════════════════════════════════════════════{RESET}")
    print(f"{GREEN}{BOLD}🎯 INSTITUTIONAL SMC SETUP DETECTED: {sym} {direction}{RESET}")
    print(f"{GREEN}{BOLD}══════════════════════════════════════════════════════════{RESET}")
    print(f"  • Setup Type:       {CYAN}{signal.get('setup_type')}{RESET}")
    print(f"  • Swept Pivot:      {YELLOW}{signal.get('pivot_level_swept')}{RESET}")
    print(f"  • Limit Entry (CE): {GREEN}{entry}{RESET}")
    print(f"  • Invalidation (SL):{RED}{sl}{RESET}")
    print(f"  • Target (TP 3.5R): {GREEN}{tp}{RESET}")
    print(f"  • Risk / Reward:    {BOLD}{rr}{RESET}")
    print(f"  • Conviction Score: {BOLD}{conf}%{RESET}")
    print(f"{GREEN}──────────────────────────────────────────────────────────{RESET}")

    if PAPER_TRADING:
        print(f"{YELLOW}📝 [PAPER TRADE EXECUTED] Simulated Limit {direction} order placed at {entry}. SL: {sl}, TP: {tp}{RESET}\n")
    else:
        # Live Binance Order Execution (requires python-binance or CCXT)
        print(f"{GREEN}🚀 [LIVE ORDER] Sending order to Binance Futures API...{RESET}\n")
        # TODO: integrate binance_client.futures_create_order(...)

def main():
    print_banner()
    
    if RAPIDAPI_KEY == "YOUR_RAPIDAPI_KEY_HERE":
        print(f"{YELLOW}[!] WARNING: You haven't set your RAPIDAPI_KEY yet!")
        print(f"    Get your free key at: https://rapidapi.com/ZiyaefeYilmaz/api/smc-liquidity-sweep-sfp-hunter")
        print(f"    Set it in the script or run: export RAPIDAPI_KEY='your_key'{RESET}\n")

    print(f"{CYAN}[*] Starting real-time SMC Liquidity Scanner across {len(SYMBOLS)} pairs...{RESET}")

    while True:
        try:
            print(f"\n{CYAN}--- [{time.strftime('%Y-%m-%d %H:%M:%S')}] Scanning Crypto Liquidity Levels... ---{RESET}")
            
            # If no symbols specified, queries Top 20 multi-asset scan
            if not SYMBOLS:
                res = query_smc_signal()
                if res and res.get("signals"):
                    for sig in res["signals"]:
                        execute_trade(sig)
                else:
                    print(f"  No active SFP sweep. Market is consolidating within pivots.")
            else:
                for sym in SYMBOLS:
                    sig = query_smc_signal(symbol=sym)
                    if sig:
                        status = sig.get("status")
                        if status == "SIGNAL_FOUND":
                            execute_trade(sig)
                        else:
                            curr = sig.get("current_price", "N/A")
                            p_high = sig.get("nearest_pivot_high", "N/A")
                            p_low = sig.get("nearest_pivot_low", "N/A")
                            print(f"  [{sym}] Price: {curr} | Resistance: {p_high} | Support: {p_low} (Monitoring)")
                    time.sleep(1) # respectful query spacing

            print(f"{YELLOW}[i] Sleeping for {SCAN_INTERVAL_SECONDS}s before next liquidity scan...{RESET}")
            time.sleep(SCAN_INTERVAL_SECONDS)

        except KeyboardInterrupt:
            print(f"\n{RED}[*] Bot stopped by user.{RESET}")
            break
        except Exception as e:
            print(f"{RED}[!] Loop exception: {e}{RESET}")
            time.sleep(10)

if __name__ == "__main__":
    main()
