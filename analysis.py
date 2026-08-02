from pathlib import Path
import pandas as pd

folder = Path(__file__).parent
alloys = pd.read_csv(folder / "data" / "alloys.csv")

benefit_columns = ["Tensile_Strength_MPa", "Hardness_HB", "Corrosion_Rating", "Processability_Rating"]
cost_columns = ["Density_g_cm3", "Cost_INR_kg"]

scenarios = {
    "Balanced": [0.25, 0.15, 0.10, 0.20, 0.15, 0.15],
    "Performance": [0.35, 0.20, 0.10, 0.25, 0.05, 0.05],
    "Budget": [0.15, 0.10, 0.10, 0.15, 0.20, 0.30]
}

criteria = ["Tensile_Strength_MPa", "Hardness_HB", "Density_g_cm3", "Corrosion_Rating", "Processability_Rating", "Cost_INR_kg"]

def rank_alloys(data, weights):
    normalized = data.copy()
    for column in benefit_columns:
        normalized[column] = (data[column] - data[column].min()) / (data[column].max() - data[column].min())
    for column in cost_columns:
        normalized[column] = (data[column].max() - data[column]) / (data[column].max() - data[column].min())
    score = sum(normalized[column] * weight for column, weight in zip(criteria, weights))
    result = data[["Alloy"]].copy()
    result["Score"] = score.round(4)
    result["Rank"] = result["Score"].rank(method="dense", ascending=False).astype(int)
    return result.sort_values(["Rank", "Alloy"])

output = folder / "output"
output.mkdir(exist_ok=True)

balanced_ranking = rank_alloys(alloys, scenarios["Balanced"])
balanced_ranking.to_csv(output / "balanced_ranking.csv", index=False)

scenario_results = []
for name, weights in scenarios.items():
    result = rank_alloys(alloys, weights)
    result.insert(0, "Scenario", name)
    scenario_results.append(result)

pd.concat(scenario_results).to_csv(output / "scenario_results.csv", index=False)
alloys.drop(columns="Alloy").describe().round(2).to_csv(output / "statistics_summary.csv")

print(balanced_ranking.to_string(index=False))
