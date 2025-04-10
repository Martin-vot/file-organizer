import os
import shutil
import logging

# Function to organize files
def organize_files(directory):
    # Check if the directory exists
    if not os.path.isdir(directory):
        print(f"Error: The directory {directory} does not exist.")
        return

    # List of file types we want to organize
    file_types = {
        'images': ['.jpg', '.jpeg', '.png', '.gif'],
        'documents': ['.txt', '.pdf', '.docx'],
        'audio': ['.mp3', '.wav'],
        'videos': ['.mp4', '.mov']
    }

    # Set up logging
    logging.basicConfig(filename="file_organizer.log", level=logging.INFO, format='%(asctime)s - %(message)s')
    logging.info("File organization started.")
    
    # Iterate through files in the given directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue
        
        # Get the file extension
        _, file_extension = os.path.splitext(filename)

        # Determine the file type based on the extension
        for folder, extensions in file_types.items():
            if file_extension.lower() in extensions:
                # If the folder doesn't exist, create it
                folder_path = os.path.join(directory, folder)
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
                
                # Handle duplicate file names by renaming the file
                new_file_path = os.path.join(folder_path, filename)
                if os.path.exists(new_file_path):
                    base, ext = os.path.splitext(filename)
                    counter = 1
                    while os.path.exists(new_file_path):
                        new_file_path = os.path.join(folder_path, f"{base}_{counter}{ext}")
                        counter += 1
                    filename = os.path.basename(new_file_path)  # Update filename with new name

                try:
                    # Move the file to the appropriate folder
                    shutil.move(file_path, new_file_path)
                    logging.info(f"Moved: {filename} to {folder}")
                    print(f"Moved: {filename} to {folder}")
                except PermissionError:
                    logging.error(f"Permission denied while moving file: {filename}")
                    print(f"Permission denied while moving file: {filename}")
                except Exception as e:
                    logging.error(f"Error moving file {filename}: {str(e)}")
                    print(f"Error moving file {filename}: {str(e)}")
                break

if __name__ == '__main__':
    directory = 'path_to_your_directory'  # Replace with the actual path
    organize_files(directory)
