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

__all__ = (
    "WeatherlyException",
    "WeatherAPIException",
    "NoLocationFound",
    "InvalidAPIKey",
    "APILimitExceeded",
    "APIKeyDisabled",
    "AccessDenied",
    "InternalApplicationError",
)

class WeatherlyException(Exception):
    """
    A base class for all ``weatherly`` exceptions. Almost all exceptions of this module inherit from this class.

    Inherits from :class:`Exception`.
    """
    pass

class InvalidDate(WeatherlyException):
    """
    Raised when a date (for History/Future API) is invalid.

    Inherits from :class:`WeatherlyException`.
    """
    pass

class WeatherAPIException(WeatherlyException): 
    """
    The base class for :class:`Client` weather requests exceptions.
    
    Parameters
    ----------
    status: :class:`int`
        HTTP status code
    code: :class:`int`
        Error code
    message: :class:`str`
        Message provided with the error
    """
    def __init__(self, status: int, code: int, message: str, *args):
        self.status = status
        self.code = code
        self.message = message
        self.formatted_message = f"{self.status} (error code {self.code}): {message}"
        super().__init__(self.formatted_message, *args)

class NoLocationFound(WeatherAPIException): 
    """
    Exception like this is raised when no location was found when searching for weather data.

    Usually has status code  400 and error code 1006.
    
    Inherits from :class:`WeatherAPIException`.
    """
    pass

class InvalidAPIKey(WeatherAPIException): 
    """
    Exception like this is raised when provided API key is invalid

    Usually has status code 401 and error code 2006.
    
    Inherits from :class:`WeatherAPIException`.
    """
    pass

class APILimitExceeded(WeatherAPIException): 
    """
    Exception like this is raised when API key has exceeded monthly calls limit.

    Usually has status code 400 and error code 2007.
    
    Inherits from :class:`WeatherAPIException`.
    """
    pass

class APIKeyDisabled(WeatherAPIException): 
    """
    Exception like this is raised when API key has been disabled.

    Usually has status code 403 and error code 2008.
    
    Inherits from :class:`WeatherAPIException`.
    """
    pass

class AccessDenied(WeatherAPIException): 
    """
    Exception like this is raised when API key does not have access to requested resource.

    Usually has status code 403 and error code 2009.
    
    Inherits from :class:`WeatherAPIException`.
    """
    pass

class InternalApplicationError(WeatherAPIException): 
    """
    Exception like this is raised when an internal application error occured. There is nothing to do about it.

    Usually has status code 400 and error code 9999.
    
    Inherits from :class:`WeatherAPIException`.
    """
    pass