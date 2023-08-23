import argparse
import os

import matplotlib.pyplot as plt
from gpx_converter import Converter


def convert_gpx_to_dataframe(gpx_file):
    """
    This function convert the gpx data to a dataframe.

    Arguments:
    gpx_file: file with gpx data.

    Return:
    dataframe: dataframe with the .gpx file data
    """

    dataframe = Converter(input_file=gpx_file).gpx_to_dataframe(
        lats_colname="latitude",
        longs_colname="longitude",
        times_colname="time",
        alts_colname="altitude",
    )

    return dataframe


def plot_dataframe(df):
    """
    Plot latitude and longitude from the dataframe

    Arguments:
    df: dataframe with the .gpx file data

    Plot latitude vs longitude
    """

    # Extract data
    longitude = df.longitude
    latitude = df.latitude

    # Plot
    plt.scatter(longitude, latitude)
    plt.plot(longitude, latitude, "r--")

    # Labels
    plt.title("Longitude vs Latitude")
    plt.xlabel("Latitude")
    plt.ylabel("Longitude")

    plt.grid()
    plt.show()


def get_comline_parser():
    parser = argparse.ArgumentParser(description="Search files")
    parser.add_argument(
        "--path", type=str, default=".", help="Path where found the files"
    )

    return parser


if __name__ == "__main__":
    args = get_comline_parser().parse_args()

    for file_ in os.listdir(args.path):
        name, extension = os.path.splitext(file_)

        if extension in [".gpx"]:
            gpx_file = name + extension
            print("I found the file {}".format(gpx_file))

            dataframe = convert_gpx_to_dataframe(gpx_file)

            plot_dataframe(dataframe)
