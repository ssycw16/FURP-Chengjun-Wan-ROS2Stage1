#!/usr/bin/env python3

import csv
import math
import sys


def parse_value(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else 'gps_log.csv'
    with open(path, 'r', encoding='utf-8') as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)

    if not rows:
        print(f'No rows in {path}')
        return

    lats = [parse_value(row.get('lat')) for row in rows]
    lons = [parse_value(row.get('lon')) for row in rows]
    statuses = [row.get('status', 'unknown') for row in rows]
    satellites = [parse_value(row.get('satellites')) for row in rows]

    valid_lat = [value for value in lats if value is not None]
    valid_lon = [value for value in lons if value is not None]
    valid_sat = [value for value in satellites if value is not None]

    fix_count = sum(1 for status in statuses if 'fix' in status.lower())
    no_fix_count = len(rows) - fix_count

    print(f'Total samples: {len(rows)}')
    print(f'Fix samples: {fix_count}')
    print(f'No-fix samples: {no_fix_count}')
    if valid_lat and valid_lon:
        print(f'Lat range: {min(valid_lat):.8f} to {max(valid_lat):.8f}')
        print(f'Lon range: {min(valid_lon):.8f} to {max(valid_lon):.8f}')
    if valid_sat:
        print(f'Satellites: min={min(valid_sat):.0f} '
              f'mean={sum(valid_sat)/len(valid_sat):.1f} '
              f'max={max(valid_sat):.0f}')


if __name__ == '__main__':
    main()
