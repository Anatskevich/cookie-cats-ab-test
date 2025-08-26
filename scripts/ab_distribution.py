from pandas import DataFrame

def calculate_ab_distribution(df: DataFrame, group_name: str, aggregator_name: str):
    distribution = df.groupby(group_name, as_index = False).agg(
        number_of_players = (aggregator_name, 'count')
    )

    distribution['percent'] = ((distribution['number_of_players'] / distribution['number_of_players'].sum()) * 100).round(2)
    return distribution