import read_csv
import json_converter
import search
import json
import pandas as pd

def main():
    csv_file_path = 'data.csv'
    json_file_path = 'data.json'
    
                  # Step 1: Read CSV
    csv_data = read_csv.read_csv("files/google_review_ratings.csv")
    
                  # Step 2: Convert to JSON
    json_data = json_converter.convert_to_json(csv_data)
    
                  # Step 3: Save JSON to file
    json_converter.save_json_to_file(json_data, json_file_path)
    
    # Print JSON data
    # print("JSON Data:\n", json_data)
    
    # uncomment the search_string and search_results once you implement search module
                  # Step 4: Search in JSON
    search_string = input("Enter a string to search in the JSON data: ")
    search_results = search.search_json(json.loads(json_data), search_string)
    
                  # Print search results
    # print("Search Results:\n", json.dumps(search_results, indent=4))
    
    print("\nSearch Results:\n")
    data_frame = pd.DataFrame(columns=search_results[0].keys())
    
    for i in range(len(search_results)):
        data_frame.loc[i] = search_results[i].values()
    
    data_frame = data_frame.set_index('User')
    print(data_frame.to_markdown())

if __name__ == "__main__":
    main()