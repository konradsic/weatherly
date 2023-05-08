"""
MIT License

Copyright (c) 2023 Konrad (@konradsic)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
from typing import (
    Dict,
    Any,
    Optional
)

from .base import PartialAPIResponse

__all__ = (
    "AlertData",
)

class AlertData(PartialAPIResponse):
    """An alert from WeatherAPI

    Attributes
    -------------
    raw: Dict[:class:`str`, Any]
        Raw response in a JSON-like format (converted to a python dictionary)
    headline: :class:`str`
        Alert headline
    msg_type: :class:`str`
        Type of alert
    severity: :class:`str`
        Severity of alert
    urgency: :class:`str`
        Urgency
    areas: :class:`str`
        Areas covered
    category: :class:`str`
        Category
    certainty: :class:`str`
        Certainty
    event: :class:`str`
        Event
    note: :class:`str`
        Note
    effective: :class:`str`
        Effective
    expires: :class:`str`
        Expires
    description: :class:`str`
        Description
    instruction: :class:`str`
        Instruction
    """
    def __init__(
        self,
        raw: Dict[str, Any],
    ) -> None:
        super().__init__(raw)
        
        self.headline: str = raw["headline"]
        self.msg_type: str = raw["msgType"]
        self.severity: str = raw["severity"]
        self.urgency: str = raw["urgency"]
        self.areas: str = raw["areas"]
        self.category: str = raw["category"]
        self.certainty: str = raw["certainty"]
        self.event: str = raw["event"]
        self.note: str = raw["note"]
        self.effective: str = raw["effective"]
        self.expires: str = raw["expires"]
        self.description: str = raw["desc"]
        self.instruction: str = raw["instruction"]
