# DesignPatternTask
## 🎯Problem 8 — Endpoint Cross‐Cutting Concerns
Each REST handler manually performs auth, rate‐limit, logging, etc.
Requirements
• Attach behaviours to a handler dynamically, without editing its source.
• Allow stacking behaviours in any order.
• Reuse the unmodified handler elsewhere.
Ugly Starter Code
def handle_request():
print("Validating auth")
print("Checking rate limits")
print("Logging request")
print("Processing request")
handle_request()
