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
)

__all__ = (
    "PartialAPIResponse",
    "APIResponse",
)

class PartialAPIResponse():
    """Represents a partial response, or a part of a response class from WeatherAPI
    
    Attributes
    ------------
    raw: Dict[:class:`str`, Any]
        A raw dictionary representing the partial response body
    """
    def __init__(self, raw: Dict[str, Any]) -> None:
        self.raw: Dict[str, Any] = raw

    def flatten(self) -> Dict[str, str]:
        """Converts a Dict[:class:`str`, Any] into a flatten dictionary of type Dict[:class:`str`, :class:`str`]
        
        For example, given a dictionary 
        
        .. code:: javascript
        
            {
                "body": {
                    "tag": "p", 
                    "content": {
                        "yes": "no"
                    }
                }, 
                "other": {
                    "one": "two", 
                    "three": "four"
                }
            }

        It will be turned into

        .. code:: javascript

            {
                "body.tag": "p",
                "body.content.yes": "no",
                "other.one": "two",
                "other.three": "four"
            }
        
        .. note::

            This function **does not** use recursion, so there won't be any stack problems with long nested dictionaries
        """
        cur = self.raw
        res = {}

        queue = [(cur, "")]
        # we use stack strat for performance and to avoid recursion
        while queue:
            # iterate over k,v in item
            elem = queue.pop(0)
            key = str(elem[1])
            print(queue)
            d = elem[0]
            for k,v in d.items():
                k = str(k)
                if isinstance(v, dict):
                    queue = [((v, key + "." + k if key else k))] + queue # idx: front
                else:
                    res[key + "." + k if k else k] = v
        return res

class APIResponse(PartialAPIResponse):
    """Represents a basic response from Weather API. Inherits from :class:`PartialAPIResponse`.
    
    Attributes
    ----------
    raw: Dict[:class:`str`, Any]
        Raw response in a JSON-like format (converted to a python dictionary)
    status: :class:`int`
        HTTP status of the response. 200 is OK, and is the most common status
    code: Optional[:class:`int`]
        Response code. In some cases this can be ``None``
    """
    def __init__(
        self,
        raw: Dict[str, Any],
        status: int,
        code: Optional[int]
    ) -> None:
        self.raw: Dict[str, Any] = raw
        self.status: int = status
        self.code: Optional[int] = code