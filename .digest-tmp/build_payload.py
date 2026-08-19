import json
prompt = open('.digest-tmp/prompt.txt').read().strip()
payload = {
    "model": "grok-4.6",
    "input": [{"role": "user", "content": prompt}],
    "tools": [{"type": "x_search", "from_date": "2026-08-18", "to_date": "2026-08-19"}]
}
with open('.digest-tmp/payload.json', 'w') as f:
    json.dump(payload, f)
print("written")
