def transform_sales(df):
    df = df.drop_duplicates()
    df = df.dropna()
    df["date"] = df["date"].astype(str)
    return df


def transform_products(df):
    df = df[["id", "title", "price", "category"]]
    df = df.rename(columns={"title": "product"})
    df = df.drop_duplicates()
    df = df.dropna()
    return df


def transform_employees(df):
    df = df.drop_duplicates()
    df = df.dropna()
    return df