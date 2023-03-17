# NAMA: ADINDA APRILIANI
# NIM: 2209116024
# KELAS: A SISTEM INFORMASI 2022

from os import system
from prettytable import PrettyTable

# = = = DATABASE = = =
Judul_Film = ["Perjanjian Gaib", 
              "Waktu Maghrib", 
              "Missing", 
              "Shazam!", 
              "Ant-Man"]
Genre_Film = ["Horror", "Horror", "Drama", "Action", "Action"]
Durasi_Film = ["1 Jam 52 Menit",
               "1 Jam 44 Menit",
               "1 Jam 51 Menit",
               "2 Jam 10 Menit",
               "2 Jam 4 Menit"]
Studio_Film = ["2D_BM", "2D_SS", "2D_SCP",
               "2D_CC", "2D_PM"]


# = = = LINKED LIST = = =
class Node(object):
    def __init__(self,initvalue,next = None):
            self.value=initvalue
            self.next=None
            self.previous=None

    def getvalue(self):
        return self.value
    
    def getNext(self):
        return self.next
    
    def getPrevious(self):
        return self.previous
    
    def setvalue(self,newvalue):
        self.value=newvalue

    def setNext(self,newNext):
        self.next=newNext

    def setPrev(self,newPrevious):
        self.previous=newPrevious
        
    def r_next(self):
        return self.next

class LinkedList:
    def __init__(self, data, next = None):
        self.head = data
        self.next = next

    def sizeof(self,count = 0):
        x = self.head
        while x:
            count += 1
            x = x.next
        return count

    def deleteNode(self,data):
        temp = self.head
        if (temp is not None):
            if(temp.data == data):
                self.head = temp.next
                temp = None
                return
        while(temp is not None):
            if temp.data == data:
                break
            prev = temp
            temp = temp.next
        if(temp == None):
            return
        prev.next = temp.next
        temp = None

def buat_list(elemen):
    head = LinkedList(elemen[0])
    for elemen in elemen[1:]:
        ptr = head
        while ptr.next:
            ptr = ptr.next
        ptr.next = LinkedList(elemen)
    return head

def print_list(head,head1,head2,head3):
    ptr = head
    ptr1 = head1
    ptr2 = head2
    ptr3 = head3
    i=0
    table = PrettyTable(["Nomor", "Judul Film","Genre", "Durasi", "Studio"])
    while ptr:
        table.add_row([i+1,ptr.head,ptr1.head,ptr2.head,ptr3.head])
        ptr = ptr.next
        ptr1 = ptr1.next
        ptr2 = ptr2.next
        ptr3 = ptr3.next
        i+=1
    print(table)


# = = = FUNGSI = = =
def tambah():
           
    Judul = buat_list(Judul_Film)
    Genre = buat_list(Genre_Film)
    Duration = buat_list(Durasi_Film)
    Studio = buat_list(Studio_Film)

    print_list(Judul, Genre, Duration, Studio)
    print("="*40)
    print("===       Masukkan Data Bioskop      ===")     
    print("="*40)

    Judul2 = input("Masukkan Judul Film       : ")
    Judul_Film.append(Judul2)

    Genre2 = input("Masukkan Genre Film : ")
    Genre_Film.append(Genre2)

    Duration2 = input("Masukkan Durasi Film : ")
    Durasi_Film.append(Duration2)

    Studio2 = input("Masukkan Studio : ")
    Studio_Film.append(Studio2)

    print("="*30)
    print ("Data Bioskop Berhasil Dibuat ")
    print("="*30)

    return


