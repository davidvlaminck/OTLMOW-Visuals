from otlmow_model.OtlmowModel.Classes.Onderdeel.Aftakking import Aftakking

from otlmow_visuals.PyVisWrapper import remove_duplicates_in_iterable_based_on_asset_id


def test_remove_duplicates_in_iterable_based_on_asset_id():
    a = Aftakking()
    a.assetId.identificator = '1'
    b = Aftakking()
    b.assetId.identificator = '1'
    assets = [a, b]
    assets = remove_duplicates_in_iterable_based_on_asset_id(assets)
    assert len(assets) == 1