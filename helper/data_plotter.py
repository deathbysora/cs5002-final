import os
from typing import Any, Dict

import seaborn
from matplotlib import dates, pyplot
from matplotlib.axes import Axes
from pandas import DataFrame, to_datetime


class DataPlotter():

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
            palette = seaborn.color_palette("pastel")
            pyplot.pie(list(reasons.values()),
                       labels=list(reasons.keys()),
                       autopct="%.2f%%",
                       colors=palette)  # type: ignore
            pyplot.title(self.airport + " Delay Reasons")
            self._save_image("reasons_percentage")

        def chart_bar(reasons: Dict[str, int]):
            plot = seaborn.barplot(x=list(reasons.keys()),
                                   y=list(reasons.values()))
            plot.bar_label(plot.containers[0])
            plot.set_title(self.airport + " Delay Reasons")
            plot.set_ylabel("Count")
            plot.set_xlabel("Reasons")
            self._save_image("reasons_count")

        delay_counts = filter_reasons()
        chart_pie(delay_counts)
        pyplot.clf()
        chart_bar(delay_counts)

    def _filter_columns(self, header: str) -> DataFrame:
        return self.data.loc[:, [DataPlotter.YAXIS, header]]

    def _setup_plot(self, x_data: Any, dataframe: DataFrame) -> Axes:
        plot = seaborn.scatterplot(x=x_data,
                                   y=dataframe[DataPlotter.YAXIS],
                                   data=dataframe)
        plot.set_title(self.airport)
        plot.set_ylabel("Delay (in minutes)")

        min = -30
        max = 300
        tick = 30
        # percentile 0.05 > x <= 0.95
        # TODO this is quick visual fix. We need
        # to filter the data before this step.
        plot.set_yticks(range(min, max + tick, tick))
        plot.set_ylim(min, max + tick)

        return plot

    def _save_image(self, graph_parameter: str) -> None:
        DESTINATION = "graphs\\"

        paths = [
            DESTINATION,
            DESTINATION + "\\" + self.airport + "\\",
        ]

        for path in paths:
            if not os.path.isdir(path):
                os.mkdir(path)

        file_name = paths[1] + self.airport + "_" + graph_parameter + ".png"
        pyplot.savefig(file_name)
