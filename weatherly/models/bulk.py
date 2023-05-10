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
    Tuple,
    List
)

from .base import APIResponse
from ..enums import WeatherEndpoints

__all__ = (
    "BulkRequest",
    "BulkResponse",
)

class BulkRequest():
    """Represents a bulk request params
    
    Attributes
    -------------
    queries: List[Tuple[:class:`str`, :class:`str`]]
        Query data for the request
    endpoint: :class:`WeatherEndpoints`
        Enum representing the endpoint for the request
    """
    def __init__(self):
        self.queries: List = []
        self.endpoint: WeatherEndpoints = None # type: ignore
        
    def set_endpoint(self, endpoint: WeatherEndpoints) -> None:
        """Set the endpoint for the request
        
        Parameters
        -------------
        endpoint: :class:`WeatherEndpoints`
            Endpoint for the request as an enum
        """
        self.endpoint = endpoint
        
    def add_query(self, id: str, location: str) -> List[Tuple[str, str]]:
        """Add a query to the bulk request
        
        Parameters
        --------------
        id: :class:`str`
            Unique identifier for the query
        location: :class:`str`
            Location you want to fetch data from
        
        Returns
        ---------
        List[Tuple[:class:`str`, :class:`str`]]
            List of updated query parameters with the new query added
        """
        self.queries.append((str(id), str(location)))
        return self.queries
    
    @classmethod
    def build(cls, *queries: List[Tuple[str]], endpoint: WeatherEndpoints):
        """Build a bulk request
        
        .. note::
            This function is a class method i.e. does not require initialization. For example:
            
            .. code:: python
                
                import weatherly
                weatherly.BulkRequest.build(...) # <- no initialization needed (no parentheses after BulkRequest)
        
        Parameters
        ------------
        queries: List[Tuple[:class:`str`]]
            Query data for the request as a list of tuples (id, query)
        endpoint: :class:`WeatherEndpoints`
            Enum representing the endpoint for the request
        """
        bulk = cls()
        bulk.set_endpoint(endpoint)
        for query in queries:
            bulk.add_query(*query)
        return bulk

class BulkResponse(APIResponse):
    """Represents bulk request response data
    
    Attributes
    ------------
    raw: Dict[:class:`str`, Any]
        Raw response in a JSON-like format (converted to a python dictionary)
    status: :class:`int`
        HTTP status of the response. 200 is OK, and is the most common status.
    code: Optional[:class:`int`]
        Response code. In some cases this can be ``None``
    endpoint: :class:`WeatherEndpoints`
        Enum representing the endpoint that was bulk-requested
    data: List[Tuple[:class:`str`, Any]]
        A list containing responses with their IDs.
        For example this can be: ``[("London-ID", CurrentWeatherData), ("other-ID", CurrentWeatherData)]``
    """
    def __init__(
        self,
        raw: Dict[str, Any],
        status: int,
        code: Optional[int],
        endpoint: WeatherEndpoints,
        data: List[Tuple[str, Any]]
    ) -> None:
        super().__init__(raw, status, code)
        
        self.endpoint: WeatherEndpoints = endpoint
        self.data: List[Tuple[str, Any]] = data # too lazy to do it here check Client.bulk_request
    