from scipy import stats
import numpy as np

def calculate_ttest(n1, mean1, s1, n2, mean2, s2):
    """Calculate t-test, p-value and cohen's effect
    Args:
        n1, n2: size of set
        mean1, mean2: mean values
        s1, s2: standard deviation
    """

    t_stat, p_value = stats.ttest_ind_from_stats(
        mean1, s1, n1, mean2, s2, n2, equal_var=False
    )

    pooled_std = np.sqrt((s1 ** 2 + s2 ** 2) / 2)
    d = (mean1 - mean2) / pooled_std

    return {
        't_stat': round(t_stat, 3),
        'p_value': round(p_value, 3),
        'cohen_d': round(d, 3)
    }

if __name__ == '__main__':
    results = calculate_ttest(
        n1=42312, mean1=46.65, s1=72.94,
        n2=42977, mean2=46.49, s2=72.46
    )

    print(f't_stat: {results.get('t_stat')} p_value: {results.get('p_value')} cohen_d: {results.get('cohen_d')}')