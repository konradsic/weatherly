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
)

def parse_kwargs_to_urlargs(kwargs: Dict[str, Any]) -> str:
    """
    Parses keyword arguments (kwargs) to format fitting URLs
    Example: ``{"some_key": "some value", "yes": "no"}`` -> ``?some_key=some_value&yes=no``
    
    Parameters
    ----------
    kwargs: Dict[:class:`str`, Any]
        A dictionary of keyword arguments to be parsed.
        
    Returns
    -------
    args_string: :class:`str`
        A string - formatted keyword arguments
    """
    if not kwargs: return ""
    
    args_string = ""
    first = True
    
    for k,v in kwargs.items():
        args_string += f"{'?' if first else '&'}{k}={v}"
        first = False
    return args_string