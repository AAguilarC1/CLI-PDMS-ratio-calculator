from .ratio import PDMSRatioCalculator
import typer
import re 
from typing import Annotated

def __get_mass_or_volume(mass_or_volume: str) -> str:
    
    def truncate_string(s: str, length: int) -> str:
        return s[:length]
    
    mass_or_volume = truncate_string(mass_or_volume.upper(), 10)

    rule = re.compile(r"^(M(ASS)?|V(OLUME)?)$")
    match = rule.match(mass_or_volume)
    if not match:
        raise ValueError("Invalid input for the mass or volume type. Must be M[ass] or V[olume]")
   
    if match[0].startswith("M"):
        return "MASS"
    else:
        return "VOLUME"

def calculate_ratio(
    amount_of_pdms: Annotated[
        float, typer.Argument(help="Expected amount of PDMS in grams or milliliters")
    ] = 10.0,
    MassOrVolume: Annotated[
        str, typer.Option(help="Calculate based on M[ass] or V[olume] (case insensitive)", show_default=True)
    ] = "Mass",
    A_ratio: Annotated[float, typer.Option(help="Ratio of component A")] = 10.0,
    B_ratio: Annotated[float, typer.Option(help="Ratio of component B")] = 1.0,
) -> None:

    _MassOrVolume: str = __get_mass_or_volume(MassOrVolume)

    if amount_of_pdms <= 0:
        raise ValueError("Amount of PDMS must be greater than zero.")

    if A_ratio <= 0 or B_ratio <= 0:
        raise ValueError("Ratios must be greater than zero.")
    
    if _MassOrVolume not in ("MASS", "VOLUME"):
        raise ValueError("Invalid mass or volume type.")


    ratio = PDMSRatioCalculator(
        amount_of_pdms_unit=amount_of_pdms,
        A_ratio=A_ratio,
        B_ratio=B_ratio,
        mass_or_volume=_MassOrVolume,
    )

    ratio.print_amounts()
