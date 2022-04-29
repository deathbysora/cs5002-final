"""App to unzip data."""
import os
from zipfile import ZipFile


def main():
    """Entry point."""
    path = r"C:\Users\pmtqe\Downloads\Washington"
    for zipped_folder_name in os.listdir(path):
        source = path + "\\" + zipped_folder_name
        with ZipFile(source, "r") as zip_folder:
            info = zip_folder.infolist()
            file_name = zipped_folder_name.replace(".zip", ".csv")
            info[0].filename = file_name

            destination = os.getcwd() + "\\source"
            zip_folder.extract(info[0], destination)

        print(f"Unzipped {zipped_folder_name} to {file_name}")


if __name__ == "__main__":
    main()
