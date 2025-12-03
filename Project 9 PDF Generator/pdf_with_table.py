from fpdf import FPDF
from fpdf.fonts import FontFace
import csv

with open("countries.txt",encoding="utf-8") as csv_file:
    # save each line/row in a list
    # this reads the csv file
    data = list(csv.reader(csv_file,delimiter=","))


pdf = FPDF()
pdf.set_font("helvetica",size=14)

pdf.add_page()
# this sets the color of the lines separating the columns
pdf.set_draw_color(255,100,0)
# the width of the lines 
pdf.set_line_width=0.3

headings_style = FontFace(emphasis="BOLD",color=255,fill_color=(255,100,0))
with pdf.table(borders_layout="NO_HORIZONTAL_LINES", cell_fill_color=(224,235,255), col_widths=(42,39,35,42), line_height=6, headings_style=headings_style, text_align=("LEFT","CENTER","RIGHT","RIGHT"),width=160) as table:
    for data_row in data:
        # looping through each list(row)
        row = table.row()
        for data in data_row:
            # looping through each cell in row (Name of country, capital etc)
            row.cell(data)

pdf.output("table.pdf")


