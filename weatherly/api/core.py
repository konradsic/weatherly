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
    Any,
    Optional,
    List,
    Tuple,
    Literal,
    Dict,
    TypeVar
)
import urllib
import requests
from ..utils import parse_kwargs_to_urlargs
import json

T = TypeVar("T")

__all__ = (
    "BaseAPIClient",
)

class BaseAPIClient():
    """
    Represents a base API client that can handle requests. Used as a base class for :class:`Client`
    
    Parameters
    ----------
    base_url: :class:`str`
        An URL that will be used as a base for requests.
    default_options: Optional[Dict[:class:`str`, Any]]
        Default options for requests made by the client that will be automatically added.
    """
    def __init__(
        self,
        base_url: str,
        default_options: Optional[Dict[str, Any]]
    ) -> None:
        self.url = base_url
        self.default_options = default_options or {}
        
    def _request(
        self,
        path: str,
        **kwargs: Optional[Dict[str, str]]
    ) -> Tuple[Dict[Any, Any], requests.Response]:
        """
        Request data from the base URL + path.
        Private function, use :class:`Client` methods instead
        
        Parameters
        ----------
        path: :class:`str`
            A path that will be used as an endpoint for the request.
        kwargs: Optional[Dict[str, str]]
            Additional parameters for the request.
        """
        full_url = self.url + path + parse_kwargs_to_urlargs({**self.default_options, **kwargs})

        response = requests.get(full_url)
        return response.json(), response
        
        
    