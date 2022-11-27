import os
import pyautogui as auto
import time

from PIL import ImageGrab
from docx.shared import Inches
from docx import Document


class FileGenerator:
    def __init__(self) -> None:
        self.document = Document()
        self.extension = ""
        self.fileList = []
        self.outputFileName = ""

    def getExtention(self) -> None:
        self.extension = input("Enter Files Extention: ")

    def generateFileList(self) -> None:
        baseFileName = os.path.basename(__file__)
        self.fileList = [file for file in os.listdir() if file.endswith(
            self.extension) and file != baseFileName]

    def getScreenshot(self) -> None:
        auto.hotkey("winleft", "shiftleft", "s")
        time.sleep(6)
        screenshot = ImageGrab.grabclipboard()
        try:
            screenshot.save("image.png")
        except Exception:
            print("An I/O Error Occoured Please Restart The Process")

    def runCode(self, fileName) -> None:
        os.system(f"start")
        time.sleep(1)
        auto.click()
        auto.write(f"python {fileName}", interval=0.15)
        auto.press("enter")
        self.getScreenshot()
        # time.sleep(2.5)
        auto.write(f"exit")
        auto.press("enter")
        time.sleep(1)

    def getQuestion(self, questionText) -> str:
        for index, char in enumerate(questionText.lower()):
            if 97 <= ord(char) <= 122:
                return questionText[index:]

    def generate(self) -> None:
        for _ in self.fileList:
            with open(_, "r") as file:
                question = self.getQuestion(file.readline())
                code = file.read()
                self.runCode(file.name)
                time.sleep(1)
                self.document.add_heading(str(question))
                self.document.add_paragraph(code)
                self.document.add_picture(
                    "image.png", width=Inches(5.23), height=Inches(2.3))

    def main(self) -> None:
        self.getExtention()
        self.generateFileList()
        try:
            self.generate()
        except Exception:
            print("An I/O Error Occoured Please Restart The Process")
        time.sleep(1)
        self.outputFileName = input("Enter Output File Name: ")
        self.outputFileName += ".docx"
        self.document.save(self.outputFileName)


def main() -> None:
    object = FileGenerator()
    object.main()


if __name__ == "__main__":
    main()
