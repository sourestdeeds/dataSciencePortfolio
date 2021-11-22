***

# **`serenity`**

A gradient descent ensemble boosted tree (regressor!) to compare predictions versus [`Forecaster`](https://github.com/chenjj2/forecaster). 

<p align="center">
  <img src="https://github.com/sourestdeeds/dataSciencePortfolio/blob/main/Project%20Serenity/shap2.png">
</p>

```python
Predicting the Mass:

+-------------+---------+--------------+--------------+----------------------------+----------------------------+---------------------------+
| Planet      |    Test |   Prediction |   Forecaster |   Residual Test-Prediction |   Residual Test-Forecaster | Prediction < Forecaster   |
|-------------+---------+--------------+--------------+----------------------------+----------------------------+---------------------------|
| Kepler-17 b | 2.47000 |      2.17690 |      3.70134 |                    0.29310 |                    1.23134 | True                      |
| Kepler-56 b | 0.74300 |      0.11561 |      0.11645 |                    0.62739 |                    0.62655 | False                     |
| XO-1 b      | 0.91300 |      0.75850 |      5.03887 |                    0.15450 |                    4.12587 | True                      |
| WASP-72 b   | 1.54610 |      2.13558 |      2.43534 |                    0.58948 |                    0.88924 | True                      |
| HATS-6 b    | 0.31900 |      1.00091 |      7.65828 |                    0.68191 |                    7.33928 | True                      |
| WASP-7 b    | 1.25000 |      1.65510 |      9.44126 |                    0.40510 |                    8.19126 | True                      |
| Kepler-29 c | 0.01259 |      0.05699 |      0.03317 |                    0.04440 |                    0.02058 | False                     |
| L 98-59 c   | 0.00761 |      0.00977 |      0.00766 |                    0.00216 |                    0.00005 | False                     |
| TrES-2 b    | 1.19800 |      1.14120 |      6.21201 |                    0.05680 |                    5.01401 | True                      |
| WASP-32 b   | 2.63000 |      1.89571 |      9.44126 |                    0.73429 |                    6.81126 | True                      |
| KPS-1 b     | 1.09000 |      1.46330 |      7.65828 |                    0.37330 |                    6.56828 | True                      |
| K2-266 e    | 0.04499 |      0.02528 |      0.02183 |                    0.01971 |                    0.02316 | True                      |
| HAT-P-41 b  | 0.79500 |      1.09818 |     30.01569 |                    0.30318 |                   29.22069 | True                      |
| KELT-7 b    | 1.28000 |      2.50883 |      4.08728 |                    1.22883 |                    2.80728 | True                      |
| HAT-P-13 b  | 0.90600 |      0.90435 |      3.00234 |                    0.00165 |                    2.09634 | True                      |
+-------------+---------+--------------+--------------+----------------------------+----------------------------+---------------------------+

Residual sum for Prediction: 5.52
Residual sum for Forecaster: 74.97
Prediction versus Forecaster Accuracy: 12/15
```
# Prediction vs. Forecaster
- Display all the predicted values against the forecaster package, take the residuals of both and rank for `Prediction < Forecaster`.
- Then see how many times it takes for Forecaster to have a better accuracy than our prediction.


# Dataset
- Dataset acquired from the [`NASA Exoplanet Archive`](https://exoplanetarchive.ipac.caltech.edu)
- `ML_nasa_tess_viable` is a collection of all exoplanets with a TESS data product.

# Model: `XGBRegressor()`
- Test-Train splits have a test size of `0.2`.
- Data leakage accounted for with piplines handling preprocessing before cross-validation.
- Capable of handling categorical or numerical columns.
- Categorical uses `OneHotEncoder()` and the most frequent string if there are missing values using `SimpleImputer()`.
- Numerical preprocessing steps use the `RobustScalar()` method and a mean strategy using `SimpleImputer()`.
- Need to investigate why `count:possion` gives the best accuracy.

# Shap Values
Shap values show how much a given feature changed our prediction (compared to if we made that prediction at some baseline value of that feature). Permutation importance is great because it created simple numeric measures to see which features mattered to a model. This helped us make comparisons between features easily, and you can present the resulting graphs to non-technical audiences.

But it doesn't tell you how each features matter. If a feature has medium permutation importance, that could mean it has

- A large effect for a few predictions, but no effect in general, or
- A medium effect for all predictions.
