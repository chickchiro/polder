from msilib import _directories
from pickle import FALSE
import zipfile
import os

def zipdir(_path, zip_handle, zipname, filenames):
    for root, dirs, files in os.walk(_path):
        for file in files:
            if(file != zipname and file in filenames):
                print( os.path.join(root, file))
                zip_handle.write(os.path.join(root, file), file)

    

def multiplecompression(_path):
    if os.path.isdir(_path):
        # base name of the zip file
        # basename = os.path.basename(_path)
        basename = input("enter zip file name: ")
        # name of the zip file
        zipfile_name = basename + '.zip'
        
        # desination
        # destination_dir = "C:\\Users\\asus\\Desktop"
        destination_dir = input("Enter zip destination: ")
        # IDEA: input validation
        destinationfile = os.path.join(destination_dir, zipfile_name)
        
        print( "saving: " + destinationfile)

        file_name = []
        x = int(input("\nEnter number of files to be compressed: "))
        print("Enter Files To Be compressed in " + _path )
        for i in range(0, x ):
            fls = input("File %d: " %i)
            file_name.append(fls)
            

        with zipfile.ZipFile(destinationfile, 'w', compression=zipfile.ZIP_DEFLATED, allowZip64=True) as z:
            zipdir(_path, z, zipfile_name, file_name)
        
        print ("zip file created in " + destinationfile)

        return destinationfile
    else:
        print("Directory doesn't exist")
        return 



isDone = False
while not isDone:
    path_input = input("Enter directory: ")
    # IDEA : input validation
    multiplecompression(path_input)

    user_input = input("Do you want to try again(y/n)? ")
    if(user_input == 'y'):
        continue
    else:
        isDone = True
else:
    # IDEA: return to main menu
    os.system('clear')
    print("Thank youu!")


