from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from numbering import print_sheet_numbering
from models.read_format import *
from reportlab.lib.units import mm, inch

# Параметры страницы
# cell_width = 100
# cell_height = 80
# left_margin = 50
# top_margin = 750


LEFT_MARGIN_RATIO = 0.0000000001  
TOP_MARGIN_RATIO = 0.000000000001 



def create_end_index(drops):
    """количество элементов в строке"""
   
    match drops:
        case 1:
            return 1 
        case 2: 
            return 2
        case 3: 
            return 2 
        case 4: 
            return 4
    return 1  

def create_end_index_row(drops):
    """количество строк """

    match drops:
        case 1:
            return 2 
        case 2: 
            return 2
        case 3: 
            return 4 
        case 4: 
            return 4
        
    return 1  



def create_pdf_with_numbering(filename, pages, drops,  first_entry):
    all_page_for_one_page = pow(2,int(drops)) * 2 
    drop_for_one_page = int(pages) / all_page_for_one_page
    
    first_for_list = int(first_entry)
    schet  = 0 
  
    Format._width = int(Format._width) *mm
    Format._height = int(Format._height) *mm    
    page_width = Format._width
    page_height = Format._height
    print(f"pw: {page_width}, ph: {page_height}")
    
    _pagesize = (page_width,page_height)
    print(_pagesize)
    pdf = canvas.Canvas(filename, pagesize=(_pagesize[0],_pagesize[1]))
    
    end_index = create_end_index(drops) 
    end_index_row = create_end_index_row(drops)

    left_margin = (LEFT_MARGIN_RATIO) * page_width
    top_margin = (1-TOP_MARGIN_RATIO) * page_height
    right_margin = (1-LEFT_MARGIN_RATIO) * page_width
    bottom_margin = (TOP_MARGIN_RATIO) * page_height

    usable_width = right_margin- left_margin 
    usable_height = top_margin - bottom_margin

    cell_width = usable_width / end_index
    cell_height = usable_height / end_index_row


    #num_one_rows_on_page = int((usable_height // cell_height) // 2)  
    #items_per_page = end_index * num_one_rows_on_page  

    
    SPACING = 0

    def draw_page(items):
        """Отрисовка страницы с номерами"""
        for row in range(end_index_row):
            for col in range(end_index):

                index = row * end_index + col

                if index >= len(items):  
                    break

                x = left_margin + SPACING + col * (cell_width)
                y = top_margin - row * (cell_height)

                pdf.rect(x, y - cell_height, cell_width-2*SPACING, cell_height-SPACING) 
                
                write_item = str(items[index])
                if int(write_item ) > (pages+first_entry-1):
                    write_item = " "
                pdf.drawString(x + cell_width / 2   , y - cell_height / 2, write_item)
    
    
    while(schet < drop_for_one_page):
        pairs = print_sheet_numbering(pages,drops, first_for_list)
        first_half = pairs[:len(pairs) // 2]
        second_half = pairs[len(pairs) // 2:]
        lena = len(pairs)
        first_for_list += lena
        for items in [first_half, second_half]:
            draw_page(items)
            pdf.showPage()  
        schet+=1

    pdf.save()
  