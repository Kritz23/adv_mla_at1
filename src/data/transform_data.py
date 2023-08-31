import pandas as pd

def convert_height_numeric(height_str):
    
    if isinstance(height_str, int or float): #handling exceptional cases
        height_str = str(height_str)
        
    if pd.isnull(height_str): # handle missing values
        return 0
    
    parts = height_str.split("-")
    
    if len(parts) < 2: #if there is just one part (date/month)
        return 0
    
    date = parts[0].strip()  # Remove leading/trailing spaces
    month = parts[1].strip()   
    
    if month=='' or date =='': # if month/date is empty (was raising keyerror '')
        return 0
    
    month_mapping = {
            'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
            'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12
        }
    
    if month == '00': #when inches is 0
        inches = 0
        feet = month_mapping[date.lower()]
        
    else:
        feet = month_mapping[month.lower()]
        inches = int(date)
    
    total_inches = feet * 12 + inches #calculate height in inches
    return total_inches