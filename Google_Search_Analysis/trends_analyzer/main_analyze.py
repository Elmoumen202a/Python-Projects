# import pandas as pd
from pytrends.request import TrendReq

def analyze_trends():
    # Set up pytrends
    trends = TrendReq(hl='en-US', tz=360)
    
    # Build payload and retrieve data
    trends.build_payload(kw_list=["Machine Learning"])
    data = trends.interest_by_region()
    
    # Sort data and get top 10 regions
    data = data.sort_values(by="Machine Learning", ascending=False)
    top_regions = data.head(10)
    
    return top_regions

if __name__ == "__main__":
    # Example usage
    trends_data = analyze_trends()
    print(trends_data)
