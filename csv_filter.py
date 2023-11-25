import csv

with open("companies_export.csv", "r") as f:
    reader = csv.DictReader(f)

    companies = []  # create empty list to store matching companies

    for company in reader:
        # TODO  Check if current row/company column contains "BUYER"
        if "BUYER" in company["(COMPANY) LEAD CLASSIFICATION"]:
            if "real estate" in company["Description"] and "acquisition" in company["Description"]:
                companies.append(company)
    # what to do with this list?
    # 1. create a new csv file and loop through these companies and add to new csv file
    # GOOGLE: how to create a new csv file from a list of dictionaries
    print(companies)

    with open("re_acq_buyers_filtered.csv", "w", encoding='utf8', newline='') as x:
        keys = companies[0].keys()
        writer = csv.DictWriter(x, fieldnames=keys)
        writer.writeheader()
        for company in companies:
            writer.writerow(company)
