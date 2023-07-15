import json

def bubble_sort(data):
    keys = list(data.keys())
    n = len(keys)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if int(keys[j]) > int(keys[j+1]):
                keys[j], keys[j+1] = keys[j+1], keys[j]
    sorted_data = {}
    for key in keys:
        sorted_data[key] = data[key]
    return sorted_data

# Membaca Data dari file JSON
with open('anggotas.json') as file:
    data = json.load(file)

# Mengurutkan data berdasarkan ID Anggota menggunakan Bubble Sort
sorted_data = bubble_sort(data)

# Menampilkan Data yang sudah diurutkan
for member in sorted_data.values():
    print(json.dumps(member, indent=4))
