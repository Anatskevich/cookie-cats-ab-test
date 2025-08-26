from pandas import DataFrame
import pandas as pd
from typing import List

def calculate_retention(df: DataFrame,
                        group_name: str,
                        retention_columns: List[str]):
    grouped = df.groupby(group_name, as_index=False).agg({
        col: 'mean' for col in retention_columns
    })

    grouped[retention_columns] = grouped[retention_columns] * 100

    difference_data = {
        group_name: ['difference']
    }

    for col in retention_columns:
        diff = grouped[col].iloc[0] - grouped[col].iloc[1]
        difference_data[col] = diff.round(2)

    additional_frame = pd.DataFrame(difference_data)
    final_table = pd.concat([grouped, additional_frame])

    return final_table