from msilib import _directories
import zipfile
import os

padding = 59


def multipleCompression():
    padding = 50
    # show available drives
    for drive_letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        if os.path.exists(f'{drive_letter}:'):
            print(f'{drive_letter}:'.center(90))
        else:
            pass

    loc = "D:\\"

    os.chdir(loc)
    cwd = os.getcwd()

    # listing the files that will be compressed
    file_name = ["readmehaiz.md", "testtest.docx", "somefile.py"]
    zName = "test.zip"
    print("")
    print("Zipping the files...".center(padding))
    # loading()

    # crawling in directories
    print(f'TETSTING = cwd : {cwd}')

    with zipfile.ZipFile(zName, 'w') as zipF:
        for root, dirs, files in os.walk(loc):
            for file in files:
                if file in file_name:
                    print("FILE = " + file)
                    print("root = " + root)
                    os.chdir(root)
                    print(os.getcwd())
                    print(os.path.join(root, file).center(98))
                    zipF.write(file, compress_type=zipfile.ZIP_DEFLATED)
    print(os.getcwd())


def make_zipfile(_path):
    if os.path.isdir(_path):
        inName = os.path.join(
            'D:\experiments', os.path.basename(_path) + '.zip')
        #head, tail = os.path.split(os.path.split(_path)[0])
        print("saving: " + inName)

        def zipdir(_path, zip_handle):
            for root, dirs, files in os.walk(_path):
                for file in files:
                    print(os.path.join(root, file))
                    zip_handle.write(os.path.join(root, file), file)
        with zipfile.ZipFile(inName, 'w', compression=zipfile.ZIP_DEFLATED, allowZip64=True) as z:
            zipdir(_path, z)
    print("zip file created")
    return inName


make_zipfile("D:\experiments")
# multipleCompression()
