# This file simulates an external storage package.
# The API layer should call these functions instead of directly reading and writing the CSV inside route functions.

import csv

CSV_FILE = "anime_news.csv"

def read_all_rows():
    # You may directly use this helper.
    with open(CSV_FILE, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    normalized_rows = []
    for row in rows:
        normalized_rows.append({
            "id": int(row["id"]),
            "title": row["title"],
            "link": row["link"],
            "image_url": row["image_url"],
        })
    return normalized_rows

def write_all_rows(rows):
    # You may directly use this helper.
    with open(CSV_FILE, mode="w", newline="", encoding="utf-8") as file:
        fieldnames = ["id", "title", "link", "image_url"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

def get_all_news():
    return read_all_rows()

def get_news_by_id(news_id: int):
    rows = read_all_rows()
    for row in rows:
        if row["id"] == news_id:
            return row
    return None


def create_news(news_data: dict):
    rows = read_all_rows()
    if not rows:
        next_id = 1
    else:
        next_id = max(row["id"] for row in rows) + 1
    new_row = {
        "id": next_id,
        "title": news_data["title"],
        "link": news_data["link"],
        "image_url": news_data["image_url"],  
    }
    rows.append(new_row)
    write_all_rows(rows)
    return new_row                    

def update_news(news_id: int, news_data: dict):
    rows = read_all_rows()
    for i, row in enumerate(rows):
        if row["id"] == news_id:
            rows[i] = {
                "id": news_id,
                "title": news_data["title"],
                "link": news_data["link"],
                "image_url": news_data["image_url"],  
            }
            write_all_rows(rows)
            return rows[i]
    return None


def delete_news(news_id: int):
    rows = read_all_rows()
    for i, row in enumerate(rows):
        if row["id"] == news_id:
            del rows[i]
            write_all_rows(rows)
            return True
    return False    