# Simple Python script for batch-removing the watermark from the app CamScanner on a folder of PDFs -- created by Allan Edh @crabfeather
# Requirements: 'pip install PyMuPDF'

import fitz
import os
import sys

# Crop function
def crop_pdf(input_folder, crop_left, crop_right, crop_top, crop_bottom):
    output_folder = os.path.join(os.path.dirname(input_folder), os.path.basename(input_folder) + '_NoMark')
    
    # Create output folder
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Iterate through files
    for filename in os.listdir(input_folder):
        if filename.endswith('.pdf'):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            
            doc = fitz.open(input_path)
            for page in doc:
                rect = page.rect
                
                # Is the page horisontal
                is_horizontal = rect.width > rect.height
                
                if is_horizontal:
                    # If horisontal crop only bottom
                    new_rect = fitz.Rect(
                        rect.x0,
                        rect.y0,
                        rect.x1,
                        rect.y1 - crop_bottom
                    )
                else:
                    # If vertical crop sides too
                    new_rect = fitz.Rect(
                        rect.x0 + crop_left,
                        rect.y0 + crop_top,
                        rect.x1 - crop_right,
                        rect.y1 - crop_bottom
                    )
                
                page.set_cropbox(new_rect)
            
            # Save output
            doc.save(output_path)
            doc.close()

# Main
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python CSMarkRemover.py <input-folder>")
        sys.exit(1)
    
    input_folder = sys.argv[1]

    # EDIT CROP VALUES IF NEEDED:
    crop_left = 25  
    crop_right = 25  
    crop_top = 0  
    crop_bottom = 50

    crop_pdf(input_folder, crop_left, crop_right, crop_top, crop_bottom)
