import pandas as pd


def extract_customers(path):
    return pd.read_csv(path)


def extract_products(path):
    return pd.read_csv(path)


def extract_organizations(path):
    return pd.read_csv(path)