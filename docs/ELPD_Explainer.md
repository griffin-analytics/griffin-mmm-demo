# Understanding Model Evaluation Metrics in Griffin MMM

## Leave-One-Out (LOO) Cross-Validation Metrics

### ELPD (Expected Log Pointwise Predictive Density)
The ELPD is a key metric for assessing predictive accuracy in Bayesian models:

* **Definition**: Measures how well the model predicts new, unseen data points
* **Interpretation**: 
  - Higher values indicate better predictive performance
  - Scale depends on dataset size and complexity
* **Usage**: 
  - Compare different model specifications 
  - Evaluate model robustness
  - Guide model selection

### Effective Parameters (p_loo)
The p_loo metric helps understand model complexity:

* **Definition**: Estimates the effective number of parameters accounting for:
  - Model structure
  - Data utilization
  - Parameter interactions
* **Interpretation**:
  - Lower values suggest simpler models
  - Higher values indicate more complex models
* **Warning Signs**:
  - Rapid increase in p_loo with minor model changes
  - p_loo exceeding actual parameter count significantly

### Standard Error
Quantifies uncertainty in ELPD estimation:

* **Definition**: Measures reliability of ELPD estimate
* **Interpretation**:
  - Lower values indicate more reliable ELPD estimates
  - Compare relative to ELPD magnitude
* **Rule of Thumb**:
  - SE should be substantially smaller than ELPD
  - Large SE/ELPD ratio suggests unstable estimates

## Practical Example

Consider this model evaluation scenario:

```python
Model Evaluation Results:
------------------------
ELPD:  -245.32
p_loo:    12.45
SE:       8.67
```

### Analysis:
1. **ELPD Assessment**:
   - Negative value indicates scale of prediction error
   - Compare with simpler/more complex models

2. **Complexity Check**:
   - p_loo (12.45) suggests moderate complexity
   - Consider if complexity justified by improved predictions

3. **Reliability Analysis**:
   - SE (8.67) is relatively small compared to ELPD
   - Suggests stable predictive performance estimates

## Decision Framework

When evaluating models:

1. **Compare Multiple Models**:
   ```python
   Model A: ELPD=-245, p_loo=12, SE=8
   Model B: ELPD=-242, p_loo=18, SE=9
   Model C: ELPD=-248, p_loo=10, SE=7
   ```

2. **Consider Trade-offs**:
   * Predictive accuracy (ELPD)
   * Model complexity (p_loo)
   * Estimate reliability (SE)

3. **Select Based On**:
   * Business requirements
   * Data availability
   * Computational constraints

## Warning Signs

Watch for these potential issues:

1. **Overfitting Indicators**:
   * High p_loo relative to model parameters
   * Large gap between training and LOO performance

2. **Instability Signs**:
   * Large standard errors
   * Highly variable predictions
   * Sensitive to data changes

3. **Model Misspecification**:
   * Unexpectedly low ELPD
   * Inconsistent performance across subsets

## Best Practices

1. **Model Comparison**:
   * Compare similar model structures
   * Use consistent evaluation criteria
   * Document selection rationale

2. **Validation Strategy**:
   * Cross-validate where possible
   * Check prediction stability
   * Verify business relevance

3. **Documentation**:
   * Record metric values
   * Note selection criteria
   * Document assumptions

## Technical Implementation

```python
# Example model evaluation code
def evaluate_model(model):
    loo = az.loo(model.idata, pointwise=True)
    metrics = {
        'elpd': float(loo.elpd_loo),
        'p_loo': float(loo.p_loo),
        'se': float(loo.se)
    }
    return metrics
```


Reference: 
Vehtari, A., Gelman, A., & Gabry, J. (2017). Practical Bayesian model evaluation using leave-one-out cross-validation and WAIC. Statistics and Computing.
