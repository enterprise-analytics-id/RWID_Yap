"""
Tipe data dictionary sekedar menghubungkan antara Key dan VALU
KVP = Key Value Pair
Dictionary = Kamus
"""

# kamus_ind_en = {}
# kamus_ind_en['anak'] = 'child'
# kamus_ind_en['istri'] = 'wife'
# kamus_ind_en['ayah'] = 'father'
# kamus_ind_en['ibu'] = 'mother'
#
# print(kamus_ind_en)
# print(kamus_ind_en['ayah'])
# print(kamus_ind_en['ibu'])


# kamus_ind_en = {'anak': 'child', 'istri': 'wife', 'ayah': 'father', 'ibu': 'mother'}
#
# print(kamus_ind_en)
# print(kamus_ind_en['ayah'])
# print(kamus_ind_en['ibu'])

print('data ini dikirimkan oleh server gojek untuk memberikan info driver di sekitar pemakai aplikasi')
data_dari_server_gojek = {
    'tanggal': '2020-06-10',
    'driver_list': [{'nama': 'Eko', 'jarak': 10},
                    {'nama': 'Dwi', 'jarak': 50},
                    {'nama': 'Tri', 'jarak': 30},
                    {'nama': 'Catur', 'jarak': 40}]
}

print(data_dari_server_gojek)
print(f"Driver di sekitar sini {data_dari_server_gojek['driver_list']}")
print(f"\nDriver #1 {data_dari_server_gojek['driver_list'][0]}")
print(f"\nDriver terdekat berjarak {data_dari_server_gojek['driver_list'][0]['jarak']} meter")
