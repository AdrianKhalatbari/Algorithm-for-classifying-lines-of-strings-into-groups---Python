import csv

try:
    file_name = input("Give the name of the file to read:\n")
    file_name2 = input("Give the name of the file to write:\n")
    brandList = []
    finalBrandList = []
    # ///////////Open and read first file
    with open(file_name, 'r') as vehiclesBrands:
        rentedVehiclesCsv = csv.reader(vehiclesBrands)
        for i in rentedVehiclesCsv:
            if len(i) != 0:
                brandList.append(i[0])
    vehiclesBrands.close()
    # //////////////////Remove repeated brands
    for brand in brandList:
        if brand not in finalBrandList:
            finalBrandList.append(brand)
    # /////////////////////Print Brands
    if len(brandList) == 0:
        print("The file was empty, no car brand was recognized.")
    else:
        print("There were "+str(len(finalBrandList))+" different car brands in the file.")
        for a in finalBrandList:
            print(a, sep = "\n")
        # ////////////////Write to a new file
        with open(file_name2, "w") as finalFile:
            for i in finalBrandList:
                finalFile.write(i)
                finalFile.write("\n")
            finalFile.close()
except FileNotFoundError:
    print("Error processing file '{}', stopping.".format(file_name))
