import mysql.connector as ms

x = ms.connect(host = 'localhost', user = 'root', passwd = 'dpsbn', database = 'arafoodsdb')

y = x.cursor(buffered = True)

y.execute("select items from copperchimney__whitefield")

data = y.fetchall()

c = 1

for i in range(len(data)):

    y.execute("update copperchimney__whitefield set id = {} where items = '{}'".format(c, data[i][0]))
    x.commit()
    c += 1
