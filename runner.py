import sqlite3
import sys


if __name__ == '__main__':
    con = sqlite3.connect(input())
    cur = con.cursor()
    solution = open(sys.argv[1], "rt", encoding="utf8").read().strip()
    result = cur.execute(solution).fetchall()
    con.close()
    print("\n".join(map(lambda item: item[0], result)))
