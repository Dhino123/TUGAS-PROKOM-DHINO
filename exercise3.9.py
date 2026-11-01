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

print(f"gw ngajak {len(orang)} orang main ke jogja")