from dataclasses import dataclass
from typing import NamedTuple

Ratio = NamedTuple("Ratio", [("A", float), ("B", float)])


@dataclass
class PDMSRatioCalculator:
    __weight_of_pdms_g: float = 10.0
    __weight_of_A_g: float = 0.0
    __weight_of_B_g: float = 0.0
    __ratio: Ratio = Ratio(10, 1)

    def __init__(
        self,
        weight_of_pdms_g: float = 10.0,
        A_ratio: float = 10.0,
        B_ratio: float = 1.0,
    ):
        ratio: Ratio = Ratio(A_ratio, B_ratio)
        self.__weight_of_pdms_g = weight_of_pdms_g
        self.__ratio = ratio
        self.__post_init__()

    def __post_init__(self):
        self.__weight_of_A_g, self.__weight_of_B_g = self.calculate_weight(
            self.__weight_of_pdms_g, self.__ratio
        )

        print(
            f"For a weight of {self.__weight_of_pdms_g} g of PDMS with a ratio of {self.__ratio.A:.2f}:{self.__ratio.B:.2f} the weights of A and B are:"
        )

    @staticmethod
    def calculate_weight(total_weight: float, ratio: Ratio) -> tuple[float, float]:
        divisor: float = 1 / (ratio.A + ratio.B)

        weight_of_A_g: float = total_weight * ratio.A * divisor
        weight_of_B_g: float = total_weight * ratio.B * divisor

        return weight_of_A_g, weight_of_B_g

    def print_weights(self):
        print(f"Weight of A: {self.__weight_of_A_g:.2f} g")
        print(f"Weight of B: {self.__weight_of_B_g:.2f} g")
