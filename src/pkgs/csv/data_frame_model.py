from src.pkgs.clickup import Task
from datetime import datetime


class DataFrameModel:

    @classmethod
    def get_header(cls) -> list:
        return [
            'nome',
            'status',
            'responsavel',
            'departamento',
            'name_tag',
            'data_inicio',
            'data_finaliz',
            'data_conclusao',
            'diretoria',
            'produto',
            'tipo_atividade',
            'data_conclus_real'
        ]

    @classmethod
    def generate_new_line(cls, card: Task) -> list:
        items = card.checklists[0].items if card.checklists else []
        return [
            card.name,
            card.status.name,
            card.assignees[0].username if card.assignees else '',
            card.tags[0].name if card.tags else '',
            card.tags[0].name if card.tags else '',
            datetime.fromtimestamp(int(card.start_date) / 1000) if card.start_date else '',
            datetime.fromtimestamp(int(card.due_date) / 1000) if card.due_date else '',
            datetime.fromtimestamp(int(card.date_closed) / 1000) if card.date_closed else '',
            items[0].name if len(items) >= 1 else '',
            items[1].name if len(items) >= 2 else '',
            items[4].name if len(items) >= 5 else '',
            items[5].name if len(items) >= 6 and card.checklists[0].items[5].name != 'SEM DATA' else ''
        ]
