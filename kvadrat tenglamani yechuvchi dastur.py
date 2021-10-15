from math import sqrt
print("C-R-E-A-T-E-D B-Y {{{{B-E-K-Z-O-D-J-O-N_P-Y-T-H-O-N_M-A-S-T-E-R}}}}")
chiqish = input("Chiqish uchun {exit deb yoz}. chiqmoqchi bo'lmasangiz xoxlagan narsangizni yozing = ")
while chiqish != 'exit':
    a = int(input("a ni kiriting = "))
    b = int(input("b ni kiriting = "))
    c = int(input("c ni kiriting = "))
    diskriminat = (b**2)-(4*a*c)
    if diskriminat > 0:
        x1 = (-b+sqrt(diskriminat))/2*a
        x2 = (-b-sqrt(diskriminat))/2*a
        print("x1 = ",x1)
        print("x2 = ",x2)
        print("GITHUB USERNAME == bekzodjon2006")
        chiqish = input("Chiqish uchun {exit deb yoz}. chiqmoqchi bo'lmasang xoxlagan narsangni yoz ")
        while chiqish != 'exit':
            break
    else:
        print("Diskrimant yechimga ega emas! Chunki diskriminant o dan kichik ekan")
        print("GITHUB USERNAME == bekzodjon2006")
        chiqish = input("Chiqish uchun {exit deb yoz}. chiqmoqchi bo'lmasang xoxlagan narsangni yoz ")
        while chiqish != 'exit':
            break
