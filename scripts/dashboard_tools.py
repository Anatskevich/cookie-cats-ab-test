from typing import List
from pandas import DataFrame


def get_list_data_from_segment(segments: List[DataFrame],
                               indexer: str,
                               column_name: str,
                               loc_value: str) -> List[float]:
    values_list: List[float] = list()

    for segment in segments:
        values_list.append(segment.set_index(indexer)[column_name].loc[loc_value].round(2))

    return values_list

def get_loc_values_list(df: DataFrame,
                        indexer: str,
                        column_name: str,
                        loc_list: List[str]) -> List[float]:
    return df.set_index(indexer)[column_name].loc(loc_list).tolist()