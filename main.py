from drive_auth import authenticate_drive
from drive_operations import list_files, upload_file, delete_file
import openai
openai.api_key = "YOUR_OPENAI_KEY"

def main():
    service = authenticate_drive()
    print("Google Drive connected!")

    while True:
        command = input("Enter command (list/upload/delete/exit): ").strip().lower()
        
        if command == "list":
            files = list_files(service)
            for f in files:
                print(f"{f['name']} ({f['id']})")
        elif command == "upload":
            file_name = input("Enter file name to upload: ")
            file_id = upload_file(service, file_name)
            print(f"Uploaded file with ID: {file_id}")
        elif command == "delete":
            file_id = input("Enter file ID to delete: ")
            delete_file(service, file_id)
            print("File deleted successfully")
        elif command == "exit":
            break
        else:
            print("Unknown command!")

def summarize_file(file_content):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": f"Summarize this:\n{file_content}"}]
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    main()
