import redis


class gestorBBDD:

    def __init__(self):
        self.r = redis.StrictRedis(host='35.180.103.245', port=6379, db=0, password="redis")
        self.tests = redis.StrictRedis(host='35.180.103.245', port=6379, db=1, password="redis")

    def addData(self, date, data):
        if self.r.zcard(date) < 1:
            for word in data:
                self.r.zadd(date, word[1], word[0])
        else:
            self.r.delete("temp")
            for word in data:
                self.r.zadd("temp", word[1], word[0])
            self.r.zunionstore(date, ["temp", date], aggregate=None)


    def addDataTest(self, date, data):
        if self.tests.zcard(date) < 1:
            for word in data:
                self.tests.zadd(date, word[1], word[0])
        else:
            self.tests.delete("temp")
            for word in data:
                self.tests.zadd("temp", word[1], word[0])
            self.tests.zunionstore(date, ["temp", date], aggregate=None)

    def showData(self, date):
        return self.r.zrange(date, 0, -1, desc=True, withscores=True)

    def showDataTest(self, date):
        return self.tests.zrange(date, 0, -1, desc=True, withscores=True)

if __name__ == '__main__':
    gestor = gestorBBDD()
    data = []
    letters = ["a", "b", "c", "d", "e"]
    for i in range(4):
        data.append([letters[i], i+1])
    print(data)
    gestor.addDataTest("21/04/97", data)
    print(gestor.showDataTest("21/04/97"))