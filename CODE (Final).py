from msilib import _directories
import zipfile
import time #sdfasdf
import sys
import os
def cls(): return os.system('cls')

# prompt
def more():
    ans = input(
        "\n                       Do you want to do another activity? <Yes or No>? ")

    def cls(): return os.system('cls')

    if ans == 'Yes' or ans == 'yes':
        cls()
        menu()

    elif ans == 'No' or ans == 'no':
        exit(2)
    else:
        print("Invalid answer".center(98))
        more()


# shows the zipping animation
def loading():
    animation = ["[■□□□□□□□□□]".center(98), "[■■□□□□□□□□]".center(98), "[■■■□□□□□□□]".center(98), "[■■■■□□□□□□]".center(98), "[■■■■■□□□□□]".center(
        98), "[■■■■■■□□□□]".center(98), "[■■■■■■■□□□]".center(98), "[■■■■■■■■□□]".center(98), "[■■■■■■■■■□]".center(98), "[■■■■■■■■■■]".center(98)]
    for i in range(len(animation)):
        time.sleep(0.2)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()

# Finding the directory of files to be compressed
def zipdir(_path, zip_handle, zipname, filenames):
    for root, dirs, files in os.walk(_path):
        for file in files:
            if(file != zipname and file in filenames):
                print(" ")
                print(os.path.join(root, file).center(98))
                zip_handle.write(os.path.join(root, file), file)

# compression process
def compressFiles(_path, zipfile_name, file_list, destination_file):
    with zipfile.ZipFile(destination_file, 'w', compression=zipfile.ZIP_DEFLATED, allowZip64=True) as z:
        zipdir(_path, z, zipfile_name, file_list)

    print ("                               Zip file created in " + destination_file)
    return destination_file

def SingleCompresionPage():
    isDone = False
    while not isDone:
        cls()
        
        print("\n================================================================================================")
        print("------------------------------------------------------------------------------------------------")
        print("                      _____ ____  __  __ _____  _____  ______  _____ _____                      ")
        print("                     / ____/ __ \|  \/  |  __ \|  __ \|  ____|/ ____/ ____|                     ")
        print("                    | |   | |  | | \  / | |__) | |__) | |__  | (___| (___                       ")
        print("                    | |   | |  | | |\/| |  ___/|  _  /|  __|  \___ \ ___ \                      ")
        print("                    | |___| |__| | |  | | |    | | \ \| |____ ____) |___) |                     ")
        print("                     \_____\____/|_|  |_|_|    |_|  \_\______|_____/_____/                      ")
        print("\n------------------------------------------------------------------------------------------------")
        print("================================================================================================\n")

        path_input = input("                               Enter directory: ")
        # IDEA : input validation

        if os.path.isdir(path_input):
            # base name of the zip file
            # basename = os.path.basename(path_input)
            basename = input("                               Enter zip file name: ")
            # name of the zip file
            zipfile_name = basename + '.zip'
            
            # desination
            # destination_dir = "C:\\Users\\asus\\Desktop"
            destination_dir = input("                               Enter zip destination: ")
            # IDEA: input validation
            destinationFile = os.path.join(destination_dir, zipfile_name)
            
            print("                               Saving: " + destinationFile)

            file_name = []
            fls = input("                               Enter file name to be compressed: ")
            file_name.append(fls)
            loading()
            compressFiles(path_input, zipfile_name, file_name, destinationFile)

            more()
        else:
            print("Directory doesn't exist".center(98))
            return

def MultipleCopressionPage():
    isDone = False
    while not isDone:
        cls()

        print("\n================================================================================================")
        print("------------------------------------------------------------------------------------------------")
        print("                      _____ ____  __  __ _____  _____  ______  _____ _____                      ")
        print("                     / ____/ __ \|  \/  |  __ \|  __ \|  ____|/ ____/ ____|                     ")
        print("                    | |   | |  | | \  / | |__) | |__) | |__  | (___| (___                       ")
        print("                    | |   | |  | | |\/| |  ___/|  _  /|  __|  \___ \ ___ \                      ")
        print("                    | |___| |__| | |  | | |    | | \ \| |____ ____) |___) |                     ")
        print("                     \_____\____/|_|  |_|_|    |_|  \_\______|_____/_____/                      ")
        print("\n------------------------------------------------------------------------------------------------")
        print("================================================================================================\n")

        path_input = input("                               Enter directory: ")
        # IDEA : input validation

        if os.path.isdir(path_input):
            # base name of the zip file
            # basename = os.path.basename(path_input)
            basename = input("                               Enter zip file name: ")
            # name of the zip file
            zipfile_name = basename + '.zip'
            
            # desination
            # destination_dir = "C:\\Users\\asus\\Desktop"
            destination_dir = input("                               Enter zip destination: ")
            # IDEA: input validation
            destinationFile = os.path.join(destination_dir, zipfile_name)
            
            print("                               Saving: " + destinationFile)

            file_name = []
            x = int(input("\n                               Enter number of files to be compressed: "))
            print("                               Enter Files To Be compressed in " + path_input ) 
            for i in range(1, x + 1):
                fls = input("                               File %d: " %i)
                file_name.append(fls)
            loading()
            compressFiles(path_input, zipfile_name, file_name, destinationFile)
            more()
        else:
            print("Directory doesn't exist".center(98))
            return 
        user_input = input("                                     Do you want to try again (Yes or No)? ")
        if(user_input == 'Yes' or user_input == 'yes' or user_input == 'Y' or user_input == 'y'):
            continue
        else:
            isDone = True
    else:
        # IDEA: return to main menu
        os.system('clear')
        menu()
    
