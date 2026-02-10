def transform_customers(df):
    df["First Name"] = df["First Name"].str.title()
    df["Last Name"] = df["Last Name"].str.title()
    df["Email"] = df["Email"].str.lower()
    df["Subscription Date"] = df["Subscription Date"].astype("datetime64[ns]")
    return df


def transform_products(df):
    df["Name"] = df["Name"].str.lower()
    df["Price"] = df["Price"].round(2)
    df["Availability"] = df["Availability"].str.lower()
    return df


def transform_organizations(df):
    df["Name"] = df["Name"].str.title()
    df["Founded"] = df["Founded"].astype(int)
    return df


def merge_datasets(customers, products, organizations):
    cust_org = customers.merge(
        organizations,
        left_on="Company",
        right_on="Name",
        how="left"
    )

    cust_org["key"] = 1
    products["key"] = 1

    final_df = cust_org.merge(products, on="key").drop(columns=["key"])
    return final_df