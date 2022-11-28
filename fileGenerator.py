import os
import pyautogui as auto
from PIL import ImageGrab
import time
from docx.shared import Inches
from docx import Document


class FileGenerator:
    def __init__(self) -> None:
        self.document = Document()
        self.extension = ""
        self.fileList = []
        self.outputFileName = ""
        self.Map={"py":self.runPythonCode,"cpp":self.runCppCode,"java":self.runJavaCode}


    def getExtention(self) -> None:
        self.extension = input("Enter Files Extention: ")        

    def generateFileList(self) -> None:
        res=True
        baseFileName = os.path.basename(__file__)
        self.fileList = [file for file in os.listdir() if file.endswith(
            self.extension) and file != baseFileName]
        if self.extension not in self.Map:
            print(f"{self.extension} is not supported")
            res=False
        if len(self.fileList)==0:
            print(f"{self.extension} files not found")
            res=False
        return res

    def getScreenshot(self) -> None:
        auto.hotkey("winleft", "shiftleft", "s")
        time.sleep(6)
        screenshot = ImageGrab.grabclipboard()
        try:
            screenshot.save("image.png")
        except Exception:
            print("An I/O Error Occoured Please Restart The Process")

    def runPythonCode(self, fileName) -> None:
        os.system(f"start")
        time.sleep(1)
        auto.click()
        auto.write(f"python {fileName}", interval=0.15)
        auto.press("enter")
        self.getScreenshot()
        auto.write(f"exit")
        auto.press("enter")
    def runCppCode(self,fileName) -> None:
        os.system(f"start")
        time.sleep(1)
        auto.click()
        auto.write(f"g++ {fileName} -o {fileName}.exe", interval=0.04)
        auto.press("enter")
        auto.write(f"{fileName}.exe", interval=0.04)
        auto.press("enter")
        time.sleep(0.5)
        self.getScreenshot()
        auto.write(f"exit")
        auto.press("enter")

    def runCode(self) -> None:
        pass
    def runJavaCode(self,fileName) -> None:
        print("JAVA CODE")
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

        
    def start(self) -> None:
        self.getExtention()
        if not self.generateFileList():
            return
        self.runCode=self.Map[self.extension]
        try:
            self.generate()
        except Exception:
            print("An I/O Error Occoured Please Restart The Process")
        time.sleep(1)
        os.remove("image.png")
        self.outputFileName = input("Enter Output File Name: ")
        self.outputFileName += ".docx"
        self.document.save(self.outputFileName)


def main() -> None:
    object = FileGenerator()
    object.start()


if __name__ == "__main__":
    main()
