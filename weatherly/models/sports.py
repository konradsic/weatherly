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
    Optional,
    List
)

from .base import APIResponse, PartialAPIResponse
from ..enums import SportsEventType

__all__ = (
    "SportsEvent",
    "SportsData",
)

class SportsEvent(PartialAPIResponse):
    """Represents a single sports event from the Sports API

    Attributes
    ---------------
    raw: Dict[:class:`str`, Any]
        Raw response in a JSON-like format (converted to a python dictionary)
    stadium: :class:`str`
        Name of stadium
    country: :class:`str`
        Country
    region: :class:`str`
        Region
    tournament: :class:`str`
        Tournament name
    start_time: :class:`str`
        Start local date and time for event in yyyy-MM-dd HH:mm format
    match: :class:`str` 
        Match name
    event_type: :class:`SportsEventType`
        An enum representing the type of event. Can be "golf", football" or "cricket"
    """
    def __init__(
        self, 
        raw: Dict[str, Any], 
        event_type: SportsEventType
    ) -> None:
        super().__init__(raw)
        self.event_type = event_type
        self.stadium = raw["stadium"]
        self.country = raw["country"]
        self.region = raw["region"]
        self.tournament = raw["tournament"]
        self.start_time = raw["start"]
        self.match = raw["match"]

class SportsData(APIResponse):
    """Represents sports data returned from the Sports API

    Attributes
    -------------
    raw: Dict[:class:`str`, Any]
        Raw response in a JSON-like format (converted to a python dictionary)
    status: :class:`int`
        HTTP status of the response. 200 is OK, and is the most common status.
    code: Optional[:class:`int`]
        Response code. In some cases this can be ``None``
    events: List[:class:`SportsEvent`]
        A list of sports 
    categorized: Dict[str, List[:class:`SportsEvent`]]
        Dictionary of events, that are same as in :py:attr:`~events`, but categorized. 
        Category is the key, and value is a list of :class:`SportsEvent`.
    """
    def __init__(
        self,
        raw: Dict[str, Any],
        status: int,
        code: Optional[int]
    ) -> None:
        super().__init__(raw, status, code)

        self.events: List[SportsEvent] = []
        self.categorized: Dict[str, List[SportsEvent]] = {"football": [], "golf": [], "cricket": []}
        for fball in raw["football"]:
            obj = SportsEvent(fball, SportsEventType.football)
            self.events.append(obj)
            self.categorized["football"].append(obj)

        for golf in raw["golf"]:
            obj = SportsEvent(golf, SportsEventType.golf)
            self.events.append(obj)
            self.categorized["golf"].append(obj)
        
        for cricket in raw["cricket"]:
            obj = SportsEvent(cricket, SportsEventType.cricket)
            self.events.append(obj)
            self.categorized["cricket"].append(obj)
