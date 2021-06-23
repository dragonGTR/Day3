import re
import sys
import random
import string
import logging
from configparser import ConfigParser

class Testing:
    def __init__(self, filename):
        self.filename = filename

    def read_file(self):
        file_data = open(self.filename, 'r')
        return file_data
    def write_file(self,filename,str1):
        file_name = open(filename,"a")
        file_name.write(str(str1))
        file_name.close()






class PerformManipulation(Testing):
    def __init__(self, filename):
        super().__init__(filename)

    def file_data(self):
        lines = self.read_file()
        line = lines.readlines()
        file_list = []

        for lines in line:
            arr = [str for str in lines.split()]
            file_list.extend(arr)
        return file_list

    def line_data(self):
        lines = self.read_file()
        line = lines.readlines()
        return line


    def generate_name(self):
        length = 5
        file_name = ''.join([random.choice(string.ascii_letters) for _ in range(length)])
        return file_name

    def write_result(self,str1):
        log_name = config['logging name']['name2']
        logging.basicConfig(filename=log_name, level=logging.DEBUG)
        logging.debug(str1)
        name = self.generate_name()
        self.write_file(name, str1)

    def split_vowels(self):
        vowels_list = []
        words = self.file_data()
        for i in range(len(words)):
            word1 = words[i]
            result = re.split('a|e|i|o|u', word1)
            vowels_list.append(result)

        self.write_result(vowels_list)



    def capital_third_character(self):
        str1 = ''
        words = self.file_data()
        for word in words:
            if len(word)>=3:
                str1 += word[:2]\
                        +word[2].upper()\
                        +word[2+1:]+' '
            else:
                str1 += word+' '
        self.write_result(str1)

    def capital_elements(self):
        words = self.file_data()
        for i in range(len(words)):
            if i % 5 == 4:
                words[i] = words[i].upper()
        self.write_result(words)

    def new_line(self):
        words = self.file_data()
        str2 = ' '.join(words)
        str3 = ''
        for i in range(len(str2)):
            if str2[i] == ' ':
                str3 += '-'
            else:
                str3 += str2[i]
        self.write_result(str3)


    def semi_colon(self):
        list4 =[]
        lines = self.line_data()
        for i in range(len(lines)):
            if (len(lines) > 1):
                if i != len(lines) - 1:
                    list4.append(lines[i] + ";")
                else:
                    list4.append(lines[i])
            else:
                list4.append(lines[i])

        self.write_result(list4)

    def __del__(self):
        print("Deleted")




try:
    file = 'config.ini'
    config = ConfigParser()
    config.read(file)
    filename = config['filename']['filename']
    test = PerformManipulation(filename)
    test.split_vowels()
    test.capital_third_character()
    test.capital_elements()
    test.new_line()
    test.semi_colon()
    del test

except Exception as e:
    sys.stderr.write(str(e))




