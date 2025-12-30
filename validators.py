import pandera.pandas as pa

SleepSchema = pa.DataFrameSchema(
    {
        "subject_id": pa.Column(int),
        "epoch_idx": pa.Column(int),
        "stage": pa.Column(
            str, checks=pa.Check.isin(["W", "N1", "N2", "N3", "REM", "MOVE", "NAN"])
        ),
        "delta_power": pa.Column(float, checks=pa.Check.ge(0)),
        "theta_power": pa.Column(float, checks=pa.Check.ge(0)),
        "alpha_power": pa.Column(float, checks=pa.Check.ge(0)),
        "sigma_power": pa.Column(float, checks=pa.Check.ge(0)),
        "beta_power": pa.Column(float, checks=pa.Check.ge(0)),
    }
)
