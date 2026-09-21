import pymysql

conn = pymysql.connect(host='localhost', user='appuser', password='q1w2e3', db='shopping_db')
cur = conn.cursor() #SQL 문을 실행하거나 실행된 결과를 돌려받는 통로
cur.execute("select * from CUSTOMER")
rows = cur.fetchall()   #fetchone() 반복
print(rows)
conn.commit()
conn.close()
