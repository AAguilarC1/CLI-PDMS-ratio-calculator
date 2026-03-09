from dataclasses import dataclass
from typing import NamedTuple
from enum import StrEnum

Ratio = NamedTuple("Ratio", [("A", float), ("B", float)])


class MassOrVolume(StrEnum):
    MASS = "MASS"
    VOLUME = "VOLUME"


@dataclass
class PDMSRatioCalculator:
    __mass_or_volume: MassOrVolume = MassOrVolume.MASS
    __ratio: Ratio = Ratio(10, 1)

    __amount_of_pdms_unit: float = 10.0
    __amount_of_A_unit: float = 0.0
    __amount_of_B_unit: float = 0.0

    def __init__(
        self,
        amount_of_pdms_unit: float = 10.0,
        A_ratio: float = 10.0,
        B_ratio: float = 1.0,
        mass_or_volume: str = "MASS",
    ):
        ratio: Ratio = Ratio(A_ratio, B_ratio)
        self.__amount_of_pdms_unit = amount_of_pdms_unit
        self.__ratio = ratio
        self.__mass_or_volume = MassOrVolume(mass_or_volume)
        self.__post_init__()

    def __post_init__(self):
        self.__amount_of_A_unit, self.__amount_of_B_unit = self.calculate_ratio(
            self.__amount_of_pdms_unit, self.__ratio
        )

    @staticmethod
    def calculate_ratio(total_amount: float, ratio: Ratio) -> tuple[float, float]:
        divisor: float = 1 / (ratio.A + ratio.B)

        amount_of_A: float = total_amount * ratio.A * divisor
        amount_of_B: float = total_amount * ratio.B * divisor

        return amount_of_A, amount_of_B

    def print_amounts(self):
        unit: str = "g" if self.__mass_or_volume == MassOrVolume.MASS else "mL"

        print(
            f"For a {self.__mass_or_volume.value} of {self.__amount_of_pdms_unit} {unit} of PDMS with a ratio of {self.__ratio.A:.2f}:{self.__ratio.B:.2f} the amounts of A and B are:"
        )

        print(f"Amount of A: {self.__amount_of_A_unit:.2f} {unit}")
        print(f"Amount of B: {self.__amount_of_B_unit:.2f} {unit}")
