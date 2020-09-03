from data import *



class Employee:

    def __init__(self, data):
        self.data = data

    def create(self, val):
        val = list(val.items())
        # ubah ke tuple, sifat tuple tidak bisa di ubah atau hapus, namun bisa diisi dengan berbagai macam nilai dan object
        val.insert(0,("id",self.data[len(self.data) - 1]["id"] + 1)) # setelah itu kan jadi array jadi bisa prepemd id
        # fungsi insert ini untuk memasukan nilai kedalam array, kenapa - 1? karena mengambil nilai terakhirnya dan ["id"] + 1, increment +1
        self.data.append(dict(val))
        # fungsi append disini untuk menambah item dari belakang
        return self.data

    def delete(self, id):
        for i, val in enumerate(self.data): # Fungsi enumerate() mengembalikan objek enumerate yaitu objek iterable yang tiap itemnya berpasangan dengan indeks.
            if val['id'] == id:
                del self.data[i] # fungsi del ini adalah untuk menghapus object
        return self.data

    def read(self):
        return self.data
        
    def update(self, id, val):
        for i, val in enumerate(self.data):
            if val['id'] == id:
                val = list(val.items())
                val.insert(0,("id",id)) # menambah item id dari depan
                self.data[i] = dict(val)
        return self.data

employee = Employee(data)
create_employee = employee.create({"fullname":"ratna putri", "address":"jakarta", "salary":5000000, "phone":"099903"}) #id generate secara otomatis ketika data bertambah
create_employee_2 = employee.create({"fullname":"mega mendung", "address":"jakarta", "salary":10000000, "phone":"343234"})
delete_employee = employee.delete(2) #menghapus data employe dengan id 2
read_employee = employee.read() #return semua data employee yang sudah ditambahkan
update_employee = employee.update(4,{"fullname":"raisa andriana", "address":"bekasi", "salary":1000000, "phone":"9939999"}) #mengubah data dengan id 2, return semua data employee

# print(create_employee)
# print(create_employee_2)
# print(delete_employee)
# print(read_employee)
# print(update_employee)