# Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# Каждая группа включает файлы с несколькими расширениями.
# В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

import shutil
import os
import random


# плюс/минус содержимое file_extensions_map взято из ...
#   https://github.com/jddinneen/file-extension-categoriser/blob/master/binfiles.py
file_extensions_map = {
  'text': ['doc', 'docx', 'docm', 'odt', 'pdf', 'txt', 'rtf', 'pages', 'pfb', 'mobi',
           'chm', 'tex', 'bib', 'dvi', 'abw', 'text', 'epub', 'nfo', 'log', 'wks',
           'wps', 'wpd', 'emlx', 'utf8', 'ichat', 'asc', 'ott', 'fra', 'opf'],
  'image': ['img','jpg', 'jpeg', 'png', 'png0', 'ai', 'cr2', 'ico', 'icon', 'jfif',
            'tiff', 'tif', 'gif', 'bmp', 'odg', 'djvu', 'odg', 'ai', 'fla', 'pic',
            'ps', 'psb', 'svg', 'dds', 'hdr', 'ithmb', 'rds', 'heic', 'aae',
            'apalbum', 'apfolder', 'xmp', 'dng', 'px', 'catalog', 'ita', 'visual',
            'shape', 'appicon', 'icns'],
  'development': ['py', 'h', 'm', 'jar', 'cs', 'c', 'c#', 'cpp', 'c++', 'class', 'java',
                  'php', 'phps', 'php5', 'htm', 'html', 'css', 'xml', '3mf', 'o', 'obj',
                  'json', 'jsonp', 'blg', 'bbl', 'j', 'jav', 'bash', 'bsh', 'sh', 'rb',
                  'vb', 'vbscript', 'vbs', 'vhd', 'vmwarevm', 'js', 'jsp', 'xhtml', 'nib',
                  'strings', 'frm', 'myd', 'myi', 'props', 'vcxproj', 'vs', 'lst', 'sol',
                  'pch', 'pdb', 'lib', 'nas', 'assets', 'sql', 'sqlite-wal', 'rss', 'swift',
                  'xsl', 'manifest', 'dist', 'ashx', 'tpm', 'dsw', 'hpp', 'tga', 'kf', 'cxx',
                  'rq', 'rdf', 'ttl', 'pyc', 'pyo', 'lua', 'vim', 'dashtoc', 'md', 'seto',
                  'mo', 'make', 'cmake', 'makefile', 'options', 'def', 'cc', 'f90', 'dcp'],
  'executable': ['exe', 'bat', 'dmg', 'msi', 'bin', 'pak', 'app', 'com', 'application'],
  'archive': ['zip', 'gz', 'rar', 'cab', 'iso', 'tar', 'lzma', 'bz2', 'pkg', 'xz', '7z',
              'vdi', 'ova', 'rpm', 'z', 'tgz', 'deb', 'vcd', 'ost', 'vmdk', 'arj', 'package', 'ims'],
  'audio': ['mp3', 'm3u', 'm4a', 'wav', 'ogg', 'flac', 'midi', 'oct', 'aac', 'aiff',
            'aif', 'wma', 'pcm', 'cda', 'mid', 'mpa', 'ens', 'adg', 'dmpatch', 'sngw',
            'seq', 'wem', 'mtp', 'l6t', 'lng', 'adx', 'link'],
  'database': ['accdb', 'accde', 'mdb', 'mde', 'odb', 'db', 'gdbtable', 'gdbtablx', 'gdbindexes',
               'sqlite', 'enz', 'enl', 'sdf', 'hdb', 'cdb', 'gdb', 'cif', 'xyz', 'mat', 'bgl',
               'r', 'exp', 'asy', 'info', 'meta', 'adf', 'appinfo', 'xg0', 'yg0'],
  'presentation': ['ppt', 'pptx', 'pps', 'ppsx', 'odp', 'key'],
  'video': ['mpg', 'mpeg', 'avi', 'mp4', 'flv', 'h264', 'mov', 'mk4', 'swf', 'wmv', 'mkv', 'plist',
            'm4v', 'trec', '3g2', '3gp', 'rm', 'vob']
}


# Чистка
def clearing():
    shutil.rmtree('.', ignore_errors=True)


# Наполнение
def seeds():
    for category, extensions in file_extensions_map.items():
        random.shuffle(extensions)

        for extension in extensions[:5]:
            file_name = ''.join(random.sample(category, len(category)))
            full_file_name = f'{file_name}.{extension}'

            if not os.path.exists(full_file_name):
                with open(full_file_name, 'w') as f:
                    f.write(category)

        if not os.path.exists(category):
           os.makedirs(category)

    with open('alone.file', 'w') as f:
        f.write('without category')


# Сортировка
def sorting():
    for category, extensions in file_extensions_map.items():
        full_file_names = []

        for (path, ds, fs) in os.walk('.'):
            full_file_names.extend(fs)
            break

        for full_file_name in full_file_names:
            extension = os.path.splitext(full_file_name)[1].replace('.', '')

            if extension in extensions:
                os.replace(full_file_name, f'./{category}/{full_file_name}')


if __name__ == '__main__':
    os.chdir('t1_cwd')

    clearing()
    seeds()
    sorting()
