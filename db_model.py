import pymysql

# MySQL / MariaDB 연결 (db이름: study_db)
conn = pymysql.connect(
    host='localhost', 
    user='root',       # 예: 'myuser' 또는 'root'
    password='q1w2e3', 
    db='study_db', 
    charset='utf8mb4'
)

def add_status(status):
    # 트랜잭션 오류 방지 및 자동 재연결 처리
    conn.ping(reconnect=True)
    with conn.cursor() as cur:
        sql = "INSERT INTO record_led(status) VALUES ('{0}')".format(status)
        cur.execute(sql)
    conn.commit()
