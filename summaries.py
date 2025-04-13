

# We now want to define the functions that would create summaries

def company_summary(row):
    # Adjust column names as needed. This example assumes:
    # "Company", "Canton", "Year", "Industry"
    company = row.get("Title", "Unknown Company")
    canton = row.get("Canton", "Unknown Location")
    year = row.get("Year", "Unknown Year")
    industry = row.get("Industry", "an unknown industry")
    city = row.get("City", "an unknown city")
  
    summary = f"Company {company} is based in {city}, {canton}, was founded in {year}, and operates in the {industry} sector."
    return summary

def deals_summary(row):
    # Adjust column names as needed. This example assumes:
    # "Company", "Deal Date", "Deal Type", "Deal Amount"
    company = row.get("Company", "Unknown Company")
    deal_date = row.get("Date of the funding round", "an unknown date")
    deal_type = row.get("Type", "an unknown deal type")
    deal_amount = row.get("Amount", "an unknown/confidential amount")
    deal_investor = row.get("Investors","an unknown investor")
    deal_valuation = row.get("Valuation", "unknown valuation")
    deal_gender = row.get("Gender CEO", "unknown")
    
    summary = f"On {deal_date}, {company} executed a {deal_type} funding of {deal_amount} millions from {deal_investor}, with a company valuation of {deal_valuation} at the time of the deal. The CEO's gender is {deal_gender}"
    return summary