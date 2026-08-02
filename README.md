# Alloy Selection and Cost Optimization Simulator

A data-driven decision-support project for comparing engineering alloys and selecting the most suitable material based on performance, manufacturability, and cost.

![Python](https://img.shields.io/badge/Python-Analysis-3776AB?logo=python&logoColor=white)
![Excel](https://img.shields.io/badge/Excel-Data%20Source-217346?logo=microsoftexcel&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

## Overview

Selecting the right alloy requires balancing multiple engineering and business factors. A material with high strength may be expensive, while a low-cost alloy may not meet corrosion-resistance or processability requirements.

This project uses a weighted decision model to compare engineering alloys across key material properties and cost criteria. It ranks alternatives, performs sensitivity analysis, and supports what-if simulations to help users understand material-performance-cost trade-offs.

## Business Objectives

- Compare multiple engineering alloys using consistent evaluation criteria
- Identify the best alloy based on weighted decision factors
- Balance performance requirements with material cost
- Analyze the effect of changing decision priorities
- Support material-selection decisions with transparent, data-driven insights

## Evaluation Criteria

| Criterion | Description |
|---|---|
| Strength | Ability of the alloy to withstand applied loads |
| Hardness | Resistance to wear, indentation, and deformation |
| Density | Material weight consideration for the application |
| Corrosion Resistance | Ability to resist environmental degradation |
| Processability | Ease of manufacturing, machining, or fabrication |
| Cost | Relative material cost for the selected alloy |

## How the Simulator Works

```text
Alloy Data + Decision Criteria
            ↓
Data Preparation and Normalization
            ↓
Assign Weights to Each Criterion
            ↓
Calculate Weighted Scores
            ↓
Rank Alloy Alternatives
            ↓
Sensitivity Analysis and What-If Simulation
            ↓
Material Selection Insight
