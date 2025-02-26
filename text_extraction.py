
from pdfplumber import open

def text_extraction(uploaded_file):
    report = ""
    with open(uploaded_file) as pdf:
        for i in range(len(pdf.pages)):

            page = pdf.pages[i]
            box = (0,210,page.width,700)
            crop = page.crop(box)
            for i in crop.extract_text().split("/n"):
                report += i
            report += "\n\n\n"

    return report

if __name__ == "__main__":
    text_extraction("sample.pdf")