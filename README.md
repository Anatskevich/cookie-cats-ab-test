# cookie-cats-ab-test
## Project Overview

This project contains a full-scale A/B test analysis for the popular mobile game "Cookie Cats". The game's core mechanic involves placing "gates" that force players to wait or make an in-app purchase to proceed. The test aimed to determine if moving the first gate from level 30 to level 40 would impact key player metrics.

## About the Data

The dataset contains simulated data from approximately 90,000 players who installed the game during the A/B test. Each row represents a player and includes:
*   `userid`: A unique identifier for the player.
*   `test_version`: Whether the player was in the control (`gate_30`) or treatment (`gate_40`) group.
*   `sum_gamerounds`: The number of game rounds played by the player during the first 14 days.
*   `retention_1`: Whether the player came back and played 1 day after installing.
*   `retention_7`: Whether the player came back and played 7 days after installing.

## How to Run

1.  Clone the repository:
    ```bash
    git clone https://github.com/your-username/cookie-cats-ab-test.git
    ```
2.  Navigate to the project directory and install the required dependencies (if needed):
    ```bash
    pip install -r requirements.txt
    ```
3.  Launch Jupyter Notebook:
    ```bash
    jupyter notebook
    ```
4.  Open and run the cells in `notebooks/project_notebook.ipynb` to see the full analysis.

## Technologies Used

*   **Language:** Python
*   **Libraries:** Pandas, NumPy, Matplotlib, Seaborn, SciPy
*   **Environment:** Jupyter Notebook
*   **Methods:** A/B Testing, Statistical Significance Testing (Z-test for proportions), Data Cleaning, Exploratory Data Analysis (EDA), Data Visualization.

## Analysis Steps

The Jupyter Notebook (`project_notebook.ipynb`) walks through the entire analytical process:

1.  **Data Loading & Inspection:** Initial check for data integrity, missing values, and basic structure.
2.  **Group Balance Check:** Verification that control (gate_30) and treatment (gate_40) groups are evenly sized and comparable.
3.  **Retention Rate Analysis:** Calculation and visualization of core metrics (1-day and 7-day retention) for both groups.
4.  **Statistical Hypothesis Testing:** Performing Z-tests to determine the statistical significance of the observed differences in retention.
5.  **Behavioral Analysis:** Analysis of the `sum_gamerounds` metric to understand player engagement and identify super-users (outliers).
6.  **Sensitivity Analysis:** Re-running the analysis after removing the top 1% of players to ensure the results are robust and not skewed by extreme outliers.
7.  **Conclusion & Recommendation:** Synthesizing the results into a clear, actionable business recommendation.