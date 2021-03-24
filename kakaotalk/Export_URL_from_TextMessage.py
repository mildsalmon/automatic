#-*- coding: utf-8 -*-

import os

class ExportURL():
    def __init__(self):
        file_list = self.print_file_list()

        choice_num = int(input("URL을 추출할 파일 번호를 입력하세요 : "))

        file_name = self.select_file(file_list, choice_num)

        print("'{0}' 파일을 선택하셨습니다".format(file_name))

        contents = self.read_txt(file_name)

        url = self.export_url(contents)

        self.write_csv(file_name, url)

    def print_file_list(self):
        path = os.path.dirname(os.path.abspath(__file__))
        list_dir = os.listdir(path)

        file_list = dict()
        name_list = []

        for name in list_dir:
            if 'txt' in name:
                name_list.append(name)
                file_list[len(name_list)] = name

        # print(file_list)

        for file in file_list.items():
            # print(file)
            num = file[0]
            name = file[1]

            print("{0} : {1}".format(num, name))
        # print(file_list[1])
        return file_list

    def select_file(self, file_list, num):
        choice = file_list[num]

        # print(choice)

        return choice

    def read_txt(self, file_name):
        with open(file_name, "r", encoding='utf-8') as f_read:
            lines = f_read.readlines()

            # for line in lines:
            #     print(line)
        # print(lines)
        return lines

    def export_url(self, contents):
        url_txt = list()

        for content in contents:
            if (content.find('https:') != -1) or (content.find('http:') != -1):
                url_txt.append(content)

        for txt in url_txt:
            print(txt)
        print(len(url_txt))

        return url_txt

    def write_csv(self, file_name, url):
        with open("{0}.csv".format(file_name[:-4]), "w", encoding='utf-8-sig') as f_write:
            for text in url:
                f_write.write("{0}".format(text))

if __name__ == "__main__":
    ExportURL()