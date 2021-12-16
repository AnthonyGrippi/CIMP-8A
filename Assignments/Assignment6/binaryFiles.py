import pickle

OS = [["Mac OS", "10.6"], ["Windows", "10"], ["Android", "7"]]

# open a binary file for wtrite 
with open("A:\\Python Projects\\Assignments\\Temp\\os.txt", "wb") as file:
    pickle.dump(OS, file)

with open("A:\\Python Projects\\Assignments\\Temp\\os.txt", "rb") as file:
    os = pickle.load(file)
    print(os)