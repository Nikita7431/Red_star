Создание спусков полос 
27.11.24 

Для формирования PDF используется библиотека tkPDFViewer,
для её установки запустить script_check_tkpdfviewer.py

. Вывод порядка нумерации полос реализован в модуле numbering
. Формирование PDF файла реализовано в модуле tk_pdf_collect_2

Все компоненты определены в папке Components 

    . root_Window.py - основное окно в котором размещаются остальные компоненты (Two_Windows и Toolbar)
    Под ним создаётся родительское окно и положение дочернего окна (root) зависит от parent (перемещается вместе с ним)
    . . hide_custom_menu() - обрабатывает закрытие выпадающего меню 
    . app.py создаются оба окна (parent и root)

    . two_window.py - разделяет окно на два используя paned_window 
    и добавляет в левой части поля для ввода, в правой части окно для вывода PDF 
    /* self.paned_window.add(left_bar)
        self.paned_window.add(self.pdf_frame)
    */

    . toolbar.py - toolbar, заменяющий стандартную оконную рамку (свернуть, полный экран, закрыть) 
    ..do_move() - служит для перемещения окна за toolbar

    . tb_filebox.py - выпадающее меню по кнопке Файл

. PDFViewer служит для создания виджета tkPDFViewer 
Сам виджет создаётся в методе open_pdf(file_name) 
В нём происходит проверка на наличие уже созданного окна 
/*
if self.current_view is not None:
            self.current_view.destroy()
          
            self.pdf_frame.update_idletasks()
        
*/  
/* self.v1.img_object_li.clear() */    -  удаляет собстввенный frame


В models определены:
    .read_format 
    В нём класс Format для формата листа

Активные поля для ввода:
. Доля
. Количество страниц 
. Первая страница 

-------------------------------------------------------------------------------------
Запускать app.py
После распаковки запустить script_check_tkpdfviewer.py 
