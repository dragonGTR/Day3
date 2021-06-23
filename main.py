from configparser import ConfigParser
from collections import Counter
import sys
import logging

class Testing:
    def __init__(self,filename):
        self.filename = filename


    def read_file(self):
        file_data = open(self.filename,'r')
        return file_data


class PerformManipulation(Testing):
    def __init__(self,filename):
        super().__init__(filename)

    def file_data(self):
        lines = self.read_file()
        lines = lines.readlines()
        words_list = []

        for line in lines:
            arr = [str for str in line.split()]
            words_list.extend(arr)
        return words_list

    def count_prefix(self):
        result_data = self.file_data()
        prefix_count = 0
        for i in range(len(result_data)):
            if (i != 0):
                if result_data[i - 1] == 'to':
                    prefix_count += 1
        return prefix_count

    def ends_with(self):
        result_data = self.file_data()
        end_count = 0
        for i in range(len(result_data)):
            if result_data[i].endswith("ing"):
                end_count += 1

        return end_count

    def maximum_word(self):
        result_data = self.file_data()
        c = Counter(result_data)
        return c.most_common(1)


    def palindrome_words(self):
        result_data = self.file_data()
        str1 = []
        palindrome = 0
        for i in range(len(result_data)):
            if (result_data[i][::-1] ==
                        result_data[i]):
                palindrome += 1
                str1.append(result_data[i])
            if (i == len(result_data) - 1 and
                        palindrome == 0):
                str1.append("No Palindrome")
        return str1


    def unique_list(self):
        result_data = self.file_data()
        set1 = set(result_data)
        unique_list2 = list(set1)
        return unique_list2

    def dict_index(self):
        result_data = self.file_data()
        Word = dict()
        count = 0
        for line in result_data:
            words = line.split(" ")
            print(words)
            for word in words:
                Word[count] = word
                count += 1
        return Word


    def display_results(
                  self,prefix,
                  end,max1,
                  palindrome,unique,dicts):
        log_name = config['logging name']['name1']
        print(type(log_name))
        logging.basicConfig(filename=log_name,level=logging.DEBUG)
        logging.debug(prefix)
        logging.info(end)
        logging.warning(max1)
        logging.critical(palindrome)
        logging.error(unique)
        logging.debug(dicts)

    def __del__(self):
        print("Deleted")

try:
    file = 'config.ini'
    config = ConfigParser()
    config.read(file)
    filename = config['filename']['filename']

    test = PerformManipulation(filename)
    num_prefix = test.count_prefix()
    ends_with = test.ends_with()
    max_count = test.maximum_word()
    palindrome_words = test.palindrome_words()
    unique_set = test.unique_list()
    dicts_index = test.dict_index()
    test.display_results(
            num_prefix,ends_with,
            max_count,palindrome_words,
            unique_set,dicts_index,)
    del test 


except Exception as e:
    sys.stderr.write(str(e))

