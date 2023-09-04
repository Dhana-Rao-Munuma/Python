import pytesseract
from PIL import Image
import csv

def read_text_from_jpg(jpg_file):
    # Open the JPG image
    img = Image.open(jpg_file)

    # Perform OCR on the image to extract text
    extracted_text = pytesseract.image_to_string(img)

    return extracted_text

def write_text_to_csv(text, csv_file):
    # Split the extracted text into lines
    lines = text.split('\n')

    # Write the text to a CSV file
    with open(csv_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for line in lines:
            # Write each line of text as a separate row in the CSV file
            writer.writerow([line])

if __name__ == "__main__":
    # Replace 'input.jpg' with the path to your JPG file
    input_jpg_file = 'C:\Dhana\OneDrive - Conduent\Reading Materials\python\my_code\user_emails.jpg'
    # Replace 'output.csv' with the desired output CSV file path
    output_csv_file = 'output.csv'

    # Read text from the JPG file
    extracted_text = read_text_from_jpg(input_jpg_file)

    # Write extracted text to CSV file
    write_text_to_csv(extracted_text, output_csv_file)

    print("Data has been successfully read from the JPG file") 
    #and written to the CSV file.")
