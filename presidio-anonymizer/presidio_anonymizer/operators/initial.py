from typing import Dict
from .operator import OperatorType
from presidio_anonymizer.operators import Operator


class Initial(Operator):
    def operate(self, text: str, params: Dict = None) -> str:
        split_text = text.split()

        initials = ""
        for text in split_text:
            if text:
                initials += text[0].upper() + ". "

        initials = initials.strip()
        return initials

    def validate(self, params: Dict = None) -> None:
        pass

    def operator_name(self) -> str:
        return "initial"
    
    def operator_type(self) -> OperatorType:
        return OperatorType.Anonymize