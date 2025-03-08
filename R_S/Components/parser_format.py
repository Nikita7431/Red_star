def parse_format(strFormat:str):
    strf = list(map(str,strFormat.lstrip().split("/")))
    
    result = strf[1]
    return result