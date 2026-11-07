# dns-ttl-analyzer

Check DNS record TTLs: under 60 seconds risks query churn, over a day risks stale records after a change — lowest TTL first.

## How to run

```sh
python3 main.py records.csv
```

## Example output

```
www.example A: TOO LOW (TTL 30s)
mail.example MX: OK (TTL 3600s)
```

Standard library only. Run the tests with `python3 -m unittest discover`.
