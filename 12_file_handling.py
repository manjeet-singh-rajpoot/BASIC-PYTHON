                #created a file #
import os               
f=open("C:\\Users\\manje\\OneDrive\\Desktop\\arjun singh - Copy\\raj.txt","x")
print("file created succesfully.....");

              #write a data  in file raj.txt#

f=open("C:\\Users\\manje\\OneDrive\\Desktop\\arjun singh - Copy\\raj.txt","w")
f.write("hii manjeet kya haal hai i hope ")
f.write("\nyou are very happy")
f.write("\ni want to give notice that you are succesfully hired in my company")
f.write("\nso please give your personl detailed..")
f.write("\nthank you...")
print("data wrote succesfully.....");

              #read from a file #

f=open("C:\\Users\\manje\\OneDrive\\Desktop\\arjun singh - Copy\\raj.txt","r")
print(f.read(200));

             
             # we start exception handling in file #
try:
    f=open("C:\\Users\\manje\\OneDrive\\Desktop\\arjun singh - Copy\\maj.txt","r")
    print(f.read(200));
except: 
    print("sorry...plz creat a new file")
else:
    f.close()
    print("file closed...") 
    
    
       # copy data of ones file data to another file #

 
try:
   with open("C:\\Users\\manje\\OneDrive\\Desktop\\arjun singh - Copy\\raj.txt") as f2:
       with open("C:\\Users\\manje\\OneDrive\\Desktop\\arjun singh - Copy\\maj.txt","w") as f3:
          for i in f2:
              f3.write(i)
   
except: 
    print("sorry...plz creat a new file")
else:
    f2.close()
    print("file closed...") 

         # delete a file #
if os.path.exists("C:\\Users\\manje\\OneDrive\\Desktop\\arjun singh - Copy\\raj.txt"):
        os.remove("C:\\Users\\manje\\OneDrive\\Desktop\\arjun singh - Copy\\raj.txt")
else:
    print("file does not exists....")
    

print("file deleted sucesfully....")