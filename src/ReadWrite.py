"""  Read Write Operations"""

# imports


# write to csv and visualization
# receives a dataframe and output paths
def writeAll(putputCsv, outputVisual, df):
        # print to csv
    df.to_csv(putputCsv, index=False)
    # print for visualization
    with open(outputVisual, 'w') as file:
        file.write(str(df))
