"""Classify DNS records by TTL risk.

Usage: python3 main.py records.csv
CSV columns: name,type,ttl_seconds.
TOO LOW under 60s (churn risk), TOO HIGH over 86400s (stale-change
risk), otherwise OK. Lowest TTL first.
"""
import argparse, csv, sys

def analyze(rows):
    out = []
    for row in rows:
        ttl = int(row["ttl_seconds"])
        verdict = "TOO LOW" if ttl < 60 else ("TOO HIGH" if ttl > 86400 else "OK")
        out.append((row["name"], row["type"], ttl, verdict))
    return sorted(out, key=lambda r: r[2])

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path")
    args = parser.parse_args(argv)
    with open(args.path, newline="", encoding="utf-8") as f:
        for name, typ, ttl, verdict in analyze(list(csv.DictReader(f))):
            print(f"{name} {typ}: {verdict} (TTL {ttl}s)")
    return 0

if __name__ == "__main__":
    sys.exit(main())
