from typing import Optional, Protocol
import pandas as pd


class WarehouseClient(Protocol):
    """
    A blueprint that all database clients must follow.
    This ensures our pipeline can talk to DuckDB, Snowflake, or any future database
    using the exact same methods.
    """

    def load_epochs(self, df: pd.DataFrame, subject_id: int) -> None:
        """Saves a batch of sleep data to the database."""
        ...

    def log_ingestion_error(
        self,
        subject_id: int,
        error_type: str,
        error_message: str,
        stack_trace: Optional[str] = None,
    ) -> None:
        """Saves error details to a table so we can debug them later."""
        ...
