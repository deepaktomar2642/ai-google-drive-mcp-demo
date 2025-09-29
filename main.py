from drive_auth import authenticate_drive
from drive_operations import list_files, upload_file, delete_file, download_file
from openai_ops import summarize_text, generate_file, rewrite_text

def main():
    service = authenticate_drive()
    print("Google Drive connected!")

    while True:
        command = input("\nEnter command (list/upload/delete/download/summarize/generate/rewrite/exit): ").strip().lower()

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

        elif command == "download":
            file_id = input("Enter file ID to download: ")
            content = download_file(service, file_id)
            print("\n=== File Content ===\n", content)

        elif command == "summarize":
            file_id = input("Enter file ID to summarize: ")
            content = download_file(service, file_id)
            summary = summarize_text(content)
            print("\n=== Summary ===\n", summary)

        elif command == "generate":
            prompt = input("Enter prompt to generate file content: ")
            content = generate_file(prompt)
            file_name = input("Enter name for the new file: ")
            with open(file_name, "w") as f:
                f.write(content)
            upload_file(service, file_name)
            print(f"Generated and uploaded file: {file_name}")

        elif command == "rewrite":
            file_id = input("Enter file ID to rewrite: ")
            instruction = input("Enter rewrite instruction (e.g., simplify, make professional): ")
            content = download_file(service, file_id)
            new_content = rewrite_text(content, instruction)
            file_name = input("Enter name for rewritten file: ")
            with open(file_name, "w") as f:
                f.write(new_content)
            upload_file(service, file_name)
            print(f"Rewritten file uploaded as: {file_name}")

        elif command == "exit":
            print("Exiting...")
            break

        else:
            print("Unknown command!")

if __name__ == "__main__":
    main()
