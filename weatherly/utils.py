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
    overload
)
from .enums import Languages
from enum import Enum

gray = "#535353"
white = "#ffffff"

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

@overload
def find_language(lang: str, asobj: bool=False) -> None:
    ...
    
@overload
def find_language(lang: str, asobj: bool=False) -> Languages:
    ...

def find_language(lang: str, asobj: bool=False) -> str:
    """Used to find language code from available languages.

    Parameters
    ---------------
    lang: :class:`str`
        A language you want to search for

    Returns
    -----------
    Union[:class:`str`, :class:`Languages`, None]
        Language code, could be ``None``, could be a :class:`Languages` enum.
    """

    if isinstance(lang, Languages):
        try:
            if asobj: return lang
            return lang.value
        except: 
            return None

    lang = lang.lower()

    for language in Languages:
        if language.name.lower() == lang or language.value.lower() == lang:
            if asobj: return language
            return language.value
        
    return None

def str_to_enum(query: str, target: Enum) -> Enum:
    """Find a corresponding enum class for the given string
    
    Parameters
    ------------------
    query: :class:`str`
        Query string you want to get the enum class for
    target: :class:`Enum`
        An enum class inheriting from :class:`Enum`

    Returns
    ---------
    :class:`Enum`
        Found enum class for the given string
    """
    query = query.lower()

    for obj in target:
        if obj.name.lower() == query or obj.value.lower() == query:
            return obj