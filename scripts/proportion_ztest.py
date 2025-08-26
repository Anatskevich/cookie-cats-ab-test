from typing import overload
from statsmodels.stats.proportion import proportions_ztest

@overload
def calculate() -> float: ...

@overload
def calculate(count: list[int], nobs: list[int]) -> float: ...

def calculate(count=None, nobs=None):
    if count is None or nobs is None:
        count = [1937, 2057] #number of success (zero players for example)
        nobs = [44700, 45489] #number of users in data. Full users count

    z_stat, p_value = proportions_ztest(count, nobs, alternative='two-sided')
    print(f"Z-stat: {z_stat:.3f}, p-value: {p_value:.3f}")
    return p_value

if __name__ == '__main__':
    calculate()