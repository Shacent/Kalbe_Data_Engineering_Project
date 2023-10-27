#Melakukan import mysql connector
import mysql.connector

#Melakukan percobaan koneksi ke database db
conn = mysql.connector.connect(
        host="localhost", user="root", passwd="", database="kalbe" )

#Membuat kursor sebagai penanda

cursor = conn.cursor()

#Deklarasi SQL Query untuk memasukkan record ke DB (KARYAWAN)
insert_sql = (
    "INSERT INTO karyawan (FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)"
    "VALUES (%s, %s, %s, %s, %s)"
)   
values = ("Hauzan", "Dini", "20", "F", "3120000")

try:
    #Eksekusi SQL Command
    cursor.execute(insert_sql, values)
    
    #Melakukan perubahan (commit) pada DB
    conn.commit()    
    print("Berhasil terhubung ke database")
    
except mysql.connector.Error as err:
    #Roll Back apabila ada issue
    print("gagal")
    conn.rollback()

#Menutup koneksi
conn.close()

# Muhammad Hauzan Dini Fakhri 