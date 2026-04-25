import pandas as pd
import numpy as np
import re


def _count_numbers(text: str) -> int:
    return len(re.findall(r"\d", text))


def add_username_ratio(df: pd.DataFrame) -> pd.DataFrame:
    
    #nums/length_username
    
    df["nums/length_username"] = df["username"].apply(
        lambda x: _count_numbers(x) / len(x) if len(x) > 0 else 0
    )
    return df


def add_fullname_features(df: pd.DataFrame) -> pd.DataFrame:
    
    #fullname_words & nums/length_fullname
    
    df["fullname_words"] = df["fullname"].apply(lambda x: len(str(x).split()))
    df["nums/length_fullname"] = df["fullname"].apply(
        lambda x: _count_numbers(x) / len(x) if len(x) > 0 else 0
    )
    return df


def add_name_comparison(df: pd.DataFrame) -> pd.DataFrame:
    
    #fullname==username
    
    df["fullname==username"] = df["fullname"] == df["username"]
    return df


def add_description_length(df: pd.DataFrame) -> pd.DataFrame:
    
    #description_length
    
    df["description_length"] = df["bio"].apply(lambda x: len(str(x)))
    return df


def reorder_columns(df: pd.DataFrame) -> pd.DataFrame:

    #Urutkan kolom sesuai requirement
    
    final_cols = [
        "profile_pic",
        "nums/length_username",
        "fullname_words",
        "nums/length_fullname",
        "fullname==username",
        "description_length",
        "verified",
        "private",
        "#posts",
        "#followers",
        "#follows"
    ]

    return df[final_cols]


def feature_engineering(df: pd.DataFrame) -> pd.DataFrame:
    
    #Full feature engineering pipeline
    
    df = add_username_ratio(df)
    df = add_fullname_features(df)
    df = add_name_comparison(df)
    df = add_description_length(df)

    df = reorder_columns(df)

    return df