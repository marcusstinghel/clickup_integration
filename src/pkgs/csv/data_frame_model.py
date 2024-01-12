from datetime import datetime as dt
import re
from src.pkgs.clickup import Task


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
        default = ''
        return [
            card.name,
            card.status.name,
            card.assignees[0].username if card.assignees else default,
            card.tags[0].name if card.tags else default,
            card.tags[0].name if card.tags else default,
            dt.fromtimestamp(int(card.start_date) / 1000) if card.start_date else default,
            dt.fromtimestamp(int(card.due_date) / 1000) if card.due_date else default,
            dt.fromtimestamp(int(card.date_closed) / 1000) if card.date_closed else default,
            items[0].name if len(items) >= 1 else default,
            items[1].name if len(items) >= 2 else default,
            items[4].name if len(items) >= 5 else default,
            (
                dt.strptime(items[5].name, "%d/%m/%Y").strftime("%Y-%m-%d")
                if len(items) >= 6
                and re.match(r'\d{2}/\d{2}/\d{4}', items[5].name)
                else default
            )
        ]
