# Добавление QR-кода в многостраничный PDF документ
from pdfrw import PdfReader, PdfWriter, PageMerge
import os
from pathlib import Path
import time
import sqlite3
from datetime import datetime

print('-----------------------')
print(os.path.abspath(os.curdir))
print('-----------------------')

class SQLLiter():
    
    def __init__(self, sqlite_path):
        self.sqlite_path = sqlite_path
    
    def connect(self):
        self.conn = sqlite3.connect(self.sqlite_path)
        self.cursor = self.conn.cursor()
    
    def get_task(self):
        sql = "SELECT * FROM PDFEditor_wotermark WHERE status=?"
        self.cursor.execute(sql, [("В очереди")])
        return self.cursor.fetchall()
    
    def disconnect(self):
        self.cursor.close()
        
    def set_status(self, new_status, pathESP, id_db):
        sql = 'UPDATE PDFEditor_wotermark SET status = ?, pathESP = ? where id = ?'
        self.cursor.execute(sql, (new_status, pathESP, id_db))
        self.conn.commit()
    
    def get_path_of_id(self, id_db):
        sql = "SELECT * FROM PDFEditor_wotermark WHERE id=?"
        self.cursor.execute(sql, [(id_db)])
        return self.cursor.fetchall()

    def get_path_ECP_id(self, id_PDFEditor_ecp):
        sql = "SELECT * FROM PDFEditor_ecp WHERE id = ?"
        self.cursor.execute(sql, [(id_PDFEditor_ecp)])
        data_set = self.cursor.fetchall()
        return str(data_set[0][1])



#Получаем все XML в папку in   
def lists_pdf(path_katalog):
    return [i for i in os.listdir(path=path_katalog) if Path(i).suffix == '.pdf'] # запрос


def watermark_pdf_create(input_file, output_file, watermark_file):
    # определяем объекты чтения и записи
    reader_input = PdfReader(input_file)
    writer_output = PdfWriter()
    watermark_input = PdfReader(watermark_file)
    watermark = watermark_input.pages[0]
    # просматривать страницы одну за другой
    for current_page in range(len(reader_input.pages)):
        merger = PageMerge(reader_input.pages[current_page])
        merger.add(watermark).render()
    # записать измененный контент на диск
    writer_output.write(output_file, reader_input)

if __name__ == '__main__':

    path_katalog = "./files/media/pathNew/"
    watermark_file = "./source/ЭЦП.pdf"
    sqlite_path = './db.sqlite3'
    pathMedia = './files/media/'
    sql_db = SQLLiter(sqlite_path)

    #Вечный цикл
    while True:
        sql_db.connect()
        #Тут я получаю все файлы из папки, надо переопределить pdf_all для путей из БД
        #pdf_all = lists_pdf(path_katalog)
        
        #Получаю данные из БД
        pdf_all = []
        query_set_all = sql_db.get_task()
        query_set_id_db = []       
        for item in query_set_all:
            query_set_id_db.append(item[0])
            pdf_all.append(item[0])
        

        coutn = len(pdf_all)

        for i in pdf_all:
            #Вызов функции преобразования
            new_path = pathMedia + "pathNew/" + datetime.strftime(datetime.now(), "%Y/%m/%d/%H/%M/%S/")
            try:
                os.makedirs(new_path, mode=0o777, exist_ok=False)
            except:
                #каталог существует
                pass

            try:
                query_set = sql_db.get_path_of_id(i)
                pathOld = str(query_set[0][3]).replace('/', '/')
                watermark_file = pathMedia + str(sql_db.get_path_ECP_id(query_set[0][5])).replace('/', '/')             
                namefile = os.path.basename(pathOld)
                print(query_set)
                # Это тестовый код!!!!!!!!!!!!!!!!!!!!!!!!!
                
                #continue
                new_path_full = new_path + namefile
                new_path_full = new_path_full.replace('/', '/')
                new_path_full = new_path_full[2:]
            
                watermark_pdf_create(pathMedia + pathOld, new_path_full, watermark_file)
                new_path_full = new_path_full.replace(pathMedia[2:].replace('/', '/'), '')
                #А впрочем нет ничего более временого чем постоянное.

                sql_db.set_status("Готово", new_path_full, i)
                print('OK')
            except sqlite3.Error:
                sql_db.set_status("Ошибка работы с БД", "Фатальный Егор", i)
                print('Ошибка работы с БД')
            coutn -= 1
        sql_db.disconnect()
        time.sleep(10)



    




