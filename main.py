
from dotenv import load_dotenv
from datetime import datetime
import classes as cs
import os

token = 'pk_3249047_FG83KQ8W65G06FA7H89DO7HPFL1RRZQ2'
gdp = '900700204280'
csv_path = 'C:\PDI\Repositorio\ClickUp\CSV\data.csv'

clickup = cs.ClickUp(gdp, token)
tasks = clickup.get_tasks()
csv_file = cs.CsvFolder(csv_path)
task_dados = {}
tasks_list = []
for page in tasks:
    for task in page:
        try:
            try: task_dados['nome'] = task['name']
            except: pass
            try: task_dados['status'] = task["status"]["status"]
            except: pass
            try: task_dados['responsavel'] = task['assignees'][0]['username']
            except: pass
            try: task_dados['departamento'] = task['tags'][0]['name']
            except: pass
            try: task_dados['name_tag'] = task['tags'][0]['name']
            except: pass
            try: task_dados['data_inicio'] = datetime.fromtimestamp(int(task['start_date']) / 1000)
            except: task_dados['data_inicio'] = ''
            try: task_dados['data_final'] = datetime.fromtimestamp(int(task['due_date']) / 1000)
            except: task_dados['data_final'] = ''
            try: task_dados['data_conclusao'] = datetime.fromtimestamp(int(task['date_closed']) / 1000).strftime('%Y-%m-%d %H:%M:%S')
            except: task_dados['data_conclusao'] = ''
            try: task_dados['diretoria'] = task['checklists'][0]['items'][0]['name']
            except: pass
            try: task_dados['produto'] = task['checklists'][0]["items"][1]["name"]
            except: pass
            try: task_dados['tipo_atividade'] = task['checklists'][0]['items'][4]['name']
            except: pass
            try: card_data_conclusao_real = task['checklists'][0]['items'][5]['name']
            except: pass
            try:
                if card_data_conclusao_real == 'SEM DATA': task_dados['data_conclusao_real'] = ''
                else: task_dados['data_conclusao_real'] = str(card_data_conclusao_real)
            except: pass
        except: pass
        tasks_list.append(task_dados.copy())

csv_file.prepara_arquivo_csv()
for task in tasks_list:
    content = ({'nome': task['nome'], 'status': task['status'], 'responsavel': task['responsavel'], 'departamento': task['departamento'], 'name_tag': task['name_tag'], 
                'data_inicio': task['data_inicio'], 'data_finaliz': task['data_final'], 'data_conclusao': task['data_conclusao'], "diretoria": task['diretoria'], 
                "produto": task['produto'], "tipo_atividade": task['tipo_atividade'], "data_conclus_real": task['data_conclusao_real']})
    csv_file.file_writer(content)
