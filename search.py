import re
from fuzzywuzzy import fuzz

def search_json(json_data, search_string):
    results = []
    # Place your search code here
    # you will have to loop through the json_data file you created earlier
    # finally you can store the match in the result list and return it
    
    keywords = search_string.split()
    
    for item in json_data:
        temp = {}
        for key, value in item.items():
            if key == "User":
                temp[key] = value
            for keyword in keywords:
                if re.search(keyword, key, re.IGNORECASE) or re.search(keyword, str(value), re.IGNORECASE):
                    temp[key] = value
                elif fuzz.partial_ratio(keyword.lower(), key.lower()) > 80 or fuzz.partial_ratio(keyword.lower(), str(value).lower()) > 80:
                    temp[key] = value
        results.append(temp)
    
    return results