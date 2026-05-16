import pywhatkit as p
from colorama import Fore, Style, init
init()
import time
def agri_store(option):
    c = 0
    if option == "1":
        print("What seeds do you need?\n1.Maize\n2.Paddy\n3.Gingelly")
        seeds = input("Enter the number:")
        acre = float(input("How much acres are you cultivating?\n"))

        if seeds == "1":
            print(Fore.CYAN + "1.Syngenta's 'NK 6240' Duration:110 ₹400/kg Days\n2.Pioneer's 'P3302' Duration:100 Days ₹420/kg")
            print("3.PAC's '740' Duration:120 Days ₹380/kg\n4.Mahyco's 'MRM 4065' Duration:140 Days ₹430/kg" + Style.RESET_ALL)
            v1 = input("Enter the number:")
            if v1 == "1":
                print("8Kg is needed for an acre")
                c = acre * 3200
            elif v1 == "2":
                print("8Kg is needed for an acre")
                c = acre * 3360
            elif v1 == "3":
                print("7.2Kg is needed for an acre")
                c = acre * 2736
            elif v1 == "4":
                print("7.2Kg is needed for an acre")
                c = acre * 3096

            herb = input("Do you need pre emergence herbicide? (yes/no): ")
            if herb == "yes":
                c += acre * 450

        elif seeds == "2":
            print(Fore.CYAN+"We have\n1.ADT 45 Duration 120 Days,Moderate water requirement\n2.Bhavani\White Ponni Duration 140 Days,High Water requirement")
            print("3.CR1009(Ponmani) Duration 160+ Days,High yielding Variety with high water requirement"+Style.RESET_ALL)
            v2 = input("Enter number:")
            if v2 == "1":
                print("The seed per acre is 30Kg and Cost per kg is Rs.30")
                c = acre * 900
            elif v2 == "2":
                print("The seed per acre is 20Kg and Cost per kg is Rs.40")
                c = acre * 800
            elif v2 == "3":
                print("The seed per acre is 20Kg and Cost per kg is Rs.60")
                c = acre * 1200

        elif seeds == "3":
            print(Fore.CYAN+"We have new varieties called\n1.TMV 4 Duration 90 Days, Oil content 50%\n2.VRI 2 Duration 90 Days, Better drought Tolerance")
            print("3.CO 4 Duration 100 Days, High yielding variety, Better Pest tolerance"+Style.RESET_ALL)
            print("What do you need")
            v3 = input("Enter number:")
            if v3 == "1":
                print("The seed per acre is 3kg and it costs Rs.100 per Kg")
                c = acre * 300
            elif v3 == "2":
                print("The seed per acre is 2.5kg and it costs Rs.120 per Kg")
                c = acre * 300
            elif v3 == "3":
                print("The seed per acre is 3.5kg and it costs Rs.140 per Kg")
                c = acre * 490

    elif option == "2":
        acre = float(input("Enter the acres of cultivation:\n"))
        print(Fore.CYAN+"1.Urea-Rs.300/Bag\n2.20:20:0:0-Rs.1400/Bag\n3.Diammonium Phosphate(DAP)-Rs.1300/Bag\n4.Ammonium Sulphate-1800/Bag")
        print("5.Potash- Rs.1800/Bag\n6.Neem Cake-1100/Bag\n7.Zinc Sulphate(6Kg)-120/Bag\n8.Mycore(6Kg)-Rs.720/Bag"+Style.RESET_ALL)
        print("1.Maize\n2.Paddy\n3.Turmeric")
        fert = input("Enter the number:")

        if fert == "1":
            print("What is the stage of the crop?\n1.0-15 Days\n2.25-30 Days\n3.50-55 Days")
            f = input("Enter the number:")
            if f == "1":
                print("You need 2 Bags of Urea and 1 Bag of Ammonium Phosphate Sulphate(20:20:0:0) and 6Kg of Zinc sulphate per acre")
                c = acre * 2120
            elif f == "2":
                print("You need 1 Bag of urea and 25Kg of Potash")
                c = acre * 1200
            elif f == "3":
                print("You need 25Kg of Urea and 25Kg of Potash")
                c = acre * 1050

        elif fert == "2":
            print("What is the stage of the crop?\n1.0-10 Days\n2.35-40 Days\n3.Above 60 Days")
            f = input("Enter the number:")
            if f == "1":
                print("You need 2 bags of DAP per acre and 2 Bags of Neem Cake")
                c = acre * 4800
            elif f == "2":
                print("You need 2 Bags of Ammonium Phosphate per acre and 20Kg of Potash")
                c = acre * 4320
            elif f == "3":
                print("You need 1 Bag of Ammonium Sulphate and 20Kg of Potash")
                c = acre * 2520

        elif fert == "3":
            print("What is the stage of the crop")
            print("1.0-10Days\n2.80-90 Days\n3.Above 150 Days")
            f = input("Enter the number:")
            if f == "1":
                print("You need 2 Bags of 20:20:0:0")
                c = acre * 2800
            elif f == "2":
                print("You need 4 Bags of 20:20:0:0,2 Bags of urea,2 Bags of Potash,2 Bags of Mycore,4 Bags of Neem Cake")
                c = acre * 15040
            elif f == "3":
                print("You need 1 Bag of Ammonium sulphate and 1 Bag of Potash at interval of two months")
                c = acre * 3600

    elif option == "3":
        acre = float(input("Enter the acres of cultivation:\n"))
        print("1.Pesticides\n2.Fungicides")
        chem = input("Enter the number:")

        if chem == "1":
            print(Fore.CYAN+"Delegate(180ml)-Rs.1800\nImidacloprid(100ml)\nCartap Hydrochloride(500Gm)-Rs.600\nLambda-cyhalothrin(200Ml)-Rs.300")
            print("All chemicals to be diluted in 100Liters of Water and to be sprayed"+Style.RESET_ALL)
            print("1.Maize\n2.Paddy")
            crop = input("Enter the number:")
            if crop == "1":
                print("Delegate(Spinetorum) which is best for Maize's Bollworms,Leaf miners where you need 180ml/acre")
                c = acre * 1800
            elif crop == "2":
                print("1.Stem borer\n2.Leaf folder")
                p = input("Enter the number:")
                if p == "1":
                    print("You need Cartap Hydrochloride(500Gm) and Imidacloprid(100Ml)")
                    c = acre * 750
                elif p == "2":
                    print("You need Lambda-cyhalothrin(200Ml)")
                    c = acre * 300

        elif chem == "2":
            print(Fore.CYAN+"Carbendazim(1Kg)-₹1400\nPropiconazole(250Ml)-₹600\nMancozeb(1kg)-₹900"+Style.RESET_ALL)
            print("All chemicals to be diluted in 100Liters of Water and to be sprayed")
            print("1.Turmeric\n2.Groundnut")
            crop = input("Enter the number:")
            if crop == "1":
                print("You need Carbendazim(500Gm) and Propiconazole(250Ml)")
                c = acre * 1300
            elif crop == "2":
                print("You need Mancozeb(500Gm)")
                c = acre * 450
    return c
total_bill = 0

while True:
    print(Fore.LIGHTGREEN_EX + "Welcome to Agri Store" + Style.RESET_ALL)
    print("1.Seeds")
    print("2.Fertilizers")
    print("3.Chemicals")
    print("4.Exit")

    option = input("Enter your option: ")

    if option == "4":
        print("Processing your order...")
        time.sleep(5)
        print("\nFinal Bill: ₹", total_bill)
        print('Collect your items at gate 7\nThank you! Visit again ')
        break

    elif option in ["1", "2", "3"]:
        cost = agri_store(option)
        total_bill += cost
        print("Current Total: ₹", total_bill)

    else:
        print("Invalid choice, try again")
p.sendwhatmsg("+918098129280","The total bill"+str(total_bill),20,35)
