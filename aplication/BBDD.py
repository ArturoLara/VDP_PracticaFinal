import redis


class gestorBBDD:
    def __init__(self):
        self.r = redis.StrictRedis(host='35.180.98.140', port=6379, db=0, password="redis")

    def addData(self, date, **data):
        if self.r.zcard(date) < 1:
            self.r.zadd(date, **data)
        else:
            self.r.zadd("temp", **data)
            self.r.zunionstore(date, ["temp", date], aggregate=None)
            self.r.delete("temp")

    def showData(self, date):
        return self.r.zrange(date, 0, -1, desc=True, withscores=True)

    def removeData(self, name):
        self.r.delete(name)


