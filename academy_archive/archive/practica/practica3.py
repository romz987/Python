products = {
    "HDD_Toshiba": 2000,    
    "SSD_Samsung": 8000,    
    "CPU_AMD_Rysen_7": 20000,    
    "CPU_AMD_Rysen_5": 13000
}


for key, value in products.items():
    products[key] = round(value * 1.10, 2) 


print(products)
