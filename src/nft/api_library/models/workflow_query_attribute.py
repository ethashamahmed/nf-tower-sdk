from enum import Enum


class WorkflowQueryAttribute(str, Enum):
    LABELS = "labels"
    OPTIMIZED = "optimized"

    def __str__(self) -> str:
        return str(self.value)
