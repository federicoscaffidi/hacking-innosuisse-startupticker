import pandas as pd
from translator import get_text_from_url
from googletrans import Translator
from summaries import company_summary, deals_summary

def make_df():
    
    # Import excels and read them as dfs
    df_companies = pd.read_excel("Data-startupticker.xlsx", sheet_name="Companies")
    df_deals = pd.read_excel("Data-startupticker.xlsx", sheet_name="Deals")
    #print(df_companies.head())

    # Rename column in df_companies for matching purposes
    df_companies.rename(columns={'Title': 'Company'}, inplace=True)

    # Clean up data
    df_deals["Date of the funding round"] = pd.to_datetime(df_deals["Date of the funding round"], errors="coerce")
    df_deals["Date of the funding round"] = df_deals["Date of the funding round"].dt.strftime('%Y-%m-%d')

    for col in df_companies.columns.tolist():
        df_companies[col] = df_companies[col].fillna("")

    for col in df_deals.columns.tolist():
        df_deals[col] = df_deals[col].fillna("")

    # Reduce dataframe
    df_deals_reduced = df_deals.iloc[:10, :]

    # Add articles
    df_deals_reduced['Article Summary'] = df_deals_reduced['URL'].apply(get_text_from_url)

    # Update dataframe
    df_deals['Article Summary'] = df_deals_reduced['Article Summary']
    
    # Use only if df_deals is already present
    # df_deals = pd.read_csv("df_deals.csv")

    # Integrate the dataframes with the summary columns
    df_companies["nl_summary_info"] = df_companies.apply(company_summary, axis=1)
    df_deals["nl_summary_deals"] = df_deals.apply(deals_summary, axis=1)

    # Merge dataframes
    aggregated_deals_df = df_deals.groupby("Company").agg({
        "Article Summary": lambda x: " ".join(x.dropna().astype(str)),
        "nl_summary_deals": lambda x: " ".join(x.dropna().astype(str))
    }).reset_index()
    merged_df = df_companies.merge(aggregated_deals_df, on="Company", how="left")
    
    # Clean dataframe
    for col in merged_df.columns.tolist():
        merged_df[col] = merged_df[col].fillna("")
    
    # Remove last two rows
    merged_df = merged_df.iloc[:5213, :]

    return merged_df