def edit():
            
    Judul = buat_list(Judul_Film)
    Genre = buat_list(Genre_Film)
    Duration = buat_list(Durasi_Film)
    Studio = buat_list(Studio_Film)

    print_list(Judul, Genre, Duration, Studio)

    while True:
        print("="*34)
        print("===      Edit Data Bioskop     ===")     
        print("="*34)

        try:
            ID = int(input("Input Index Data Judul Film yang Ingin Diubah : "))

        except:
            print("Gunakan Angka Saat Menginput Pilihan")
            continue
        if ID <= 0 :
            print("Pilihan Tidak Tersedia")
            continue

        Judul = ID - 1
        if (Judul > len(Judul_Film) - 1):
            print ("No Tidak Tersedia")
            continue
        else:
            try:
                tambah = input("Masukkan Judul Film Yang Baru :  ")
            except:
                print("Gunakan Angka Saat Menginput Pilihan")
                continue
            hasil = tambah 
            Judul_Film[Judul] = hasil

            return

def hapus():
    while True:
        print("="*34)
        print("===      Hapus Data Bioskop    ===")     
        print("="*34)
          
        Judul = buat_list(Judul_Film)
        Genre = buat_list(Genre_Film)
        Duration = buat_list(Durasi_Film)
        Studio = buat_list(Studio_Film)

        print_list(Judul, Genre, Duration, Studio)

        try:
            ID = int(input("Input Index Data Ingin Dihapus : ")) 
        except:
            print("Gunakan Angka Saat Menginput Pilihan")
            continue
        ID = ID - 1
        hapus = ID 
        if ID == (hapus):
            print("Anda Telah Menghapus Film",str(Judul_Film.pop(ID)),"dari Data Bioskop")
            
            Judul = buat_list(Judul_Film)
            Genre = buat_list(Genre_Film)
            Duration = buat_list(Durasi_Film)
            Studio = buat_list(Studio_Film)

            print_list(Judul, Genre, Duration, Studio)
            return
        else:
            print("Pilihan Tidak Tersedia")


# = = = MAIN MENU = = =
def menu_awal():
    back =  "ya"
    while(back == "ya"):

        print("="*3,"Selamat Datang di Bioskop La Winter".center(35),"="*3)
        print("="*43,"\n")
        print(" 1. Layanan Bioskop ")
        print(" 2. Exit ")

        while True:
            try:
                pilih = int(input("\nPilihan ==> "))
                break
            except:
                print("Gunakan Angka Saat Menginput Pilihan\n")
                continue
                
        if pilih == 1:
            Bioskop()
        elif pilih == 2:
            print("\nTerimakasih Sudah Menggunakan Program Bioskop La'Winter")
            quit()
        else :
            print("\nPilihan Tidak Tersedia")
            back = input("Apakah anda ingin kembali ? [y/n] \n==>")
            if back == "y":
                continue
            else:
                print("\nTerimakasih Sudah Menggunakan Program Bioskop La Winter")
                quit()


def Bioskop():
    system("cls")
    ulang = "ya"
    while(ulang == "ya"):
        print("="*30)
        print("===       Menu Pilihan     ===")     
        print("="*30)
        print(" 1. Masukkan Data ")
        print(" 2. Tampil Data ")
        print(" 3. Edit Data ")
        print(" 4. Hapus Data ")
        print(" 5. Exit")
        print("="*30)
        
        try:
            pilih = int(input("Masukan Pilihan Anda : "))
        except:
            print("Gunakan Angka Saat Menginput Pilihan\n")
            continue

        if pilih == 1:  
            tambah()

        elif pilih == 2:  
          
            Judul = buat_list(Judul_Film)
            Genre = buat_list(Genre_Film)
            Duration = buat_list(Durasi_Film)
            Studio = buat_list(Studio_Film)

            print_list(Judul, Genre, Duration, Studio)

        elif pilih == 3:  
            edit()

        elif pilih == 4: 
            hapus()

        elif pilih == 5:
            print("\nTerimakasih Sudah Menggunakan Program Bioskop La Winter")
            quit()

        else:
            print("Pilihan Tidak Tersedia")
            ulang = input("Apakah Anda ingin mengulang ? [y/n] \n==>")
            if ulang == "y":
                continue
            else:
                print("\nTerimakasih Sudah Menggunakan Program Bioskop La'Winter")
                quit()

menu_awal()
