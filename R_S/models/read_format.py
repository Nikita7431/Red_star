class Format:
    
    _width = 0
    _height = 0
    
    @staticmethod
    def read_format(str):
        parts = str.split("X")
        Format._width = parts[0]
        Format._height = parts[1]
    
    