from fpdf import FPDF

pdf = FPDF()

pdf.add_page()
pdf.set_font("helvetica", size=20)
pdf.write(5,"To find out what's new in tutorial, click")
pdf.set_font(style="U")
link = pdf.add_link(page=2)
pdf.write(5,"here",link)

# creating the second page which we will navigate through using the link
pdf.add_page()
pdf.image("logo.png",10,10,50,0,"","https://www.google.com")
pdf.set_left_margin(60)
pdf.set_font_size(18)
pdf.write_html("<b>This is some bold text</b>")

pdf.output('link.pdf')

