# Standard modules
from datetime import datetime, timezone
from typing import Callable, Literal, TypedDict, Union

# Local modules
from data_sources import DataSourceName


# Types

class CheckData(TypedDict):
    color: Literal['YELLOW', 'RED']
    condition: Union[Callable[[str], bool], Callable[[int], bool]]
    rows_to_ignore: list[str]


class QueryData(TypedDict):
    output_file_name: str
    data_source: DataSourceName
    query_name: str
    checks: dict[str, CheckData]


class StandardQueryData(QueryData):
    type: Literal['standard']
    query: str


class TableRecordCountsQueryData(QueryData):
    type: Literal['table_record_counts']
    tables: list[str]



class QueryDict(TypedDict):
    udp_context_store_view_counts: TableRecordCountsQueryData


QueryName = Literal[
    'udp_context_store_view_counts'
]


# Check functions

NOT_ZERO: Callable[[int], bool] = (lambda x: x != 0)
LESS_THAN_TWO: Callable[[int], bool] = (lambda x: x < 2)
LESS_THAN_TWO_DAYS: Callable[[str], bool] = (lambda x: (datetime.now(tz=timezone.utc) - datetime.fromisoformat(x)).days < 2)

# Queries configuration

QUERIES: QueryDict = {
    'udp_context_store_view_counts': {
        'output_file_name': 'udp_context_store_view_counts.csv',
        'data_source': 'UDP_Context_Store',
        'query_name': 'UDP Context Store View Record Counts',
        'type': 'table_record_counts',
        'tables': [
            'entity.learner_activity',
            'entity.course_offering',
            'entity.course_grade',
            'entity.academic_term',
            'entity.annotation',
            'entity.learner_activity_result',
            'entity.person',
        ],
        'checks': {
            'not_zero': {
                'color': 'YELLOW',
                'condition': NOT_ZERO,
                'rows_to_ignore': []
            }
        }
    }
}