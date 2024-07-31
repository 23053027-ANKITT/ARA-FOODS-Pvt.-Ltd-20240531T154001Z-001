import mysql.connector as ms

x = ms.connect(host = 'localhost', user = 'root', passwd = 'dpsbn', database = 'arafoodsdb')
y = x.cursor(buffered = True)

for i in range(1, 55):

    y.execute("delete from grand_cost where id = {}".format(i))
    x.commit()

x.close()
