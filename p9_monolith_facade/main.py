# facade method
class Cache:
    cache = {"user": "Ahmad", "user2": "Sami"}
    def get(self, key):
        if key in self.cache:
            return self.cache[key]


class DB:
    db = {"users": {"user": "Ahmad", "user2": "Sami", "user3": "Sara", "user4": "Hala"}}
    def fetch(self, table, key): 
        if table in self.db and key in self.db[table]:
            return self.db[table][key]


class API:
    data = {"user5": "Sami", "user6": "Sara"}
    def call(self, key): 
        if key in self.data:
            return self.data.get(key)
        else:
            return None


class Facade:
    def __init__(self):
        self.cache = Cache()
        self.db = DB()
        self.api = API()
    def fetch_data(self, key, table):
        if self.cache.get(key):
            return print(f"{key} inside the cache: {self.cache.get(key)}")
        elif self.db.fetch(table, key):
            return print(f"{key} not in the cache, but inside the DB: {self.db.fetch(table, key)}")
        else:
            return print(f"{key} not in the cache and DB, call API: {self.api.call(key)}")


if __name__ == "__main__":
    facade = Facade()
    facade.fetch_data(key="user", table="users")
    facade.fetch_data(key="user3", table="users")
    facade.fetch_data(key="user5", table="users")

    facade.fetch_data(key="user8", table="users")
    result = facade.cache.get(key="user2")
    print(f"for power‐users: {result}")
