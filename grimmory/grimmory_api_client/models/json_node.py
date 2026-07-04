from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.json_node_node_type import JsonNodeNodeType
from ..types import UNSET, Unset

T = TypeVar("T", bound="JsonNode")


@_attrs_define
class JsonNode:
    """Authentication request body

    Attributes:
        empty (bool | Unset):
        array (bool | Unset):
        null (bool | Unset):
        object_ (bool | Unset):
        float_ (bool | Unset):
        value_node (bool | Unset):
        container (bool | Unset):
        missing_node (bool | Unset):
        node_type (JsonNodeNodeType | Unset):
        string (bool | Unset):
        integral_number (bool | Unset):
        pojo (bool | Unset):
        floating_point_number (bool | Unset):
        short (bool | Unset):
        int_ (bool | Unset):
        long (bool | Unset):
        double (bool | Unset):
        big_decimal (bool | Unset):
        big_integer (bool | Unset):
        textual (bool | Unset):
        boolean (bool | Unset):
        binary (bool | Unset):
        number (bool | Unset):
        embedded_value (bool | Unset):
    """

    empty: bool | Unset = UNSET
    array: bool | Unset = UNSET
    null: bool | Unset = UNSET
    object_: bool | Unset = UNSET
    float_: bool | Unset = UNSET
    value_node: bool | Unset = UNSET
    container: bool | Unset = UNSET
    missing_node: bool | Unset = UNSET
    node_type: JsonNodeNodeType | Unset = UNSET
    string: bool | Unset = UNSET
    integral_number: bool | Unset = UNSET
    pojo: bool | Unset = UNSET
    floating_point_number: bool | Unset = UNSET
    short: bool | Unset = UNSET
    int_: bool | Unset = UNSET
    long: bool | Unset = UNSET
    double: bool | Unset = UNSET
    big_decimal: bool | Unset = UNSET
    big_integer: bool | Unset = UNSET
    textual: bool | Unset = UNSET
    boolean: bool | Unset = UNSET
    binary: bool | Unset = UNSET
    number: bool | Unset = UNSET
    embedded_value: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        empty = self.empty

        array = self.array

        null = self.null

        object_ = self.object_

        float_ = self.float_

        value_node = self.value_node

        container = self.container

        missing_node = self.missing_node

        node_type: str | Unset = UNSET
        if not isinstance(self.node_type, Unset):
            node_type = self.node_type.value

        string = self.string

        integral_number = self.integral_number

        pojo = self.pojo

        floating_point_number = self.floating_point_number

        short = self.short

        int_ = self.int_

        long = self.long

        double = self.double

        big_decimal = self.big_decimal

        big_integer = self.big_integer

        textual = self.textual

        boolean = self.boolean

        binary = self.binary

        number = self.number

        embedded_value = self.embedded_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if empty is not UNSET:
            field_dict["empty"] = empty
        if array is not UNSET:
            field_dict["array"] = array
        if null is not UNSET:
            field_dict["null"] = null
        if object_ is not UNSET:
            field_dict["object"] = object_
        if float_ is not UNSET:
            field_dict["float"] = float_
        if value_node is not UNSET:
            field_dict["valueNode"] = value_node
        if container is not UNSET:
            field_dict["container"] = container
        if missing_node is not UNSET:
            field_dict["missingNode"] = missing_node
        if node_type is not UNSET:
            field_dict["nodeType"] = node_type
        if string is not UNSET:
            field_dict["string"] = string
        if integral_number is not UNSET:
            field_dict["integralNumber"] = integral_number
        if pojo is not UNSET:
            field_dict["pojo"] = pojo
        if floating_point_number is not UNSET:
            field_dict["floatingPointNumber"] = floating_point_number
        if short is not UNSET:
            field_dict["short"] = short
        if int_ is not UNSET:
            field_dict["int"] = int_
        if long is not UNSET:
            field_dict["long"] = long
        if double is not UNSET:
            field_dict["double"] = double
        if big_decimal is not UNSET:
            field_dict["bigDecimal"] = big_decimal
        if big_integer is not UNSET:
            field_dict["bigInteger"] = big_integer
        if textual is not UNSET:
            field_dict["textual"] = textual
        if boolean is not UNSET:
            field_dict["boolean"] = boolean
        if binary is not UNSET:
            field_dict["binary"] = binary
        if number is not UNSET:
            field_dict["number"] = number
        if embedded_value is not UNSET:
            field_dict["embeddedValue"] = embedded_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        empty = d.pop("empty", UNSET)

        array = d.pop("array", UNSET)

        null = d.pop("null", UNSET)

        object_ = d.pop("object", UNSET)

        float_ = d.pop("float", UNSET)

        value_node = d.pop("valueNode", UNSET)

        container = d.pop("container", UNSET)

        missing_node = d.pop("missingNode", UNSET)

        _node_type = d.pop("nodeType", UNSET)
        node_type: JsonNodeNodeType | Unset
        if isinstance(_node_type, Unset):
            node_type = UNSET
        else:
            node_type = JsonNodeNodeType(_node_type)

        string = d.pop("string", UNSET)

        integral_number = d.pop("integralNumber", UNSET)

        pojo = d.pop("pojo", UNSET)

        floating_point_number = d.pop("floatingPointNumber", UNSET)

        short = d.pop("short", UNSET)

        int_ = d.pop("int", UNSET)

        long = d.pop("long", UNSET)

        double = d.pop("double", UNSET)

        big_decimal = d.pop("bigDecimal", UNSET)

        big_integer = d.pop("bigInteger", UNSET)

        textual = d.pop("textual", UNSET)

        boolean = d.pop("boolean", UNSET)

        binary = d.pop("binary", UNSET)

        number = d.pop("number", UNSET)

        embedded_value = d.pop("embeddedValue", UNSET)

        json_node = cls(
            empty=empty,
            array=array,
            null=null,
            object_=object_,
            float_=float_,
            value_node=value_node,
            container=container,
            missing_node=missing_node,
            node_type=node_type,
            string=string,
            integral_number=integral_number,
            pojo=pojo,
            floating_point_number=floating_point_number,
            short=short,
            int_=int_,
            long=long,
            double=double,
            big_decimal=big_decimal,
            big_integer=big_integer,
            textual=textual,
            boolean=boolean,
            binary=binary,
            number=number,
            embedded_value=embedded_value,
        )

        json_node.additional_properties = d
        return json_node

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
