#if price changes by x% then how much does the quantity change?
# tells us if i should increase the price or decrease the price to earn more money 

""" Demand simulation based on price elasticity estimates
Key assumptions:
1. The elasticity is constant across the price range (from the log-log model)
2. The relationship holds for the simulated price changes
3. Revenue = Price × Quantity (no additional costs or factors)
"""

import pandas as pd

def simulate_price_change(elasticity,price_change_pct):

    if not isinstance(elasticity,(int,float)) and isinstance(price_change_pct,(int,float)):
        raise TypeError("Elasticity and price_change_pct must be  numbers")

    #calculate quantity change
    quantity_change_pct= elasticity*price_change_pct
    return quantity_change_pct

def simulate_revenue_impact(current_price,current_quantity,elasticity,price_change_pct):

    #input validation 
    if current_price<=0:
        raise ValueError("Current price must be positive")
    if current_quantity<=0:
        raise ValueError("Current quantity muct be positive")
    if not isinstance(elasticity,(int,float)):
        raise TypeError("Elasticity must be a number")
    if not isinstance(price_change_pct,(int,float)):
        raise TypeError("Price change percentage must be number")
    
    #calculate new price
    new_price= current_price*(1+price_change_pct/100)

    #calculate new quantity using elasticity
    quantity_change_pct= simulate_price_change(elasticity,price_change_pct)
    new_quantity=current_quantity*(1+ quantity_change_pct/100)

    #calculate revenue
    current_revenue= current_price * current_quantity
    new_revenue= new_price * new_quantity
    revenue_change_pct=((new_revenue-current_revenue)/current_revenue)*100

    results={
        'current_price':current_price,
        'new_price':new_price,
        'price_change_pct':price_change_pct,
        'current_quantity': current_quantity,
        'new_quantity':new_quantity,
        'quantity_change_pct': quantity_change_pct,
        'current_revenue':current_revenue,
        'new_revenue':new_revenue,
        'revenue_change_pct':revenue_change_pct             
        }
    return results

def simulate_price_scenerios(current_price,current_quantity,elasticity,price_changes=None):
    #set defaultt price changes if not provided

    if price_changes is None:
        price_changes=[-20,-10,-5,5,10,20]
    
    #validate inputs 
    if not isinstance(price_changes,list):
        raise TypeError("Price changees must be a list")
    if len(price_changes)==0:
        raise ValueError("Price changes list cannot be empty")
    
    scenerios=[]

    for price_change in price_changes:
        result= simulate_revenue_impact(current_price,current_quantity,elasticity,price_change)

        scenerios.append(result)
    
    #return as dataframe for easy analysis
    df_scenerios=pd.DataFrame(scenerios)

    #reorder columns for better readability
    coulmn_order=[
        'price_change_pct','current_price','new_price',
        'current_quantity','new_quantity','quantity_change_pct',
        'current_revenue','new_revenue','revenue_change_pct'

    ]
    df_scenerios= df_scenerios[coulmn_order]

    return df_scenerios
