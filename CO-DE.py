from msilib import _directories
import zipfile
import time
import sys
import os

def cls(): return os.system('cls') # clear screen

# prompt
def more():
    ans = input("\n                       Would you like to do another activity? (Yes or No) ")

    if ans == 'Yes' or ans == 'yes' or ans == 'Y' or ans == 'y':  # if yes, babalik sa main menu
        menu()

    elif ans == 'No' or ans == 'no' or ans == 'N' or ans == 'n':  # if no mateterminate program
        exit()
    else: # if yung input is other than yes or no, magaask ulit
        print("Invalid answer".center(98))
        more()

# shows the zipping animation
def loading():
    animation = ["[■□□□□□□□□□]".center(98), "[■■□□□□□□□□]".center(98), "[■■■□□□□□□□]".center(98), "[■■■■□□□□□□]".center(98), "[■■■■■□□□□□]".center(98), "[■■■■■■□□□□]".center(98), "[■■■■■■■□□□]".center(98), "[■■■■■■■■□□]".center(98), "[■■■■■■■■■□]".center(98), "[■■■■■■■■■■]".center(98)]
    for i in range(len(animation)):
        time.sleep(0.2)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()

# compression process
def compressFiles(_path, zipfile_name, file_list, destination_file):
    with zipfile.ZipFile(destination_file, 'w', compression=zipfile.ZIP_DEFLATED, allowZip64=True) as z: 
        zipdir(_path, z, zipfile_name, file_list)
    print("                               Zip file created in " + destination_file)
    return destination_file

# Finding the directory of files to be compressed
def zipdir(_path, zip_handle, zipname, filenames):
    for file in filenames:
        print(" ")
        print(os.path.join(_path, file).center(98))
        zip_handle.write(os.path.join(_path, file), file)

# Exception handling prompt for Single Compression
def singDirError():
    user_input = input("                               Would you like to try again? (Yes or No) ")
    if(user_input == 'Yes' or user_input == 'yes' or user_input == 'Y' or user_input == 'y'): # if yes, babalik sa single compression function
        SingleCompresionPage()
    elif(user_input == 'No' or user_input == 'no' or user_input == 'N' or user_input == 'n'): # if no, pupunta sa main menu
        menu()
    else: # if hindi yes or no, magpprompt lang ulit
        print("Invalid Input.".center(98))
        singDirError()

# single compression page
def SingleCompresionPage():
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
    try:  # exception handling
        path_input = input("                               Enter drive letter (C:, D:, etc...): ")

        if os.path.isdir(path_input):  # to check if the drive exists
            # name of the zip file to be created
            basename = input("                               Enter name for the archive: ")
            zipfile_name = basename + '.zip'  # name of the zip file including extension

            # output desination
            destination_dir = input("                               Enter archive destination directory: ")
            destination_dir_list = os.listdir(destination_dir)

            destinationFile = os.path.join(destination_dir, zipfile_name)

            print("                               Saving: " + destinationFile)

            file_name = [] # variable declaration for Line 92: file_name.append(fls)

            # Exception handling for input handling
            isDone = False
            while not isDone:
                fls = input("                               Enter the file to be compressed: ")
                if(fls in destination_dir_list):
                    file_name.append(fls)
                    isDone = True
                else:
                    print("The filename you entered doesn't exist!".center(98))
                    print(" ")

            loading()  # loading animation
            compressFiles(destination_dir, zipfile_name, file_name, destinationFile)  # file compression function

            more()  # prompt
        else:  # if the drive does not exist
            print(" ")
            print("Directory doesn't exist.".center(98))
            singDirError()  # exception handling prompt for single compression
    except Exception:  # exception handling
        print(" ")
        print(
            "Runtime Error: Operation canceled. Kindly check your input.".center(98))
        singDirError()  # exception handling prompt for single compression

# Exception handling prompt for Multiple Compression
def multiDirError():
    user_input = input("                               Would you like to try again? (Yes or No) ")
    if(user_input == 'Yes' or user_input == 'yes' or user_input == 'Y' or user_input == 'y'): # if yes, babalik sa multiple compression function
        MultipleCopressionPage()
    elif(user_input == 'No' or user_input == 'no' or user_input == 'N' or user_input == 'n'):  # if no, pupunta sa main menu
        menu()
    else: # if hindi yes or no yung input, magpprompt lang ulit
        print("Invalid Input.".center(98))
        multiDirError()

