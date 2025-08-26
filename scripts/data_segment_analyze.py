from pandas import DataFrame
from scripts.ttest import calculate_ttest

def get_late_starters(df: DataFrame) -> DataFrame:
    return df[(~df['retention_1']) & (df['retention_7'])]

def get_loyal_users(df: DataFrame) -> DataFrame:
    return df[(df['retention_1']) & (df['retention_7'])]

def analyze_segment(df: DataFrame) -> DataFrame:
    avg_levels = (
        df
        .groupby('test_version')
        .agg(
            players_count=('userid', 'count'),
            avg_levels=('sum_gamerounds', 'mean')
        )
        .round({'avg_levels': 2})
        .reset_index()
    )

    levels_difference = abs(avg_levels['avg_levels'].iloc[0] - avg_levels['avg_levels'].iloc[1])
    avg_levels['difference'] = ['-', levels_difference]

    std_dev = df.groupby('test_version')['sum_gamerounds'].std()
    population = avg_levels['players_count'].iloc[:2]
    mean = avg_levels['avg_levels'].iloc[:2]

    ttest_result = calculate_ttest(population[0], mean[0], std_dev.iloc[0], population[1], mean[1], std_dev.iloc[1])

    avg_levels['p_value'] = ['-', ttest_result.get('p_value')]
    avg_levels['t_value'] = ['-', ttest_result.get('t_stat')]
    avg_levels['Cohen_s d'] = ['-', ttest_result.get('cohen_d')]

    return avg_levels