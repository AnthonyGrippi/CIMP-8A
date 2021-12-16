# Cam use single or double quotes
name = "Kelly"
occupation = 'Teacher'
tenure = 6
location = "Saddleback College"

results = "\"" + name +  "\" is a " + occupation + \
    " at " + location + \
    "\nand has been for over \'" + \
    str(tenure) + "\' Years"

print(results)