def historgram(df, df2, column):    
    import pandas as pd
    import matplotlib.pyplot as plt 
    from matplotlib.ticker import StrMethodFormatter  
    
    df[column].hist(bins=25, grid=False, figsize=(12,8), color='#86bf91', zorder=2, rwidth=0.9, histtype='step') 
    df2[column].hist(bins=25, grid=False, figsize=(12,8), color='#8690bf', zorder=2, rwidth=0.9, histtype='step')   
    
    plt.xlabel(column) 
    plt.ylabel("Frequency")
    
    plt.legend(["BOY", "MOY"])