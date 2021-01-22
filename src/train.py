from sklearn import preprocessing
import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv(TRAINING_DATA)
    train_df = df[df['kfold'].isin(FOLD_MAPPING.get(FOLD))]
    valid_df = df[df['kfold'] == FOLD]
    
    