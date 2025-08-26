from pandas import DataFrame
import pandas as pd

def get_outliers_value(df: DataFrame, column_name: str, percentile: float):
    return df[column_name].quantile(percentile)

def get_outliers_count(df: DataFrame, column_name: str, percentile: float):
    p99_threshold = df[column_name].quantile(percentile)
    return len(df[df[column_name] >= p99_threshold])

def clean_dataset(df: DataFrame, column_name: str, percentile: float, exclude_zero: bool):
    p99_threshold = df[column_name].quantile(percentile)

    if exclude_zero:
        return df[(df[column_name] > 0) & (df[column_name] < p99_threshold)].copy()

    return df[df[column_name] < p99_threshold].copy()

def calculate_zero_players(df: DataFrame,
                           version_column: str,
                           id_column: str,
                           levels_column: str):
    total_by_group = df.groupby(version_column)[id_column].count().reset_index(name='total_players')
    zero_players = df[df[levels_column] == 0] \
        .groupby(version_column)[id_column].count().reset_index(name='zero_players_count')

    final_table = pd.merge(total_by_group, zero_players, on=version_column)
    final_table['percent'] = (final_table['zero_players_count'] / final_table['total_players'] * 100).round(2)

    return final_table