# multiple compression page
def MultipleCopressionPage():
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

    try:  # exception handling
        # drive letter kung saan manggagaling yung mga icocompress
        path_input = input("                               Enter drive letter (C:, D:, etc...): ")

        if os.path.isdir(path_input): # check if the directory exists
            basename = input("                               Enter name for the archive: ") # name of the zip file to be created
            zipfile_name = basename + '.zip' # name of zip file including its extension

            # output desination
            destination_dir = input("                               Enter archive destination directory: ")
            destination_dir_list = os.listdir(destination_dir)

            destinationFile = os.path.join(destination_dir, zipfile_name)

            print("                               Saving: " + destinationFile)

            file_name = [] # declare lang ng variable para sa Line 166: file_name.append(fls)

            x = int(input("\n                               Enter number of files to be compressed: ")) # kung ilang files yung isasama sa archive
            print("                               Enter the files to be compressed in " + path_input) # filename ng mga files na icocompress kasama file extensions

            for i in range(1, x + 1):  # for loop lang ng pagprint ng File numbers
                isDone = False
                while not isDone:
                    fls = input("                               File %d: " % i)
                    if(fls in destination_dir_list): # Exception handling for input handling
                        file_name.append(fls)
                        isDone = True
                    else:
                        print("The filename you entered doesn't exist!".center(98))
                        print(" ")

            loading()  # loading animation
            compressFiles(destination_dir, zipfile_name, file_name, destinationFile)  # compressing files
            more()  # prompt
        else:  # if hindi nageexist yung drive
            print(" ")
            print("Directory doesn't exist".center(98))
            multiDirError()  # exception handling prompt for multiple compression

    except Exception:  # exception handling for wrong destination
        print(" ")
        print(
            "Runtime Error: Operation canceled. Kindly check your input.".center(98))
        multiDirError()  # exception handling prompt for multiple compression

# Exception handling prompt for Decompression
def decompDirError():
    user_input = input("                               Would you like to try again? (Yes or No) ")
    if(user_input == 'Yes' or user_input == 'yes' or user_input == 'Y' or user_input == 'y'):    # if yes, babalik sa decompression function
        decompression()
    elif(user_input == 'No' or user_input == 'no' or user_input == 'N' or user_input == 'n'):  # if no, babalik sa main menu
        menu()
    else:  # if mali yung input ni user
        print("Invalid Input.".center(98))
        decompDirError()

# data decompression
def decompression():
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

    try:  # exception handling

        # output path
        zip_dir_path = input("                               Enter archive path: ")
        zip_dir_path_dir_list = os.listdir(zip_dir_path)

        # Print the current working directory
        print("Current working directory: {0}".format(zip_dir_path).center(98))

        # Exception handling for input handling
        isDone = False
        while not isDone:
            name = (input("\n            Enter the archive name you want to decompress(name.zip,test.zip, etc): "))
            if(name in zip_dir_path_dir_list):
                isDone = True
            else:
                print("The filename you entered doesn't exist!".center(98))
                print(" ")

        print("")
        print("Unzipping the files...".center(98))
        loading()

        # search the drive
        fileLoc = (os.path.join(zip_dir_path, name))
        print("\n" + fileLoc.center(98))
        os.chdir(os.path.join(zip_dir_path)) # to set kung saang directory maghahanap yung program
        with zipfile.ZipFile(name) as item:
            print(" ")
            print("Unzip completed!".center(98))
            item.extractall()
        more()
    except Exception:  # exception handling for decompress function
        print(" ")
        print("Runtime Error: Operation canceled. Kindly check your input.".center(98))
        decompDirError()  # exception handling prompt for decompress function

# main menu
def menu():
    cls()

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

    choice = (input("\n                                     Enter your choice: "))

    # choice is compared as a string because python is strongly typed
    if choice == str('1'):
        SingleCompresionPage()
    elif choice == str('2'):
        MultipleCopressionPage()
    elif choice == str('3'):
        decompression()
    elif choice == str('4'):
        exit()
    else:
        print(" ")
        print("Invalid Input".center(98))
        print("Enter any key to continue...".center(98))
        input("                                ") # maraming spaces para nakacenter yung input cursor, di kasi gumagana string formatting sa user input strings.
        menu()

menu()