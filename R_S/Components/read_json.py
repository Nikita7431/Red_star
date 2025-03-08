import json

def open_r_json(file):
    file_path = file

    str = ""
    formats = []
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    # print(data)  
    
    for paper in data["paper_sizes"]:
        format_name = paper["format"]
        width = paper["width_mm"]
        height = paper["height_mm"]
        
        
        str=f"{format_name}/{width}X{height}                "
        formats.append(str)
         
        print(f"Формат: {format_name}, Размер: {width}x{height} мм")

    return formats      