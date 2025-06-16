import os
import json
import lzma
import pandas as pd

profiles = ["instagram", "natgeo", "mailchimp", "intel", "slackhq"]
data_list = []

for profile in profiles:
    folder = f"{profile}/"
    print(f"🔹 Checking folder: {profile}/")
    
    if os.path.exists(folder):
        for file in os.listdir(folder):
            if file.endswith(".json.xz"):
                json_file = os.path.join(folder, file[:-3])  # Remove .xz extension
                
                # Extract the file if not already extracted
                if not os.path.exists(json_file):
                    print(f"📂 Extracting: {file}")
                    try:
                        with lzma.open(os.path.join(folder, file), "rt", encoding="utf-8") as f:
                            data = json.load(f)
                        with open(json_file, "w", encoding="utf-8") as f:
                            json.dump(data, f, indent=4)
                    except Exception as e:
                        print(f"⚠️ Error extracting {file}: {e}")
                        continue
                
                # Read extracted JSON
                try:
                    with open(json_file, "r", encoding="utf-8") as f:
                        post = json.load(f)
                        data_list.append({
                            "profile": profile,
                            "likes": post.get("edge_media_preview_like", {}).get("count", 0),
                            "comments": post.get("edge_media_to_comment", {}).get("count", 0),
                            "caption": post.get("edge_media_to_caption", {}).get("edges", [{}])[0].get("node", {}).get("text", ""),
                            "timestamp": post.get("taken_at_timestamp", 0)
                        })
                except Exception as e:
                    print(f"⚠️ Skipping {file} (Invalid JSON): {e}")
                    continue

# Save data to CSV
if data_list:
    df = pd.DataFrame(data_list)
    df.to_csv("instagram_data.csv", index=False)
    print("✅ Data saved to instagram_data.csv")
else:
    print("⚠️ No data extracted! Check JSON files.")
