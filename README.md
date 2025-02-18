# CamScanner Watermark-remover

### Description:
CSMarkRemover.py is a simple Python script for batch-removing the watermark from the app CamScanner on a folder of PDFs.<br/>

### How to use:
1. Install the script by running one of below commands in a terminal depending on your OS:

Windows PowerShell:
```
iwr https://raw.githubusercontent.com/crabfeather/CSMarkRemover/main/CSMarkRemover.py -O CSMarkRemover.py
```
Linux/MacOS:
```
curl https://raw.githubusercontent.com/crabfeather/CSMarkRemover/main/CSMarkRemover.py -o CSMarkRemover.py
```
2. Verify the latest version of Python3 and PIP are installed by running:
```
python --version
pip --version
```
3. Install the required libraries:
```
pip install PyMuPDF
```
6. Run the script with Python for your folder of watermarked PDFs:
```
python CSMarkRemover.py <input-folder>
```
