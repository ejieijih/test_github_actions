#!/usr/bin/env python3
from datetime import datetime, timezone
from zoneinfo import ZoneInfo  # Python 3.9以降で利用可能

def main():
    now_utc = datetime.now(timezone.utc)
    # 'Asia/Tokyo' は日本標準時（JST、UTC+9）を表します
    now_jst = now_utc.astimezone(ZoneInfo("Asia/Tokyo"))
    print("Cron Test: This script ran at", now_jst.isoformat())

if __name__ == '__main__':
    main()
