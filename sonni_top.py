import  random as r
def son_top():
    print("Created by bekzodjon_python_master")
    print("Sonni top1 o'yinini o'ynaymiz ")
    b = int(input("1 dan nechchigacha sonlar oralig'i tanlang: ="))
    a = r.randint(1, b)   
    taxminlar = 0
    while True:
        taxminlar += 1
        f = int(input(f"1 dan {b} gacha son o'yladim topa olasizmi. Boshladik son yozing = "))
        if f < a:
            print("men o'ylagan son bundan katta. Yana urunib ko'ring: ")
        elif f > a:
            print("men o'ylagan son bundan kichik. Yana urunib ko'ring: ")
        else:  
            break           
    print(f"Topdiz! {taxminlar} ta urunishda Tabriklayman!!")
    input("Dastur haqida fikringizni qoldiring = > ")
        
son_top()
