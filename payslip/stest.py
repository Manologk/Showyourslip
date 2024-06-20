import psycopg2


def main():
    conn = psycopg2.connect('postgres://avnadmin:AVNS__IX8NB1vG06viybrJt7@payslipdb-payslipdb.j.aivencloud.com:26827/defaultdb?sslmode=require')

    query_sql = ('SELECT * FROM "payslip_payslip" LIMIT 1000')

    cur = conn.cursor()
    cur.execute(query_sql)

    version = cur.fetchone()
    print(version)


if __name__ == "__main__":
    main()