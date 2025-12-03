from fpdf import FPDF
# to create a header, we have to inherit from the fpdf class and add some things to override the header method
# so, create our own class
class PDF(FPDF):
    def header(self):
        self.image("logo.png",10,8,33)
        self.set_font("helvetica","B",16)
        # create a cell to add some text to
        # a cell is a rectangular text box that can have background color, border, etc these are the parameters that you must pass
        # there will be an empty cell between the image and the header
        self.cell(80)
        self.cell(40,10,"Hello World",align="C")
        # add a line break 
        self.ln(40)
    # do the same for the footer
    def footer(self):
        self.set_y(-15)
        self.set_font("helvetica","I",16)
        # setting the width to 0 tells the cell to get the maximum available width
        self.cell(0,10,f"Page {self.page_no()}/{{nb}}",align="C")

        
# press Ctrl (command on Mac) and click on the package to view the code for the package
pdf = FPDF()
pdf.add_page()
pdf.set_font("helvetica","B",16)
# create a for loop which displays 40 lines on the pdf
for i in range(1,41):
    # setting the width to 0 tells the cell to get the maximum available width
    pdf.cell(0,10,f"Printing line number {i}",new_x="LMARGIN",new_y="NEXT")

# this is our output pdf
pdf.output("sample.pdf")