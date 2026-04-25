import pandas as pd

def rename_columns(df: pd.DataFrame) -> pd.DataFrame:
    #Rename columns sesuai standar project

    return df.rename(columns={
        "fullName": "fullname",
        "biography": "bio",
        "followersCount": "#followers",
        "followsCount": "#follows",
        "postsCount": "#posts",
        "profilePicUrl": "profile_pic"
    })


def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    
    # Handle missing values sesuai rule:
    # - username: drop
    # - fullname: '-'
    # - bio: '-'
    # - #followers, #follows, #posts, private: drop rows
    # - profile_pic: convert ke boolean (True jika ada, False jika tidak)
    # - verified: isi dengan modus
    
    df = df.dropna(subset=["username"])

    
    df["fullname"] = df["fullname"].fillna("-")
    df["bio"] = df["bio"].fillna("-")

    
    df["profile_pic"] = df["profile_pic"].notna()

    
    df = df.dropna(subset=[
        "#followers", "#follows", "#posts", "private"
    ])

    
    if df["verified"].isnull().sum() > 0:
        mode_val = df["verified"].mode()[0]
        df["verified"] = df["verified"].fillna(mode_val)

    return df


def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    
    #Full preprocessing pipeline
    
    df = rename_columns(df)
    df = handle_missing_values(df)

    return df