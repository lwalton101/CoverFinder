from enum import Enum


class JsonNodeNodeType(str, Enum):
    ARRAY = "ARRAY"
    BINARY = "BINARY"
    BOOLEAN = "BOOLEAN"
    MISSING = "MISSING"
    NULL = "NULL"
    NUMBER = "NUMBER"
    OBJECT = "OBJECT"
    POJO = "POJO"
    STRING = "STRING"

    def __str__(self) -> str:
        return str(self.value)
