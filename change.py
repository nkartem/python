#Open the file, search parameters, and change him in new FileLists2
import os

IS_PROD = "to111111"
IS_PARAMETER = "to222222"
IS_DNS = "to33333"


with open ('FileLists.txt', 'r') as f:
    with open ('FileLists2.txt', 'w') as f2:
        for line in f:
        
            if 'SET(IS_PROD'  in line:
                print(line, " change to  ", IS_PROD )
                new_data_1 = line.replace("OFF", IS_PROD)
                f2.write(new_data_1)
            elif 'SET(IS_PARAMETER'  in line:
                print(line, " change to  ", IS_PARAMETER )
                new_data_1 = line.replace("ON", IS_PARAMETER)
                f2.write(new_data_1)
            elif 'SET(IS_DNS'  in line:
                print(line, " change to  ", IS_DNS )
                new_data_1 = line.replace("OFF", IS_DNS)
                f2.write(new_data_1)                
            else:       
                f2.write(line) 
    f.close()
    f2.close()

os.rename("CMakeLists.txt", "CMakeLists_orig.txt")
os.rename("CMakeLists2.txt", "CMakeLists.txt")

exit();