# data decompression
def decompression():
    def cls(): return os.system('cls')
    cls()
    print("\n================================================================================================")
    print("------------------------------------------------------------------------------------------------")
    print("                _____  ______ _____ ____  __  __ _____  _____  ______  _____ _____       ")
    print("               |  __ \|  ____/ ____/ __ \|  \/  |  __ \|  __ \|  ____|/ ____/ ____|      ")
    print("               | |  | | |__ | |   | |  | | \  / | |__) | |__) | |__  | (___| (___        ")
    print("               | |  | |  __|| |   | |  | | |\/| |  ___/|  _  /|  __|  \___ \ ___ \       ")
    print("               | |__| | |___| |___| |__| | |  | | |    | | \ \| |____ ____) |___) |      ")
    print("               |_____/|______\_____\____/|_|  |_|_|    |_|  \_\______|_____/_____/       ")
    print("\n------------------------------------------------------------------------------------------------")
    print("================================================================================================\n")

    # show the available drives in computer
    for drive_letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        if os.path.exists(f'{drive_letter}:'):
            print(f'{drive_letter}:'.center(90))
        else:
            pass
    loc = input("                                     Choose Drive: ")
    loc = loc + "\\"

    # changing directory
    os.chdir(loc)
    cwd = os.getcwd()

    # Print the current working directory
    print("Current working directory: {0}".format(cwd).center(98))

    # Ask user for file to be compressed
    name = (input(
        "\n            Enter the file name you want to decompress(name.zip,test.zip, etc) : "))
    print("")
    print("Unzipping the files...".center(98))
    loading()

    # search the drive
    for root, dirs, files in os.walk(loc):
        if name in files:
            fileLoc = (os.path.join(root, name))
            print("\n" + fileLoc.center(98))
            os.chdir(os.path.join(root))
            with zipfile.ZipFile(name) as item:
                print("")
                print("Unzip completed!".center(98))
                item.extractall()
    more()


def menu():

    print("\n          ,s0#########        ,s0#####0s,             ##########0s,     ############  ")
    print("        s'0d##########      s'0d#######d0's           ###########0s,    ############  ")
    print("       ^d###               ^d###       ###d^     0#0  #####     Y##0b   #####         ")
    print("     ^d####              ^d####         ####b^   0#0  #####      Y##0b  #####         ")
    print("    N#####              N#####           #####N       #####       V##0  ###########   ")
    print("    #####C              #####C           >#####       #####       V##0  ###########   ")
    print("    ######              ######           ######       #####       >##0  ###########   ")
    print("     ,#####              ,#####         #####,   0#0  #####      Y##0P  #####         ")
    print("       ,V###               ,V###       ###V,     0#0  #####     Y##0P   #####         ")
    print("        s,0############     s,0#########0,s           ###########0s'    ############  ")
    print("          ^s###########       ^s#######s^             ##########0s'     ############  \n")
    print("")
    print("Team B | File COmpression and DEcompression Program.".center(98))
    print("")

    menuPrint = [
        "Single Compression  ",
        "Multiple Compression",
        "Decompress          ",
        "Exit                ",
    ]

    for i in range(len(menuPrint)):
        print("{} {}".format([i+1], menuPrint[i]).center(98))

    choice = int(
        input("\n                                     Enter your choice: "))
    while choice != 0:
        if choice == 1:
            SingleCompresionPage()
            break
        elif choice == 2:
            MultipleCopressionPage()
            break
        elif choice == 3:
            decompression()
            break
        elif choice == 4:
            exit()
        else:
            print("Invalid choice".center(98))

# calling the functions
#####################################################################################


menu()
