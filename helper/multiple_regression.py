import pandas
from matplotlib import pyplot
from scipy import stats
from sklearn import linear_model


def multiple_regression(data: pandas.DataFrame):
    xkeys = [
        "FL_DATE",
        "DEP_TIME",
    ]
    ykey = "DEP_DELAY"

    print(*xkeys)
    airports = data["ORIGIN"].unique()
    for airport in airports:
        filtered = data[data["ORIGIN"] == airport]
        x = filtered[xkeys]
        y = filtered[ykey]
        regression = linear_model.LinearRegression()
        regression.fit(x, y)

        print(airport)
        print(regression.coef_)
        # date: 20190401
        # time: 1457
        print(regression.predict([[403, 1520]]))
        print()


def main():
    path = "data\\date_formatted.csv"
    with open(path, "r") as file:
        data = pandas.read_csv(file)
        data["FL_DATE"] = data["FL_DATE"].apply(lambda x: x - 20190000)
        # data = data[data["DEP_DELAY"] >= 0]
    linear_regression(data)


if __name__ == "__main__":
    main()
