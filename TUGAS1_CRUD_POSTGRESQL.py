import os
import psycopg2 as db
con = None
connected = None
cursor = None


def connect():
    global connected
    global con
    global cursor
    try:
        con = db.connect(host="localhost", database="tokobangunan",
                         port=5432, user="ling", password="123")
        cursor = con.cursor()
        connected = True

    except:
        connected = False
    return cursor


def disconnect():
    global connected
    global con
    global cursor
    if(connected == True):
        cursor.close()
        con.close()
    else:
        con = None
        connected = False


def Data():
    global connected
    global con
    global cursor
    a = connect()
    sql = "select * from customers"
    a.execute(sql)
    record = a.fetchall()
    if a.rowcount < 0:
        print("Data tidak ditemukan!")
    else:
        for data in record:
            print(data)


def Input():
    global connected
    global con
    global cursor
    nama = input("Masukkan Nama : ")
    alamat = input("Masukkan Alamat : ")
    no_tlp = input("Masukkan Nomor Telepon : ")
    a = connect()
    sql = "insert into customers (nama, alamat, no_telepon) values ('" + \
        nama+"', '"+alamat+"', '"+no_tlp+"')"
    a.execute(sql)
    con.commit()
    print("Input data berhasil.")


def Update():
    global connected
    global con
    global cursor
    nama = input("Masukkan Nama yang ingin dicari : ")
    a = connect()
    sql = "select * from customers where nama ='" + nama + "'"
    a.execute(sql)
    record = a.fetchall()
    print("Data saat ini : ")
    print(record)
    row = a.rowcount
    if(row == 1):
        print("Silahkan untuk mengubah data..")
        alamat = input("Masukkan Alamat : ")
        no_tlp = input("Masukkan Nomor Telepon : ")
        a = connect()
        sql = "update customers set alamat = '" + alamat + \
            "', no_telepon = '" + no_tlp + "' where nama = '" + nama + "'"
        a.execute(sql)
        con.commit()
        print("Update berhasil.")
        sql = "select * from customers where nama = '" + nama + "'"
        a.execute(sql)
        rec = a.fetchall()
        print("Data setelah diubah :")
        print(rec)

    else:
        print("Data tidak ditemukan!")


def Delete():
    global connected
    global con
    global cursor
    nama = input("Masukkan Nama yang ingin dicari : ")
    a = connect()
    sql = "select * from customers where nama ='" + nama + "'"
    a.execute(sql)
    record = a.fetchall()
    print("Data saat ini : ")
    print(record)
    row = a.rowcount
    if(row == 1):
        jwb = input("Apakah ingin menghapus data? (y/n)")
        if(jwb.upper() == "Y"):
            a = connect()
            sql = "delete from customers where nama ='" + nama + "'"
            a.execute(sql)
            con.commit()
            print("Hapus data berhasil.")
        else:
            print("Data batal untuk dihapus.")
    else:
        print("Data tidak ditemukan!")


def Search():
    global connected
    global con
    global cursor
    nama = input("Masukkan Nama yang dicari : ")
    a = connect()
    sql = "select * from customers where nama ='" + nama + "'"
    a.execute(sql)
    record = a.fetchall()
    row = a.rowcount
    if(row == 1):
        print("Data saat ini :")
        print(record)
    else:
        print("Data tidak ditemukan!")


def Show_menu():
    print("\n>>> APLIKASI CRUD DENGAN DATABASE POSTGRESQL <<<")
    print("1. Input Data")
    print("2. Show Data")
    print("3. Update Data")
    print("4. Delete Data")
    print("5. Search Data")
    print("0. Close Program")
    print("==============================")
    print("\nDibuat oleh : Lingga Dzulfikar\n")
    print("==============================")
    menu = input("Pilih menu> ")

    os.system("cls")

    if menu == "1":
        Input()
    elif menu == "2":
        Data()
    elif menu == "3":
        Update()
    elif menu == "4":
        Delete()
    elif menu == "5":
        Search()
    elif menu == "0":
        exit()
    else:
        print("Menu salah!")


if __name__ == "__main__":
    while(True):
        Show_menu()
