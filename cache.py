# cache.py
_cache = {}

def get(key):
    return _cache.get(key)

def set(key, value):
    _cache[key] = value
