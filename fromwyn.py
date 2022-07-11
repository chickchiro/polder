from msilib import _directories
import zipfile
import time
import sys
import os


def cls(): return os.system('cls')

# prompt


def more():
    ans = input(
        "\n                       Would you like to do another activity? (Yes or No)? ")

    def cls(): return os.system('cls')

    if ans == 'Yes' or ans == 'yes':  # if yes, babalik sa main menu
        cls()
        menu()

    elif ans == 'No' or ans == 'no':  # if no mateterminate program
        exit()
    else:
        # if yung input is other than yes or no, magaask ulit
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

    print("                               Zip file created in " + destination_file)
    return destination_file


# Exception handling prompt for Single Compression
def singDirError():
    user_input = input(
        "                               Would you like to try again? (Yes or No) ")
    # if yes, babalik sa single compression function
    if(user_input == 'Yes' or user_input == 'yes' or user_input == 'Y' or user_input == 'y'):
        SingleCompresionPage()
    elif(user_input == 'No' or user_input == 'no' or user_input == 'N' or user_input == 'n'):  # if no, pupunta sa main menu
        menu()
    else:  # if hindi yes or no, magpprompt lang ulit
        print("Invalid Input.".center(98))
        singDirError()

# single compression page


def SingleCompresionPage():
    # isDone = False
    # while not isDone:
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
        path_input = input(
            "                               Enter drive letter: ")

        if os.path.isdir(path_input):  # to check if the drive exists
            # name of the zip file to be created
            basename = input(
                "                               Enter name for the archive: ")
            zipfile_name = basename + '.zip'  # name of the zip file including extension

            # output desination
            destination_dir = input(
                "                               Enter archive destination directory: ")
            destination_dir_list = os.listdir(destination_dir)
            # --------------------------------- PRINT DIR LIST -------
            print("Files and directories in '", destination_dir, "' :")
            print(destination_dir_list)
            # --------------------------------- PRINT DIR LIST -------

            destinationFile = os.path.join(destination_dir, zipfile_name)

            print("                               Saving: " + destinationFile)

            file_name = []

            isDone = False
            while not isDone:
                fls = input(
                    "                               Enter the file to be compressed: ")
                if(fls in destination_dir_list):
                    file_name.append(fls)
                    isDone = True
                else:
                    print("The filename you entered doesn't exist!")

            loading()  # loading animation
            compressFiles(path_input, zipfile_name, file_name,
                          destinationFile)  # file compression function

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
    user_input = input(
        "                               Would you like to try again? (Yes or No) ")
    # if yes, babalik sa multiple compression function
    if(user_input == 'Yes' or user_input == 'yes' or user_input == 'Y' or user_input == 'y'):
        MultipleCopressionPage()
    elif(user_input == 'No' or user_input == 'no' or user_input == 'N' or user_input == 'n'):  # if no, pupunta sa main menu
        menu()
    else:
        # if hindi yes or no yung input, magpprompt lang ulit
        print("Invalid Input.".center(98))
        multiDirError()

# multiple compression page


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
        try:  # exception handling
            # drive letter kung saan manggagaling yung mga icocompress
            path_input = input(
                "                               Enter drive letter: ")

            if os.path.isdir(path_input):
                # name of the zip file to be created
                basename = input(
                    "                               Enter name for the archive: ")
                zipfile_name = basename + '.zip'  # name of zip file including its extension

                # output desination
                destination_dir = input(
                    "                               Enter archive destination directory: ")
                destination_dir_list = os.listdir(destination_dir)
                # --------------------------------- PRINT DIR LIST -------
                print("Files and directories in '", destination_dir, "' :")
                # ['docus.docx', 'powerpoint.pptx', 'script.py', 'test.zip']
                print(destination_dir_list)
                # --------------------------------- PRINT DIR LIST -------

                destinationFile = os.path.join(destination_dir, zipfile_name)

                print("                               Saving: " + destinationFile)

                file_name = []

                # kung ilang files yung isasama sa archive
                x = int(input(
                    "\n                               Enter number of files to be compressed: "))
                # filename ng mga files na icocompress kasama file extensions
                print(
                    "                               Enter the files to be compressed in " + path_input)

                for i in range(1, x + 1):  # for loop lang ng pagprint ng File numbers
                    isDone = False
                    while not isDone:
                        fls = input(
                            "                               File %d: " % i)
                        if(fls in destination_dir_list):
                            file_name.append(fls)
                            isDone = True
                        else:
                            print("The filename you entered doesn't exist!")

                loading()  # loading animation
                compressFiles(path_input, zipfile_name, file_name,
                              destinationFile)  # compressing files
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
    else:  # if isdone value is true na, babalik sa main menu
        os.system('cls')
        menu()

# Exception handling prompt for Decompression


def decompDirError():
    user_input = input(
        "                               Would you like to try again? (Yes or No) ")
    # if yes, babalik sa decompression function
    if(user_input == 'Yes' or user_input == 'yes' or user_input == 'Y' or user_input == 'y'):
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
        # show the available drives in computer
        for drive_letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            if os.path.exists(f'{drive_letter}:'):
                print(f'{drive_letter}:'.center(90))
            else:
                pass  # if hindi nageexist yung drive letter, proceed sa pagcheck sa next letter
        # enter the drive kung nasaan ang .zip file na ieextract
        loc = input("                                     Choose Drive: ")
        loc = loc + "\\"

        # changing directory
        os.chdir(loc)
        cwd = os.getcwd()

        # output desination
        zip_dir_path = input("                               Enter archive directory: ")
        zip_dir_path_dir_list = os.listdir(zip_dir_path)
        # --------------------------------- PRINT DIR LIST -------
        print("Files and directories in '", zip_dir_path, "' :")
        # ['docus.docx', 'powerpoint.pptx', 'script.py', 'test.zip']
        print(zip_dir_path_dir_list)
        # --------------------------------- PRINT DIR LIST -------


        # Print the current working directory
        print("Current working directory: {0}".format(zip_dir_path).center(98))

        # Ask user for file to be compressed
        # name = (input(
        #     "\n            Enter the file name you want to decompress(name.zip,test.zip, etc) : "))

        file_name = []

        isDone = False
        while not isDone:
            name = (input(
                "\n            Enter the file name you want to decompress(name.zip,test.zip, etc) : "))
            # fls = input(
            #     "                               Enter the file to be compressed: ")
            if(name in zip_dir_path_dir_list):
                isDone = True
            else:
                print("The filename you entered doesn't exist!")

        print("")
        print("Unzipping the files...".center(98))
        loading()

        # search the drive
        for root, dirs, files in os.walk(zip_dir_path):
            if name in files:
                fileLoc = (os.path.join(root, name))
                print("\n" + fileLoc.center(98))
                os.chdir(os.path.join(root))
                with zipfile.ZipFile(name) as item:
                    print("")
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


menu()
