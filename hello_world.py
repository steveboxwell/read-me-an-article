import argparse
import PyPDF2
import pyttsx3

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
    prog='Read Me an Article',
    description='Reads you a article',
    )
    parser.add_argument("i",
                        help="file to read")
    parser.add_argument("o",
                        help="output filename")
    args = parser.parse_args()
    # creating a pdf file object
    with open(args.i, "rb") as infile:
        pdf_reader = PyPDF2.PdfFileReader(infile)
        print(f"There are {pdf_reader.numPages} pages")
        for page in pdf_reader.pages:
            text = page.extractText()

            engine = pyttsx3.init()
            engine.say("I will speak this text")
            engine.runAndWait()