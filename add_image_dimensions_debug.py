import json
import requests
from PIL import Image
from io import BytesIO

# Path to your items.json file
json_path = r"C:\Users\hughp\OneDrive\Documents\crypto\all projects\riddithomes\riddithomes\items.json"

# Load JSON data
with open(json_path, "r", encoding="utf-8") as f:
    items = json.load(f)

# Function to get dimensions of an image URL
def get_image_dimensions(url):
    try:
        print(f"📷 Fetching image_url: {url}")
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        image = Image.open(BytesIO(response.content))
        dimensions = f"[{image.width} x {image.height}]"
        print(f"✅ Dimensions: {dimensions}")
        return dimensions
    except Exception as e:
        print(f"❌ Failed to fetch {url}: {e}")
        return "[Error]"

# Loop over items and update image_url with dimensions
total = len(items)
success = 0

for item in items:
    url = item.get("image_url")
    if url:
        dims = get_image_dimensions(url)
        item["image_url_dimensions"] = dims
        if dims != "[Error]":
            success += 1

# Save the updated JSON
output_path = json_path.replace("items.json", "items_with_image_url_dimensions.json")
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(items, f, indent=4)

print("\n🎉 Done!")
print(f"✅ Processed {success}/{total} main image URLs.")
print(f"📁 Output saved to: {output_path}")
