print("Palindrom bulucu")
sayi=str(input("Lütfen bir sayı giriniz: "))
sayi2=sayi[::-1]
if(sayi==sayi2):
    print("Girdiğiniz sayi palindromdur. ")
else:
    print("girdiğiniz sayi palindrom değildir. ")
