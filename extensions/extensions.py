extensions = {
             ".gif": "image/gif",
             ".jpg": "image/jpeg",
             ".jpeg": "image/jpeg",
             ".png": "image/png",
             ".pdf": "application/pdf",
             ".txt": "text/plain",
             ".zip": "application/zip"
             }


def main():
    file_name = input("File name (*.*)?: ").lower().strip()
    file_extension = "." + file_name.split('.', 2)[-1]
    if file_extension in extensions:
        print(extensions[file_extension])
    else:
        print("application/octet-stream")


main()
