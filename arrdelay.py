import seaborn
from matplotlib import pyplot
from pandas import read_csv
from scipy import stats


def main():
    with open("data\\cities\\combined_v3.csv", "r") as file:
        data = read_csv(file)

    ykey = "DEP_DELAY"
    xkey = "ARR_DELAY"

    destination = "graphs\\"
    file_name = "".join([destination, ykey, "x", xkey])
    stream = open(file_name + ".txt", "w")
    stream.write(
        "data is linear regression model calculated from scipy for each airport\n")
    stream.write(f"y = {ykey}\n")
    stream.write(f"x = {xkey}\n")
    stream.write("\n")

    airports = data["ORIGIN"].unique()
    for airport in airports:
        filtered = data[data["ORIGIN"] == airport]
        y = filtered[ykey].to_list()
        x = filtered[xkey].to_list()

        slope, intercept, r, p, std_err = stats.linregress(x, y)
        results = {
            "count": len(filtered),
            "slope": slope,
            "intercept": intercept,
            "r": r,
            "p": p,
            "std error": std_err,
        }

        stream.write(airport + "\n")
        for key, value in results.items():
            stream.write(f"{key}: {value}\n")
        stream.write("\n\n")

        pyplot.figure(figsize=(11, 8))
        plot = seaborn.scatterplot(x=xkey, y=ykey, data=filtered)
        plot.set_title(airport + " 2019")

        pyplot.savefig(file_name + "_" + airport + ".png")
        pyplot.clf()


if __name__ == "__main__":
    main()
