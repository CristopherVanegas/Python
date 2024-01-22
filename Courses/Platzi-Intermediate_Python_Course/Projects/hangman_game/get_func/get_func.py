#!/usr/bin/python3 

dict = {
    'Name': 'Zara',
    'Age': 27, 
    # 'Sex': 'Female'
}

print ("Value : %s" %  dict.get('Age'))
print ("Value : %s" %  dict.get('Sex', "NA"))
