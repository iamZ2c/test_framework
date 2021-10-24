import redis
config = {
    "host": "10.24.1.81",
    "port": 6379,
    "password": "Abc@1234",
    "db": 0,
    "max_connections": 10
}
POOL = redis.ConnectionPool(**config)


