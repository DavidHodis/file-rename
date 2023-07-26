import os

print("Enter File Extension:")
ext = input()
print("Enter Folder in Directory:")
fld = input()

# Function re-name multiple files
def main():
   
    folder = fld
    extension = ext
    for count, filename in enumerate(os.listdir(folder)):
        dst = f"{str(count)}.{extension}"
        src =f"{folder}/{filename}"  
        dst =f"{folder}/{dst}"
         
                os.rename(src, dst)
 
if __name__ == '__main__':
     
    # Calling the main() function
    main()
