# data string
data_nama = "Muhammad Jidan"
data_tinggi = 164
data_umur = 20
data_nomor_sepatu = 40
data_string = f"""
nama {'=':>9} {data_nama}
tinggi {'=':>7} {data_tinggi}
umur {'=':>9} {data_umur}
nomor sepatu {'='} {data_nomor_sepatu}
"""
# >1 memberikan spasi ke kanan sebanyak 1
print(f'{5 * "-"}DATA STRING{5 * "-"}')
print(data_string)