# Belastingschaal / Belastingschijf	Inkomensgrens	        Belastingtarief
# Schijf 1	        Inkomen tot € 19.922	                36,55%
# Schijf 2	        Inkomen tussen € 19.923 en € 33.715	    40,4%
# Schijf 3	        Inkomen tussen € 33.716 en € 66.421	    40,4%
# Schijf 4	        Inkomen vanaf  € 66.422	                52%

if __name__ == '__main__':

    a = int(input("Enter car price: "))
    b = int(input("Enter bijtelling [22]: ") or "22")
    e = int(input("Enter eigen-bijdrage [0]: ") or "0")
    s = int(input("Enter belasting schaal [40]: ") or "40")

    print("Auto kost maand netto: "
          + str(((a * (b/100)/12)-e)
                * (s /  100
                   )
                + e))
