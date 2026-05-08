import csv


INPUT_FILE = "anime_news.csv"
OUTPUT_FILE = "anime_news.csv"


def add_id_column():
    # TODO:
    # 1. Read all rows from anime_news.csv
    # 2. Check whether an "id" column already exists
    # 3. If not, add an "id" column as the first field
    # 4. Assign IDs starting from 1
    # 5. Write the updated rows back to the same CSV file

    with open(INPUT_FILE, 'r', newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        rows = list(reader)
    
    if not rows:
        return  # Empty file, nothing to do
    
    header = rows[0]
    if 'id' in header:
        print("ID column already exists.")
        return
    
    # Add 'id' as the first column
    header.insert(0, 'id')
    
    # Add IDs to data rows
    for i, row in enumerate(rows[1:], start=1):
        row.insert(0, str(i))
    
    # Write back to the file
    with open(OUTPUT_FILE, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(rows)


if __name__ == "__main__":
    add_id_column()
    print("Finished adding id column to anime_news.csv")
