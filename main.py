# KONSTRUKSI DASAR PYTHON
# SEQUENTIAL: Eksekusi berurutan
print('Hello World')
print('by Enterprise Analytica')
print('30 Juni 2021')
print('-' * 10)

# PERCABANGAN: Eksekusi terpilih
ingin_cepat = True
if ingin_cepat:
    print('jalan lurus saja')
else:
    print('Jalan lain')

print('-' * 4)

# PERULANGAN
jumlah_karyawan = 4
print('Hello team #1')
print('Hello team #2')
print('Hello team #3')
print('Hello team #4')

for index_anak in range(1, jumlah_karyawan+1):
    print(f'Halo karyawan ke {index_anak}')
