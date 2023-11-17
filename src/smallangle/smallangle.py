import click
import numpy as np
import pandas as pd
from numpy import pi


# define command group
@click.group()
def cmd_group():
    pass


# sin command
@cmd_group.command()
@click.option(
    "-n",
    "--number",
    default=10,
    help="Number of evenly spaced steps between 0 and 2 pi",
    show_default=True,  # show default in help
)
def sin(number):
    """Dataframe of sine values

    Args:
        number (int): number of evenly spaced steps between 0 and 2 pi
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)
    return


# tan command
@cmd_group.command()
@click.option(
    "-n",
    "--number",
    default=10,
    help="Number of evenly steps between 0 and 2 pi",
    show_default=True,  # show default in help
)
def tan(number):
    """Dataframe of tangent values

    Args:
        number (int): number of evenly spaced steps between 0 and 2 pi
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)
    return


if __name__ == "__main__":
    cmd_group()
