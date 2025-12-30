import pytest
import pandas as pd
from pandera.errors import SchemaError
from validators import SleepSchema


def test_valid_sleep_epoch():
    """
    Ensures data sample that meets constraints is successfully validated.
    """

    data = {
        "subject_id": [1],
        "epoch_idx": [100],
        "stage": ["N2"],
        "delta_power": [15.5],
        "theta_power": [14.2],
        "alpha_power": [8.0],
        "sigma_power": [1.2],
        "beta_power": [2.5],
    }

    df = pd.DataFrame(data)
    validated_df = SleepSchema.validate(df)
    assert validated_df["subject_id"].iloc[0] == 1
    assert validated_df["stage"].iloc[0] == "N2"


def test_negative_power_validation():
    """
    Ensures Pandera schema raises a SchemaError when a negative power band is seen.
    """

    data = {
        "subject_id": [1],
        "epoch_idx": [100],
        "stage": ["W"],
        "delta_power": [-5.0],
        "theta_power": [14.2],
        "alpha_power": [8.0],
        "sigma_power": [1.2],
        "beta_power": [2.5],
    }

    df = pd.DataFrame(data)
    with pytest.raises(SchemaError) as excinfo:
        SleepSchema.validate(df)

    assert "Column 'delta_power' failed" in str(excinfo.value)
    assert "greater_than_or_equal_to(0)" in str(excinfo.value)


def test_invalid_stage_label():
    """
    Confirms that the sleep stage validation rejects unsupported sleep stage labels.
    """

    data = {
        "subject_id": [1],
        "epoch_idx": [100],
        "stage": ["SLEEPING"],
        "delta_power": [15.5],
        "theta_power": [14.2],
        "alpha_power": [8.0],
        "sigma_power": [1.2],
        "beta_power": [2.5],
    }

    df = pd.DataFrame(data)
    with pytest.raises(SchemaError):
        SleepSchema.validate(df)
