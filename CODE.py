from msilib import _directories
import zipfile
import time
import sys
import os

padding = 59;

def more():
    ans = input("\n                       Do you want to do another activity? <Yes or No>? ")
    cls = lambda: os.system('cls')
    
    if ans == 'Yes' or ans == 'yes':
        cls()
        menu()

    elif ans == 'No' or ans == 'no':
        exit(2)
    else:
        print("invalid answer".center(98))
        more()
    

# shows the zipping animation 
def loading():
    animation = ["[■□□□□□□□□□]".center(98),"[■■□□□□□□□□]".center(98), "[■■■□□□□□□□]".center(98), "[■■■■□□□□□□]".center(98), "[■■■■■□□□□□]".center(98), "[■■■■■■□□□□]".center(98), "[■■■■■■■□□□]".center(98), "[■■■■■■■■□□]".center(98), "[■■■■■■■■■□]".center(98), "[■■■■■■■■■■]".center(98)]
    for i in range(len(animation)):
        time.sleep(0.2)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()

def compression():
    cls = lambda: os.system('cls')
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
    print("                        Current working directory: {0}".format(cwd))

    # ask user for file to be compressed
    name = (input("\n             Enter the file name you want to compress (name.txt, name.html, etc) : "))
    zippedfilename = input("                       Rename the zip folder: ")
    print ("Zipping the files...".center(98))
    #loading()
    # search the drive 
    for root, dirs, files in os.walk(loc):
        if name in files:
            fileLoc = (os.path.join(root, name))
            print("\n" + fileLoc.center(98))
            os.chdir(os.path.join(root))            
            zip_file = zipfile.ZipFile (zippedfilename + ".zip", 'w')
            zip_file.write(name, compress_type=zipfile.ZIP_DEFLATED)
            print("")
            print("Zip Completed!".center(98))
            more()
            zip_file.close()
            
# multi compression 
def multipleCompression():
    #show available drives
    for drive_letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        if os.path.exists(f'{drive_letter}:'):
            print(f'{drive_letter}:'.center(90))
        else:
            pass
    loc = input("                                     Choose Drive: ")
    loc = loc + "\\"
    
    os.chdir(loc)
    cwd = os.getcwd()
    
    # listing the files that will be compressed 
    file_name = []
    x = int(input("\n                         Enter number of files to be compressed: "))
    print("                         Enter Files To Be compressed in " + loc + " ")
    for i in range(1, x + 1):
            fls = input("                             File %d: " %i)
            file_name.append(fls)
    print("                         Files to be compressed : %s" %file_name)
    
    zName = input("\n                                   Enter New Zip Name : ")
    print("")
    print ("Zipping the files...".center(98))
    #loading()
    
    # crawling in directories
    print(f'TETSTING = cwd : {cwd}')
    
    # ito yung working na original
    handle = zipfile.ZipFile(zName+".zip", 'w')
    for root, dirs, files in os.walk(loc): # ginawa kong dirs instead of directories
         for file_name in file_name:
             if file_name in files:
                 cwd = os.chdir(os.path.join(root))
                 print(cwd)
                 print(os.path.join(root,file_name).center(98))
                 handle.write(file_name,compress_type=zipfile.ZIP_DEFLATED)
                 handle.close

    more()
    '''
    # testingan
    
    handle = zipfile.ZipFile(zName+".zip", 'w')
    for root, dirs, files in os.walk(loc): # ginawa kong dirs instead of directories
        for file_name2 in file_name:
            if file_name2 in files:
                handle = zipfile.ZipFile(zName+".zip", 'w')
                os.chdir(os.path.join(root))
                print(os.path.join(root,file_name2).center(98))
                handle.write(file_name2,compress_type=zipfile.ZIP_DEFLATED)
                handle.close

    more()
    '''
        

# data decompression   
def decompression():
    cls = lambda: os.system('cls')
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
    print("                        Current working directory: {0}".format(cwd))
     
    # Ask user for file to be compressed
    name = (input("\n            Enter the file name you want to decompress(name.zip,test.zip, etc) : "))
    print ("")
    print ("  Unzipping the files...".center(98))
    #loading()
    
    # search the drive 
    for root, dirs, files in os.walk(loc):
        if name in files:
            fileLoc = (os.path.join(root, name))
            print("\n" + fileLoc.center(98))
            os.chdir(os.path.join(root))            
            with zipfile.ZipFile(name) as item:
                print("")
                print ("Unzip completed!".center(98))
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
    
    for i in range (len(menuPrint)):
        print ("{} {}".format([i+1], menuPrint[i]).center(98))
        
    choice = int(input("\n                                     Enter your choice: "))
    while choice !=0:
        if choice==1:
            compression()
            break
        elif choice==2:
            multipleCompression()
            break
        elif choice==3:
            decompression()
            break
        elif choice==4:
            exit()
        else:
            print("invalid choice".center(98))

# calling the functions 
#####################################################################################

menu()



    