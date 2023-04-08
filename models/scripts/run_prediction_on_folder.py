from pathlib import Path
from enum import Enum

import typer

from src.features.utils import get_absolute_path_to_project_location
from src.pipelines.prediction_processor import PredictionPipeline


class TypeOfWeightsToLoad(str, Enum):
    miou = "miou"
    loss = "loss"


def main(
    model_revision: str = typer.Option(
        default="deeplabv3plus_v5.10.2",
        help="Choose model revision for predictions",
    ),
    weights: TypeOfWeightsToLoad = typer.Option(
        default=TypeOfWeightsToLoad.miou,
        help="Pick which weights load",
        show_choices=True
    ),
    input_folder: Path = typer.Option(
        get_absolute_path_to_project_location("models/custom_data/input"),
        help='Default: "models/custom_data/input". '
        "Folder with input images (JPG/PNG/TIFF)",
        file_okay=False,
        dir_okay=True,
        show_default=False,
    ),
    output_folder: Path = typer.Option(
        default=get_absolute_path_to_project_location("models/custom_data/output"),
        help='Default: "models/custom_data/output". Output predictions will be saved here.',
        file_okay=False,
        dir_okay=True,
        show_default=False,
    ),
    clear_cache: bool = typer.Option(True),
) -> None:

    PredictionPipeline(
        model_revision=model_revision,
        input_folder=input_folder,
        output_folder=output_folder,
        which_metric_best_weights_to_load=weights
    ).process(clear_cache)


if __name__ == "__main__":
    typer.run(main)
