# Job configuration for validate.py

# Each key in the dictionary assigned to JOBS should be an abbreviated name for the job. The value should be a
# dictionary with two key-value pairs: the "full_name" key should have as its value a human-readable string identifying
# the job; the "queries" key should have as its value a list of query names from dbqueries.py.

# Standard modules
from typing import Literal, TypedDict

# Local modules
from dbqueries import QueryName


# Types

JobName = Literal['UDP']


class JobData(TypedDict):
    full_name: str
    queries: list[QueryName]


class JobDict(TypedDict):
    UDP: JobData


# Jobs configuration

JOBS: JobDict = {
    'UDP': {
        "full_name": "UDP Daily Status Report",
        "queries": [
            "udp_context_store_view_counts"
        ]
    }
}
