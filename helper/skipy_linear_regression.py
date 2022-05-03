import pandas
from scipy import stats


def linear_regression(data: pandas.DataFrame):

    def do(x):
        return slope * x + intercept

    airports = data["ORIGIN"].unique()
    for airport in airports:
        filtered = data[data["ORIGIN"] == airport]
        x = filtered["FL_DATE"].to_list()
        y = filtered["DEP_DELAY"].to_list()

        slope, intercept, r, p, std_err = stats.linregress(x, y)
        print(airport)
        print("Slope:", slope)
        print("Intercept:", intercept)
        print("R:", r)
        print("P", p)
        print("std error:", std_err)
        print()

        mymodel = list(map(do, x))

        pyplot.scatter(x, y)
        pyplot.plot(x, mymodel)
        pyplot.show()
        pyplot.clf()
