import PyPDF2
import os

def split_pdf_into_pages(pdf_path, output_folder):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    with open(pdf_path, 'rb') as infile:
        reader = PyPDF2.PdfReader(infile)
        # 
        for i in range(len(reader.pages)):
            writer = PyPDF2.PdfWriter()
            writer.add_page(reader.pages[i])

            # text = ''
            # if i % 10 == 0:
            #     page = reader.pages[i]
            #     text += page.extract_text()
            #     # if "Cluster" in text:
            #     #     print(f"Text after 'Cluster' on page{i+1}: {text.split('Cluster')[1]}")
            #     for i in text:
            #         print(i)
            
            output_filename = os.path.join(output_folder, f"page_{i+1}.pdf")
            with open(output_filename, 'wb') as outfile:
                writer.write(outfile)
            print(f"Saved: {output_filename}")

if __name__ == "__main__":
    pdf_path = r"C:\Users\TEACHER\Downloads\staar.pdf"  # Update this path
    output_folder = r"C:\Users\TEACHER\Downloads\StaarQuestions"  # Update this path
    split_pdf_into_pages(pdf_path, output_folder)
