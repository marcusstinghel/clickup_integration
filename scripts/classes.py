
import requests
import json
import csv

class ClickUp:
    def __init__(self, gdp, acess_token):
        self.gdp = gdp
        self.acess_token = acess_token
        self.page = 0

    def get_tasks_page(self, page):
        tasks_page = {}
        self.url = f'https://api.clickup.com/api/v2/list/{self.gdp}/task?page={page}&include_closed=true'
        response = requests.get(self.url, headers = {"Authorization": self.acess_token})
        tasks_json = json.loads(response.content)
        try: tasks_page = tasks_json['tasks']
        except: pass
        return tasks_page
    
    def get_tasks(self):
        page_getted = 0
        tasks = []
        tasks_page_number = 100
        while tasks_page_number != 0:
            tasks_page = self.get_tasks_page(page_getted)
            tasks_page_number = len(tasks_page)
            tasks.append(tasks_page)
            page_getted += 1
        return tasks

class CsvFolder:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.field_names = ['nome', 'status', 'responsavel', 'departamento', 'name_tag', 'data_inicio', 'data_finaliz', 'data_conclusao', 
                      'diretoria', 'produto', 'tipo_atividade', 'data_conclus_real']
    
    def prepara_arquivo_csv(self):
        with open(self.folder_path, 'w', newline= '') as file:
            file.write('')
            writer = csv.DictWriter(file, fieldnames= self.field_names)
            writer.writeheader()

    def file_writer(self, content):
        with open(self.folder_path, 'a', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames= self.field_names)
            writer.writerow(content)
