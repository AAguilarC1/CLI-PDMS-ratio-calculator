from .ratio import PDMSRatioCalculator
import typer
from typing import Annotated


def calculate_ratio(
    weight_of_pdms_g: Annotated[
        float, typer.Argument(help="Expected weight of PDMS in grams")
    ] = 10.0,
    A_ratio: Annotated[float, typer.Option(help="Ratio of component A")] = 10.0,
    B_ratio: Annotated[float, typer.Option(help="Ratio of component B")] = 1.0,
) -> None:
    if weight_of_pdms_g <= 0:
        raise ValueError("Weight of PDMS must be greater than zero.")

    if A_ratio <= 0 or B_ratio <= 0:
        raise ValueError("Ratios must be greater than zero.")

    ratio = PDMSRatioCalculator(
        weight_of_pdms_g=weight_of_pdms_g,
        A_ratio=A_ratio,
        B_ratio=B_ratio,
    )

    ratio.print_weights()
