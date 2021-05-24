
def load_puzzle(filename):
    
    name_file = [] 
    with open(filename, "r") as f:
        for line in f:
            name_file.append( [str(val) for val in line.strip().split(",")] )
    return name_file

def main():
    found_name = "Matei" #add the found name
    filename = input("Please enter in your  file:")
    names = load_puzzle(filename)
    print(names)
    i = 0
    for name in names: 
        print(name[0])
        if name[0] == found_name:
            print(name[0] + 'found')
            names[i][0] = name[0] + " present"
        i = i + 1
        print(names)
    fileOut = open(filename, "w")                        
    for name in names:
        fileOut.write(name[0] + "\n")
    fileOut.close()

# Guard for main function - do NOT remove or change 
if __name__ == "__main__":
    main()


