def buat_motor(merek, tipe, **tambahan):
    motor = {"merek": merek, "tipe": tipe}
    motor.update(tambahan)
    return motor

motor1 = buat_motor("honda", "vario", warna="merah", bagasi=True)
motor2 = buat_motor("yamaha", "nmax", warna="hitam", tahun=2022)

print(motor1)
print(motor2)