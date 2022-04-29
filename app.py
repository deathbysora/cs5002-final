import pandas
from matplotlib import pyplot, dates


def quick_results(data: pandas.DataFrame) -> None:
    results = {
        "length": len(data),
        "minimum delay": data["DEP_DELAY"].min(),
        "max delay": data["DEP_DELAY"].max(),
    }

    for label, value in results.items():
        print(f"{label}: {value}")

    x = data[DATE_INDEX]
    y = data["DEP_DELAY"]


def main():
    DATE_INDEX = "FL_DATE"

    data = pandas.read_csv("data\\2019_AUS.csv")
    data[DATE_INDEX] = pandas.to_datetime(data[DATE_INDEX])
    data.sort_values(DATE_INDEX, inplace=True)

    quick_results(data)

    # Format graph.
    pyplot.gca().xaxis.set_major_formatter(dates.DateFormatter("%B"))
    pyplot.gca().xaxis.set_major_locator(dates.MonthLocator())
    pyplot.plot_date(x, y)
    pyplot.gcf().autofmt_xdate()

    pyplot.title("2019")
    pyplot.xlabel("Date")
    pyplot.ylabel("Delay (in minutes)")

    pyplot.show()


if __name__ == "__main__":
    main()
