name=input("İsminiz: ")
kg=float(input("Kilonuz: "))
hg=float(input("Boyunuz: "))

index=(kg/(hg)**2)
print("{}sizin kilo indeksiniz{}".format(name,index))
if(index>=0) and (index<=18.4):
    print("Zayıfsınız")
elif(18.4<index<=27.0):
    
    print("İdeal kilodasınız")
else:
    print("Kilolsunuz")
