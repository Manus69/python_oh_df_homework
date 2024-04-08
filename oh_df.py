import pandas as pd
import random

def _get_vals(df: pd.DataFrame) -> list:
    val_set = set()

    for idx in range(len(df)):
        val_set.add(df.loc[idx].values[0])

    return list(val_set)

def _get_row(df: pd.DataFrame, df_row: int, vals: list) -> list:
    row = [0] * len(vals)

    try:
        idx = vals.index(df.loc[df_row].values[0])
        row[idx] = 1
    except:
        pass

    return row

def convert_to_one_hot(df: pd.DataFrame) -> pd.DataFrame:
    vals = _get_vals(df)
    oh_df = pd.DataFrame(columns=vals)

    for row_idx in range(len(df)):
        row = _get_row(df, row_idx, vals)
        oh_df.loc[len(oh_df)] = row

    return oh_df

def test():
    lst = ['robot'] * 10
    lst += ['human'] * 10
    random.shuffle(lst)
    data = pd.DataFrame({'whoAmI':lst})

    one_hot_df = convert_to_one_hot(data)
    print(one_hot_df)

if __name__ == "__main__":
    test()
    
