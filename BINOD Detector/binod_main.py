import os

def findBinod(filename):
    """"Detects Binod Hidden in files"""
    with open(filename, "r") as f:
        fileContent = f.read()
    # Finds binod by converting string to lowercase
    if "binod" in fileContent.lower():
        return True
    else:
        return False

if __name__ == '__main__':
    # Listing folder content
    contents = os.listdir()
    nBinod=0
    for item in contents:
        if item.endswith('txt'):
            print(f"Detecting Binod in {item}")
            flag = findBinod(item)
            if(flag):
                print(f"!!!!!Binod found in {item}!!!!!")
                nBinod += 1
            else:
                print(f"Binod not found in {item}")
    print("******Binod Detector Summary******")
    print(f"{nBinod} files found with Binod hidden")
