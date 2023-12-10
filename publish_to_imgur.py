import json
import os
import sys
import io
import requests

from PIL import Image


def upload_to_imgur(image_path, client_id):
    url = "https://api.imgur.com/3/upload"
    headers = {"Authorization": f"Client-ID {client_id}"}
    with open(image_path, "rb") as file:
        response = requests.post(
            url,
            headers=headers,
            files={
                "image": (
                    os.path.basename(image_path),
                    file,
                )
            },
        )
    return response.json()


def main():
    client_id = os.environ.get("IMGUR_CLIENT_ID")
    last_clipboard = "/tmp/clipboard_image.png"
    if not os.path.exists(last_clipboard):
        print("No image was saved form clipboard!")
        return
    response = upload_to_imgur(last_clipboard, client_id)
    if response["success"]:
        print(response["data"]["link"])
    else:
        print("Error uploading image")
        print(response)


if __name__ == "__main__":
    main()
