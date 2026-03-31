import json 
from webdav3.client import Client
import os

CONFIG = "scripts/config.json"
# Client cofiguration settings 
def get_client():
    if os.path.exists(CONFIG):
        with open(CONFIG, "r") as file:
            user_config = json.load(file)

    else: 
        print("Configure your Tip Cloud\n")
        user_config = {
            "webdav_hostname": input("URL "),
            "webdav_login": input("\nLogin "),
            "webdav_password": input("\nPassword ")
        }

        # Save config file 
        choice = input("Do you want to save it? (y/n): ")
        if choice.lower() != "n":
            with open(CONFIG, "w") as file:
                json.dump(user_config, file, indent = 4)
            print(f"Saved {CONFIG}")

    return Client(user_config)

# Configure connection with host server
def sync_clipboard(data):
    # Sending clipboard to Nextcloud services
    client = get_client()
    local_clipboard = "clipboard.txt"
    with open(local_clipboard, "w", encoding = "utf-8") as file:
        file.write(data)

    # Sending 
    try: 
        client.upload_sync(remote_path = "remote_clipboard.txt", local_path = local_clipboard)
        print("Succesfully sent!\n")
    except Exception as e:
        print(f"Error {e}") 
    finally: 
        if os.path.exists(local_clipboard):
            os.remove(local_clipboard)

def get_remote_clipboard():
    client = get_client()
    try:
        client.download_sync(remote_path = "remote_clipboard.txt", local_path = "temp_clipboard.txt")
        with open("temp_clipboard.txt", "r", encoding = "utf-8" ) as file:
            clipboard_data = file.read()
        os.remove("temp_clipboard.txt")
        return clipboard_data
    except Exception:
        return None

# Test
if __name__ == "__main__":
    sync_clipboard("NNNN")
    print(f"Data from cloud: {get_remote_clipboard()}")




