import re
from typing import Any, Dict
from matplotlib.axes import Axes
from pandas import DataFrame, read_csv, to_datetime
from matplotlib import pyplot, dates
import seaborn
import os

PATH = "data\\cities\\"
DESTINATION = "graphs\\"
ROUND_AMOUNT = 2

# def graph(data: DataFrame):
#     x = data["FL_DATE"]
#     y = data["ARR_DELAY"]

#     pyplot.gca().xaxis.set_major_formatter(dates.DateFormatter("%B"))
#     pyplot.gca().xaxis.set_major_locator(dates.MonthLocator())
#     # pyplot.yticks(range(-15, 121, 15))
#     # pyplot.ylim([-15, 120])
#     pyplot.plot_date(x, y)
#     pyplot.gcf().autofmt_xdate()

#     pyplot.title("2019 Delay Times")
#     pyplot.xlabel("2019")
#     pyplot.ylabel("Delay (in minutes)")

#     pyplot.show()


class GraphAirport():

    YAXIS = "DEP_DELAY"

    def __init__(self, airport: str, data: DataFrame):
        self.airport = airport
        self.data = data

    def run(self) -> None:
        operations = [
            self._graph_date,
            self._graph_departure_time,
            self._graph_delay_reason,
        ]

        for operation in operations:
            operation()
            pyplot.clf()

    def _graph_date(self) -> None:
        header = "FL_DATE"
        data = self._filter_columns(header)
        data[header] = to_datetime(data[header])
        data = data.sort_values(header)

        plot = self._setup_plot(data[header], data)
        plot.set_xlabel("Date")
        pyplot.gca().xaxis.set_major_formatter(dates.DateFormatter("%b"))
        pyplot.gca().xaxis.set_major_locator(dates.MonthLocator())
        pyplot.gcf().autofmt_xdate()
        self._save_image("date")

    def _graph_departure_time(self) -> None:
        header = "DEP_TIME"
        data = self._filter_columns(header)
        data[header] = to_datetime(data[header])
        data = data.sort_values(header)

        plot = self._setup_plot(self.data[header], data)
        plot.set_xlabel("Departure Time")
        self._save_image("departuretime")

    def _graph_delay_reason(self) -> None:

        def filter_reasons() -> Dict[str, int]:
            headers = [
                "CARRIER_DELAY",
                "WEATHER_DELAY",
                "NAS_DELAY",
                "SECURITY_DELAY",
                "LATE_AIRCRAFT_DELAY",
            ]

            total_length = len(self.data)
            result: Dict[str, int] = {}
            for header in headers:
                data = self.data[self.data[header] > 0]
                formatted_header = header
                formatted_header = formatted_header.replace("_DELAY", "")
                formatted_header = formatted_header.replace("_", " ")
                formatted_header = formatted_header.title()
                result[formatted_header] = len(data)

            result["None"] = total_length - \
                sum([number for number in result.values()])

            return result

        def chart_pie(reasons: Dict[str, int]):
            pyplot.pie(list(reasons.values()), labels=list(
                reasons.keys()), autopct="%.2f%%", colors=seaborn.color_palette("pastel"))
            pyplot.title(self.airport + " Delay Reasons")
            self._save_image("reasons_percentage")

        def chart_bar(reasons: Dict[str, int]):
            plot = seaborn.barplot(
                x=list(reasons.keys()), y=list(reasons.values()))
            plot.set_title(self.airport + " Delay Reasons")
            plot.set_ylabel("Count")
            plot.set_xlabel("Reasons")
            self._save_image("reasons_count")

        delay_counts = filter_reasons()
        chart_pie(delay_counts)
        pyplot.clf()
        chart_bar(delay_counts)

    def _filter_columns(self, header: str) -> DataFrame:
        return self.data.loc[:, [GraphAirport.YAXIS, header]]

    def _setup_plot(self, x_data: Any, dataframe: DataFrame) -> Axes:
        plot = seaborn.scatterplot(
            x=x_data, y=dataframe[GraphAirport.YAXIS], data=dataframe)
        plot.set_title(self.airport)
        plot.set_ylabel("Delay (in minutes)")
        return plot

    def _save_image(self, graph_parameter: str) -> None:
        paths = [
            DESTINATION,
            DESTINATION + "\\" + self.airport + "\\",
        ]

        for path in paths:
            if not os.path.isdir(path):
                os.mkdir(path)

        pyplot.savefig(paths[1] + self.airport +
                       "_" + graph_parameter + ".png")


def main() -> None:
    for file_name in os.listdir(PATH):
        print(f"beginning operation on {file_name}")
        airport = re.findall(r"[A-Z]{3}", file_name)[0]
        handler = GraphAirport(airport, read_csv(PATH + file_name))
        handler.run()


if __name__ == "__main__":
    main()
