# tipe data skalar = tipe data sederhana
karyawan1 = 'Eko'
karyawan2 = 'Dwi'
karyawan3 = 'Tri'
karyawan4 = 'Catur'

print(karyawan1)
print(karyawan2)
print(karyawan3)
print(karyawan4)

# tipe data list/daftar/array
karyawan = ['Eko', 'Dwi', 'Tri', 'Catur']
print(karyawan)
karyawan.append('Panca')
print(karyawan)

# panggil karyawan ke-02
print('sapa karyawan ke-02')
print(f'Hai {karyawan[2]}')

print('\nsapa seluruh karyawan')
for i in karyawan:
    print(f'Hai {i}')

print('\nsapa seluruh karyawan cara lain')
for i in range(0, len(karyawan)):
    print(f'Hai {karyawan[i]}')