def remove_capitals(text):
    return ''.join(c for c in text if not c.isupper())

# Examples
print(remove_capitals("fOrEver"))  
print(remove_capitals("raiNCoat"))  
print(remove_capitals("cElLAr Door")) 
