from extract import extract_customers, extract_products, extract_organizations
from transform import (
    transform_customers,
    transform_products,
    transform_organizations,
    merge_datasets
)
from load import load_to_csv


def run_pipeline():
    customers = extract_customers("data/customers-100.csv")
    products = extract_products("data/products-100.csv")
    organizations = extract_organizations("data/organizations-100.csv")

    customers = transform_customers(customers)
    products = transform_products(products)
    organizations = transform_organizations(organizations)

    final_df = merge_datasets(customers, products, organizations)

    load_to_csv(final_df, "clean_merged_data.csv")

    print("✅ ETL Pipeline completed successfully")


if __name__ == "__main__":
    run_pipeline()