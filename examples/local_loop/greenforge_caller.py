import urllib.request
import json

payload = json.dumps({
    "query": "Customer is a 45 year old woman with chronic lower back pain and mild anxiety. She has low THC tolerance and prefers non-smoking consumption. What product do you recommend and why?"
}).encode()

req = urllib.request.Request(
    "http://localhost:8787/recommend",
    data=payload,
    headers={"Content-Type": "application/json"},
    method="POST"
)

print("[greenforge] sending patient profile through Gatekeeper...")

with urllib.request.urlopen(req, timeout=120) as resp:
    body = json.loads(resp.read())
    print(f"\n[mistral via gatekeeper]\n{body['reasoning']}")

print("\n[greenforge] done -- check artifacts/gatekeeper.ndjson")
