import json
import os

# Build the JSON path WITHOUT needing to know username
json_path = os.path.join(
    os.environ["USERPROFILE"],
    "Desktop",
    "Wifi Login Setup",
    "Extra Data",
    "credentials.json"
)

print("CREDENTIAL UPDATE")

new_username = input("What is your new username?: ")
new_password = input("What is your new password?: ")

# Load existing JSON
with open(json_path, "r") as f:
    data = json.load(f)

# Update fields
data["username"] = new_username
data["password"] = new_password

# Save JSON back
with open(json_path, "w") as f:
    json.dump(data, f, indent=4)

print("\nCredentials updated successfully!")
print(f"Updated file: {json_path}")
