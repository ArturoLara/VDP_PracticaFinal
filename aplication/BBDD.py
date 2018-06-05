import redis


class gestorBBDD:

    def __init__(self):
        self.r = redis.StrictRedis(host='35.180.103.245', port=6379, db=0, password="redis")

    def addData(self, date, data):
        if self.r.zcard(date) < 1:
            for word in data:
                self.r.zadd(date, word[1], word[0])
        else:
            self.r.delete("temp")
            for word in data:
                self.r.zadd("temp", word[1], word[0])
            self.r.zunionstore(date, ["temp", date], aggregate=None)

    def showData(self, date):
        return self.r.zrange(date, 0, -1, desc=True, withscores=True)

    def removeData(self, name):
        self.r.delete(name)


if __name__ == '__main__':
    nuevo = gestorBBDD()
    print nuevo.showData("0000-00-00")
