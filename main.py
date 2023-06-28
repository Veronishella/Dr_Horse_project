from veterinar import Veterinar
from veterinar import Veterinarlist
from menu import Menu

veterinari_list = Veterinarlist()
veterinari_list.pripojit_databazu("zoznam.db")
veterinari_list.nacitat_veterinarov()
menu = Menu()

menu.zobraz_menu()
choice = int(input("Zadajte volbu: "))

while (True):
    while choice in (1, 2, 3, 4):

        if choice == 1:
            veterinari_list.vypis_zoznam_veterinarov()
            menu.zobraz_menu()
            choice = int(input("Zadajte volbu: ")) 

        elif choice == 2:
            veterinari_list.uloz_veterinara(jmeno=str(input("Zadej jméno: ")), 
                                            prijmeni=str(input("Zadej příjmení: ")), 
                                            kraj=str(input("Zadej kraj: ")), 
                                            mesto_1=str(input("Zadej město: ")), 
                                            mesto_2=str(input("Zadej město: ")), 
                                            mesto_3=str(input("Zadej město: ")), 
                                            mobil=int(input("Zadej mobil: ")), 
                                            email=str(input("Zadej email: ")), 
                                            web=str(input("Zadej web: ")))

            menu.zobraz_menu()
            choice = int(input("Zadejte volbu: ")) 

        elif choice == 3:
            print("1. Vyhledej veterináře podle jména a příjmení")
            print("2. Vyhledej veterinaře podle města")
            print("3. Vrátit se na hlavni menu")
            choice = int(input("Zadejte volbu: "))

            if choice == 1:
                veterinari_list.vyhledej_veterinara_jmeno_prijmeni(jmeno=str(input("Zadejte jméno: ")), prijmeni=str(input("Zadejte příjmení: ")))                    
                menu.zobraz_menu()
                choice = int(input("Zadejte volbu: "))

            elif choice == 2:
                veterinari_list.vyhledej_veterinara_mesto(mesto=str(input("Zadejte město: ")))
                menu.zobraz_menu()
                choice = int(input("Zadejte volbu: "))

            elif choice == 3:
                menu.zobraz_menu()
                choice = int(input("Zadajte volbu: "))

            else:
                print("Nespravny vstup")
                menu.zobraz_menu()
                choice = int(input("Zadejte volbu: "))

        elif choice == 4:
            exit()
            
    else:
        print("Nesprávna volba")
        menu.zobraz_menu()
        choice = int(input("Zadejte volbu: "))















#veterinari_list.vypis_zoznam_veterinarov()

#veterinari_list.uloz_veterinara("Adam", "Biely","Liberecký kraj", "Liberec", "Jablonec nad Nisou", "Česká Lípa", "101202303", "ada@dva.cz", "www.osemplusjedna.cz")
#veterinari_list.vypis_zoznam_veterinarov()
#veterinari_list.vyhledej_veterinara_jmeno_prijmeni("Daniel")
#veterinari_list.vyhledej_veterinara_mesto("Chomutov")
#veterinari_list.odpojit_databazu()