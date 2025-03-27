from pathlib import Path

from otlmow_converter.OtlmowConverter import OtlmowConverter
from otlmow_model.OtlmowModel.Classes.Onderdeel.Bevestiging import Bevestiging
from otlmow_model.OtlmowModel.Classes.Onderdeel.Verkeersregelaar import Verkeersregelaar
from otlmow_model.OtlmowModel.Classes.Onderdeel.Wegkantkast import Wegkantkast
from otlmow_model.OtlmowModel.Helpers.RelationCreator import create_relation

from otlmow_visuals.PyVisWrapper import PyVisWrapper

if __name__ == '__main__':


    assets = OtlmowConverter.from_file_to_objects(Path('DA-2025-21973_export.xlsx'))

    PyVisWrapper().show(assets, launch_html=False)
