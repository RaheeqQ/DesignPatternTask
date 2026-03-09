# DesignPatternTask
```python
# 🎯Problem 9 — Monolith Facade

Clients must juggle Cache, DB, and API classes to fetch data.

## Requirements
• Provide a straightforward façade that covers common scenarios.
• Hide subsystem complexity but still allow power‐users to drill down.

## Ugly Starter Code

class Cache:
  def get(self, key): pass
class DB:
  def fetch(self, table): pass
class API:
  def call(self): pass
cache = Cache()
db = DB()
api = API()
# client code
cache.get("user")
db.fetch("users")
api.call()
```
