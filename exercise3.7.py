orang = ["asep", "yanto", "bayu"]

print(f"woi {orang[0]}, lu gw ajak.")
print(f"woi {orang[1]}, lu gw ajak.")
print(f"woi {orang[2]}, lu gw ajak.")

print(f"{orang[1]} ga mau ah")
orang[1] = "ijam suki"

print(f"woi {orang[0]}, lu gw ajak")
print(f"woi {orang[1]}, lu gw ajak")
print(f"woi {orang[2]}, lu gw ajak")

print("sepi amat, ngajak otrang lain lagi dah")

orang.insert(0, "otid")
orang.insert(2, "dono")
orang.append("ucok")

print(f"woi {orang[0]}, lu gw ajak ")
print(f"woi {orang[1]}, lu gw ajak ")
print(f"woi {orang[2]}, lu gw ajak ")
print(f"woi {orang[3]}, lu gw ajak ")
print(f"woi {orang[4]}, lu gw ajak ")
print(f"woi {orang[5]}, lu gw ajak ")

print("eh sorry bre, mobilnya cuma bisa diisi 2 orang")

ditolak = orang.pop()
print(f"Maaf {ditolak}, lu ga jadi gw ajak.")
ditolak = orang.pop()
print(f"Maaf {ditolak}, lu ga jadi gw ajak.")
ditolak = orang.pop()
print(f"Maaf {ditolak}, lu ga jadi gw ajak.")
ditolak = orang.pop()
print(f"Maaf {ditolak}, lu ga jadi gw ajak.")

print(f"Halo {orang[0]}, lu tetep gw ajak")
print(f"Halo {orang[1]}, lu tetap gw ajak")

del orang[1]
del orang[0]
print(orang)