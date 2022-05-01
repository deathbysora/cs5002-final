import pandas
data = pandas.read_csv("data\\2019_LAX.csv")

sort_column = "FL_DATE"
data[sort_column] = pandas.to_datetime(data[sort_column])
data.sort_values(sort_column, inplace=True)

wanted = ["FL_DATE",
          "OP_CARRIER_AIRLINE_ID",
          "OP_CARRIER_FL_NUM",
          "ORIGIN",
          "DEST",
          "DEP_TIME",
          "DEP_DELAY",
          "ARR_TIME",
          "ARR_DELAY"]
data.drop(
    columns=[column for column in data if not column in wanted], inplace=True)
data.to_csv("data\\2019_LAX_cleaned.csv", index=False)
