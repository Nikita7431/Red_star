from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from numbering import print_sheet_numbering
from models.read_format import *
from reportlab.lib.units import mm, inch
from reportlab.lib.colors import *
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('Arial', 'arial.ttf'))

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



def create_pdf_with_numbering(filename, pages, drops,  first_entry, number_public):
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
    pdf = canvas.Canvas(filename, pagesize=(_pagesize[1],_pagesize[0]))
    pdf.setFont("Arial",12)  
    
    end_index = create_end_index(drops) 
    end_index_row = create_end_index_row(drops)

    left_margin = (LEFT_MARGIN_RATIO) * page_height
    top_margin = (1-TOP_MARGIN_RATIO) *  page_width
    right_margin = (1-LEFT_MARGIN_RATIO) * page_height
    bottom_margin = (TOP_MARGIN_RATIO) *  page_width

    usable_width = right_margin- left_margin 
    usable_height = top_margin - bottom_margin

    cell_width = usable_width / end_index
    cell_height = usable_height / end_index_row


    #num_one_rows_on_page = int((usable_height // cell_height) // 2)  
    #items_per_page = end_index * num_one_rows_on_page  

    
    SPACING = 0

    
    def draw_page(items, number = "0", number_call = 2):
        """Отрисовка страницы с номерами"""
        pdf.setLineWidth(2)
        pdf.setStrokeColor(black) 
        
        def_schet_page = all_page_for_one_page
        schet_page = def_schet_page

        isFirst = False
        if(int(number_call) == 1):
            isFirst = True
        for row in range(end_index_row):
            for col in range(end_index):

                index = row * end_index + col

                if index >= len(items):  
                    break

                x = left_margin + SPACING + col * (cell_width)
                y = top_margin - row * (cell_height)

                pdf.rect(x, y - cell_height, cell_width-2*SPACING, cell_height-SPACING) 
                write_item = str(items[index])
                print("write_item "+ write_item)
                print("number "+ number)
                print("1schet_page " + str(schet_page))
                if((int(index) == int((schet_page/2)-1) or int(index) == 0)):
                    print("2schet_page " + str(schet_page)+"..."+str(int(index) == int((schet_page/2)-1))+"..."+str(int(index) == 0))
                    print("2index "+str(index))
                    
                    if(number_call == 1 and int(index) == 0 and isFirst == True):
                        print("..........number_call in method " + str(number_call))

                        isFirst = False
                        print("Continue")
                    else:
                        draw_x(x,y,green)           
                    # if(number_call!=1): 
                    #         draw_x(x,y,green)
                    # if(int(index) == int((schet_page/2)-1)):
                    #         schet_page += def_schet_page-1
                    # elif(number_call==1):
                    #     if(int(index)!=0):
                    #         draw_x(x,y,green)
                    #         schet_page += def_schet_page-1
                    #         print("3schet_page " + str(schet_page)) 
                            
                                    
                    
                    
                        
                        
                  
                       
                
                
                
                if(write_item == number):
                    pdf.setStrokeColor(red) 
                    
                    x1 = x
                    y1 = y 
                    x2 = x1 + cell_width - 2 * SPACING
                    y2 = y1 - cell_height - SPACING
                    
                    pdf.line(x1, y1, x2, y2)
                    pdf.line(x2, y1, x1, y2)

                    if(x-cell_width <=0):
                        pdf.line(x1+cell_width, y1, x2+cell_width, y2)
                        pdf.line(x2+cell_width, y1, x1+cell_width, y2)
                    else:
                        pdf.line(x1-cell_width, y1, x2-cell_width, y2)
                        pdf.line(x2-cell_width, y1, x1-cell_width, y2)
                                
                    pdf.setFont("Arial",28)  
                    pdf.setFillColor(red)
                    # pdf.rotate(90)
                    #pdf.drawString(x + cell_width / 2 - 15, y - cell_height / 2, "Реклама")
                    pdf.drawCentredString(x + cell_width / 2 - 15, y - cell_height / 2, "Реклама")
                    pdf.setFillColor(black)
                    pdf.setFont("Arial",12)  
                    
                if int(write_item ) > (pages+first_entry-1):
                    write_item = " "
                pdf.rotate(90)  
                pdf.drawString(y - cell_height / 2, -(x + cell_width - 50), write_item)  #pdf.drawString(x + cell_width -50, y - cell_height / 2, write_item)
                pdf.rotate(-90)  
                pdf.setStrokeColor(black) 
                
    def draw_x(x,y,color):
        x1 = x
        y1 = y 
        x2 = x1 + cell_width - 2 * SPACING
        y2 = y1 - cell_height - SPACING
        pdf.setStrokeColor(color)
        pdf.line(x1, y1, x2, y2)
        pdf.line(x2, y1, x1, y2)
        pdf.setStrokeColor(black)
        
    number_calls = 1
    
    while(schet < drop_for_one_page):
        pairs = print_sheet_numbering(pages,drops, first_for_list)
        first_half = pairs[:len(pairs) // 2]
        second_half = pairs[len(pairs) // 2:]
        lena = len(pairs)
        first_for_list += lena
        
        
       
        for items in [first_half, second_half]:
            draw_page(items, number_public, number_calls)
            number_calls+=1
            print("..........number_call" + str(number_calls))
            
            pdf.showPage()  
        schet+=1
    
    pdf.save()
  