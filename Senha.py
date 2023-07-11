import subprocess

#getting meta data
meta_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])

#decoding meta data
data=meta_data.decode('utf-8', errors="backslashreplace")

#splitting data by line by line
data=data.split('\n')

#creating a list of profiles
profiles = []

#traverse the data
for i in data:
  
  #find "All User Profile" in each item
  if "All User Profile" in i:
    i = i.split(":")
    i = i[1]
    i = i[1:-1]
    profiles.append(i)
 
#Printing Headign
print("{:<30}| {:<}".format("Wi-Fi Name", "Password"))
print("__")

# traversing the profiles
for i in profiles:
  
  #try catch blocks begin, and try block
  try:
    #getting meta data with password using wifii name
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles',i,'key = clear'])
    
    #decoding and splitting data line by line
    results = results.decode('uft-8', errors = "backslashreplace")
    results = results.split('\n')
    
    #finding password form the result list
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    
    #if there is password it will print the password
    try:
      print("{:<30}| {:<}".format(i, results[0]))
      
    #else it will print blank in front of password  
    except IndexErrors:  
      print("{:<30}| {:<}".format(i, ""))
      
     #called when this process get failed 
except subprocess.CalledProcessErrors:
  print ("Encoding Error Occured")
finally