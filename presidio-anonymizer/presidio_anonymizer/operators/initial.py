from typing import Dict
from .operator import OperatorType
from presidio_anonymizer.operators import Operator


class Initial(Operator):
    def operate(self, text: str, params: Dict = None) -> str:
        return ""
    
    def validate(self, params: Dict = None) -> None:
        pass

    def operator_name(self) -> str:
        return "initial"
    
    def operator_type(self) -> OperatorType:
        return OperatorType.Anonymize