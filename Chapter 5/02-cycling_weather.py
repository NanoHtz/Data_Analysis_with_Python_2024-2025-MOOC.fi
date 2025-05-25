#!/usr/bin/env python3

import pandas as pd


def split_date():
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    df.dropna(how="all", inplace=True)
    df.dropna(axis=1, how="all", inplace=True)

    date_column = df["Päivämäärä"]
    date_components = date_column.str.split(expand=True)
    date_components.columns = ["Weekday", "Day", "Month", "Year", "Hour"]

    weekdays = {
        "ma": "Mon",
        "ti": "Tue",
        "ke": "Wed",
        "to": "Thu",
        "pe": "Fri",
        "la": "Sat",
        "su": "Sun",
    }
    months = {
        "tammi": 1,
        "helmi": 2,
        "maalis": 3,
        "huhti": 4,
        "touko": 5,
        "kesä": 6,
        "heinä": 7,
        "elo": 8,
        "syys": 9,
        "loka": 10,
        "marras": 11,
        "joulu": 12,
    }

    date_components["Weekday"] = date_components["Weekday"].map(weekdays)
    date_components["Month"] = date_components["Month"].map(months).astype(int)
    date_components["Hour"] = date_components["Hour"].str[:2].astype(int)
    date_components["Day"] = date_components["Day"].astype(int)
    date_components["Year"] = date_components["Year"].astype(int)

    return (date_components, df)


def split_date_continues():
    date_components, df = split_date()
    df.dropna(how="all", inplace=True)
    df.dropna(axis=1, how="all", inplace=True)
    df.drop(["Päivämäärä"], axis=1, inplace=True)

    final = pd.concat([date_components, df], axis=1)
    return final


def cycling_weather():
    cycling_set = split_date_continues()
    weather_set = pd.read_csv("src/kumpula-weather-2017.csv", sep=",")
    merged_set = pd.merge(
        cycling_set,
        weather_set,
        left_on=["Year", "Month", "Day"],
        right_on=["Year", "m", "d"],
    )
    merged_set.drop(["m", "d", "Time", "Time zone"], axis=1, inplace=True)

    return merged_set


def main():
    cycling_weather()


if __name__ == "__main__":
    main()
