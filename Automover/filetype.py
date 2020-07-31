import os

types = {'Audio': ['.aif', '.cda', '.mid', '.midi', '.mp3', '.mpa', '.ogg', '.wav', '.wma', '.wpl'], 'Compressed': ['.7z', '.arj', '.deb', '.pkg', '.rar', '.rpm', '.tar.gz', '.z', '.zip'], 'Disc': ['.bin', '.dmg', '.iso', '.toast', '.vcd'], 'Data': ['.csv', '.dat', '.db', '.dbf', '.log', '.mdb', '.sav', '.sql', '.tar', '.xml', '.accdb'], 'E-mail': ['.email', '.eml', '.emlx', '.msg', '.oft', '.ost', '.pst', '.vcf'], 'Executable': ['.apk', '.bat', '.bin', '.cgi', '.pl', '.com', '.exe', '.gadget', '.jar', '.msi', '.wsf'], 'Font': ['.fnt', '.fon', '.otf', '.ttf'], 'Image': ['.ai', '.bmp', '.gif', '.ico', '.jpeg', '.jpg', '.png', '.ps', '.psd', '.svg', '.tif', '.tiff'], 'Internet': [
    '.asp', '.aspx', '.cer', '.cfm', '.cgi', '.pl', '.css', '.htm', '.html', '.js', '.jsp', '.part', '.php', '.rss', '.xhtml'], 'Presentation': ['.key', '.odp', '.pps', '.ppt', '.pptx'], 'Programming': ['.c', '.class', '.cpp', '.cs', '.h', '.java', '.pl', '.py', '.sh', '.swift', '.vb'], 'Spreadsheet': ['.ods', '.xls', '.xlsm', '.xlsx'], 'System': ['.bak', '.cab', '.cfg', '.cpl', '.cur', '.dll', '.dmp', '.drv', '.icns', '.ico', '.ini', '.lnk', '.msi', '.sys', '.tmp'], 'Video': ['.3g2', '.3gp', '.avi', '.flv', '.h264', '.m4v', '.mkv', '.mov', '.mp4', '.mpg', '.mpeg', '.rm', '.swf', '.vob', '.wmv'], 'Doctumen': ['.doc', '.docx', '.odt', '.pdf', '.rtf', '.tex', '.txt', '.wpd', '.epub']}


def get_extention(filename):
    basename = os.path.basename(filename)
    name, extention = os.path.splitext(basename)
    return extention


def guess(filename):
    extention = get_extention(filename)
    for k, v in types.items():
        if extention in v:
            return k
    return None


def is_image(filename):
    extention = get_extention(filename)
    return extention in types['Image']


def is_video(filename):
    extention = get_extention(filename)
    return extention in types['Video']


def is_audio(filename):
    extention = get_extention(filename)
    return extention in types['Audio']
