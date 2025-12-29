from typing import Optional, Protocol
import pandas as pd


class WarehouseClient(Protocol):
    """
    Interface for implementing warehouse-specific storage logic.
    """

    def load_epochs(self, df: pd.DataFrame, subject_id: int) -> None:
        """Loads subject-level sleep epoch data to the warehouse."""
        ...

    def log_ingestion_error(
        self,
        subject_id: int,
        error_type: str,
        error_message: str,
        stack_trace: Optional[str] = None,
    ) -> None:
        """Logs ingestion-related failures for observability."""
        ...
