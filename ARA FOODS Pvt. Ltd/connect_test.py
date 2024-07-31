import mysql.connector as ms

mycon = ms.connect(host = 'localhost', user = 'root', password = 'dpsbn', database = 'company', auth_plugin = 'dpsbn')

if mycon.is_connected() == False:
    print('ERROR')
else:
    #print('Connected')
    c = mycon.cursor()
    c.execute('select empno from emp')
    data = c.fetchall()
    for i in data:
        print(i[0])
