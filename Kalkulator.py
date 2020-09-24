print("Kalkulator 2.0")

a = int(input("Unesi A:"))
b = int(input("Unesi B:"))
print("")

print("Unesi slovo operacije:")
print("a) sabiranje;")
print("b) oduzimanje;")
print("c) množenje;")
print("d) deljenje.")
operacija = (input("Unesi operaciju:"))
print("")

if operacija=="A" or operacija=="a" or operacija=="sabiranje" or operacija=="Sabiranje" or operacija=="SABIRANJE" or operacija=="sABIRANJE":
     print("Odgovor je:", a+b)
elif operacija=="B" or operacija=="b" or operacija=="oduzimanje" or operacija=="Oduzimanje" or operacija=="ODUZIMANJE" or operacija=="oDUZIMANJE":
     print("Odgovor je:", a-b)     
elif operacija=="C" or operacija=="c" or operacija=="množenje" or operacija=="Množenje" or operacija=="MNOŽENJE" or operacija=="mNOŽENJE" or operacija=="mnozenje" or operacija=="Mnozenje" or operacija=="MNOZENJE" or operacija=="mNOZENJE":
     print("Odgovor je:", a*b)
elif operacija=="D" or operacija=="d" or operacija=="deljenje" or operacija=="Deljenje" or operacija=="DELJENJE" or operacija=="dELJENJE":
     print("Odgovor je:", a/b)
else:
     print("Računska operacija nepostoji ili je nepravilno napisana!")

exit_line = ("Klikni enter da izađeš.")
