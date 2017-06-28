import glob
import os


def last_created_file(folder, extension):
    files = list(filter(os.path.isfile, glob.glob(folder + "/*." + extension)))
    filename = []
    if len(files) > 0:
        if len(files) > 1:
            files.sort(key=lambda x: os.path.getctime(x), reverse=True)
            for file in files:
                if (os.path.getctime(files[0]) - os.path.getctime(file)) <= 10:
                    #print(file + " " + str(os.path.getctime(file)))
                    filename.append(file)
            return filename
        else:
            files.sort(key=lambda x: os.path.getctime(x), reverse=True)
            # print(os.path.getctime(files[0]))
            filename.append(files[0])
            return filename
    else:
        return None


file_name = last_created_file(raw_input('Enter file path '), raw_input('Enter file extension '))
if file_name:
    for file in file_name:
        print(file)
else:
    print("No files in this folder.")
