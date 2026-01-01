# measure the price elasticity of demand 
# if price increases by x% then how much does the quantity change?
# price -increase 1%, quantity-decrease 2%, elasitcity=-2
""" price elasticity modeling using log-log regression
    uses statsmodels OLS to estimate elasticity coefficient
    
     Key Assumptions:
      1. The relationship between price and quantity follows power law
      2. power law: Quantity doesnt change linearly, it changes with percentage
       3. This becomes linear in log-log space: log(Q)=b0 +b1*log(P) +e
       4. fit through OLS- ordinary least squares is used to find the best straight line
       4. b1- price elasticity of demand,b0- intercept , e- noise """

import statsmodels.api as sm
import numpy as np

def fit_elasticity_model(df):
    #validate required columns
    required_cols=['price','quantity']
    missing_cols=[cols for cols in required_cols if cols not in df.columns]
    if missing_cols:
        return KeyError(f"Missing required columns:{missing_cols}")
    
    if(df['price']<=0).any() or (df['quantity']<=0).any():
        return ValueError("No valid data: all prices or quantities are zero or negative")
    
    #log transformations for elasticity estimation
    log_price= np.log(df['price'])
    log_quantity=np.log(df['quantity'])

    #add constant term for intercept
    X= sm.add_constant(log_price,prepend=True)
    Y= log_quantity
    #fit OLS model
    model= sm.OLS(Y,X).fit()

    return model

#this fucntion extracts elasticity b1 from the model
def get_elasticity(model):
    params_names= model.params.index.tolist()
    price_names=None
    for name in params_names:
        if name not in ['const','Intercept']:
            price_names=name
            break
    
    if price_names is None:
        raise KeyError("Could not find price coefficient in model parameters")
    
  
    elasticity= model.params[price_names]
    return elasticity 

def get_model_summary(model):
    #find the price parameter name
    params_names= model.params.index.tolist()
    elasticity=get_elasticity(model)
        
    # get the model summary
    summary={
        'elasticity':elasticity,
        'r_squared': model.rsquared,
        'adj_r_squared': model.rsquared_adj,
        'p_values':model.pvalues[params_names],
        'std_errors': model.bse[params_names],
        'n_observations':int(model.nobs)
    }
    return summary





