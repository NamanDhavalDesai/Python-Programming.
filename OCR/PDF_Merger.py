from PyPDF2 import PdfMerger

#Create an instance of PdfFileMerger() class
merger = PdfMerger()

#Create a list with the file paths
pdf_files = ['1.pdf', '2.pdf','3.pdf','4.pdf','5.pdf', '6.pdf','7.pdf','8.pdf','9.pdf']

#Iterate over the list of the file paths
for pdf_file in pdf_files:
    #Append PDF files
    merger.append(pdf_file)

#Write out the merged PDF file
merger.write("Ground-Floor-Services_Final-Submission.pdf")
merger.close()