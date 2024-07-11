import os 
 # This function is for create the file        

def create_file(filename):
    try:
        with open(filename, 'x') as f :# With is  used for automatically close the file only
            print(f" File name {filename} : ceated sucessfully")
    except FileExistsError:
        print(f"{filename} : is already exist")        
    except Exception as E:
        print("An error accured!")    

def view_all_files(): 
    files =os.listdir() # this will return all the files and directories in the current directory.
    if not files:
        print('No files found !')
    else :
        print("files in directory !") 
        for file in files: 
            print(file) 


# This  function will be called if  user want to delete files.

def delete_file(filename):
    try:
        os.remove(filename)
        print(f"{filename} has been deeleted sucessfully!")

    except FileNotFoundError:
        print("File not found")

    except Exception as E:
        print(f"An error occured!")


# This function is for read the file        

def read_file(filename):
    try:
        with open('sample.txt','r') as f:
            content = f.read()
            print(f"content of '{filename}' :\n{content}")

    except FileNotFoundError:
        print("file name does not exist!")

    except Exception as E:
        print("An error occured!")    

# This function is for edit the file   

def edit_file(filename):
    try:
        with open('sample.txt','a') as f:    # "a" means append mode
            content =  input("Enter the data to add")
            f.write(content + "\n") 
            print("content added to {filename} sucessfully!")  

    except FileExistsError:  
        print("File not found !") 
    except FileExistsError:
        print("The file yu want to update does not exist!")        
            
    except Exception as E:
        print("An error occured!")        


def main():
    while True:
        print('File managemnt app')
        print('1 : to create file')
        print('2 : to view all file')
        print('3 : to delete file')
        print('4 : to read file')
        print('5 : to edit file')
        print('6 : Exit')

        choice = int(input ("Enter your choice between (1-6) : "))

        if choice == 1:
            filename  = input("Enter the file name to create :")
            create_file(filename)

        elif choice == 2 :
            view_all_files()

        elif choice == 3:
            filename = input("Enter the file name you want to delete: ")    
            delete_file(filename)

        elif choice == 4 :
            filename = input("Enter the file name you want to read : ")
            read_file(filename)

        elif choice == 5 :
            filename = input("Enter the file name you want to edit  : ")
            edit_file(filename)

        elif choice == 6 :
            print("closig the app....")
            break

        else:
            print("Wrong input")          


if __name__ == "__main__":
    main()





