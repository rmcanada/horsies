# from io import StringIO
# from PyPDF2 import PdfFileReader

# # Open the PDF file
# with open('https://www.equibase.com/static/chart/pdf/AQU120422USA1.pdf', 'rb') as f:
#     # Read the file
#     reader = PdfFileReader(f)
#     # Extract the text from the PDF
#     text = reader.getPage(0).extractText()

# # Print the extracted text
# print(text)


# import io
# from urllib.request import Request, urlopen

# from PyPDF2 import PdfFileReader


# class GetPdfFromUrlMixin:
#     def get_pdf_from_url(self, url):
#         """
#         :param url: url to get pdf file
#         :return: PdfFileReader object
#         """
#         remote_file = urlopen(Request(url)).read()
#         memory_file = io.BytesIO(remote_file)
#         pdf_file = PdfFileReader(memory_file)
#         return pdf_file


# https://www.equibase.com/premium/chartEmb.cfm?track=AQU&raceDate=12/04/2022&cy=USA&rn=1


import requests
from bs4 import BeautifulSoup
import io
from PyPDF2 import PdfFileReader
 
 
url = "https://www.equibase.com/premium/chartEmb.cfm?track=AQU&raceDate=12/04/2022&cy=USA&rn=1"
read = requests.get(url)
html_content = read.content
soup = BeautifulSoup(html_content, "html.parser")
 
list_of_pdf = set()
l = soup.find('p')
print(l)
p = l.find_all('a')
 
for link in (p):
    pdf_link = (link.get('href')[:-5]) + ".pdf"
    print(pdf_link)
    list_of_pdf.add(pdf_link)
 
def info(pdf_path):
    response = requests.get(pdf_path)
     
    with io.BytesIO(response.content) as f:
        pdf = PdfFileReader(f)
        information = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()
 
    txt = f"""
    Information about {pdf_path}:
 
    Author: {information.author}
    Creator: {information.creator}
    Producer: {information.producer}
    Subject: {information.subject}
    Title: {information.title}
    Number of pages: {number_of_pages}
    """
    print(txt)
    return information
 
 
for i in list_of_pdf:
    info(i)

