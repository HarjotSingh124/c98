from fileinput import filename


def swapFileData():
    filename1 = input("Enter  The firstFile Name:- ")
    filename2 = input("Enter  The secondFile Name:- ")

    with open(filename1, 'r') as fileobject1:
        dataoffileobject1 = fileobject1.read()

    with open(filename2, 'r') as fileobject2:
        dataoffileobject2 = fileobject2.read()

    with open(filename1, 'w') as fileobject1:
        fileobject1.write(dataoffileobject2)

    with open(filename2, 'w') as fileobject2:
        fileobject2.write(dataoffileobject1)

swapFileData()

        
if not os.path.exists(req_path):
  print("Please provide a valid path")
  sys.exit(1)
if os.path.isfile(req_path):
  print("Please Provide a Directory path")  
  sys.exit(2)
