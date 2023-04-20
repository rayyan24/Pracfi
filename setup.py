import os
print("Please Wait Installing Dependencies")
def install(package):
    os.system(f'pip install {package}')
try:
    import pyautogui
except Exception:
    install("pyautogui")
try:
    import PIL
except Exception:
    install("Pillow")
try:
    import docx
except Exception:
    install("python-docx")
try:
    import docx2pdf
except Exception:
    install("docx2pdf")
