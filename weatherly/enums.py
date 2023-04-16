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

from enum import Enum

__all__ = (
    "Languages",
)

class Languages(Enum):
    """
    Languages - an enum representing languages available for use in the WeatherAPI requests.
    
    Attributes are languages and language codes
    
    Attributes
    ----------
    Arabic: :class:`str`
        Language code: ar
    Bengali: :class:`str`
        Language code: bn
    Bulgarian: :class:`str`
        Language code: bg
    ChineseSimplified: :class:`str`
        Language code: zh
    ChineseTraditional: :class:`str`
        Language code: zh_tw
    Czech: :class:`str`
        Language code: cs
    Danish: :class:`str`
        Language code: da
    Dutch: :class:`str`
        Language code: nl
    Finnish: :class:`str`
        Language code: fi
    French: :class:`str`
        Language code: fr
    German: :class:`str`
        Language code: de
    Greek: :class:`str`
        Language code: el
    Hindi: :class:`str`
        Language code: hi
    Hungarian: :class:`str`
        Language code: hu
    Italian: :class:`str`
        Language code: it
    Japanese: :class:`str`
        Language code: ja
    Javanese: :class:`str`
        Language code: jv
    Korean: :class:`str`
        Language code: ko
    Mandarin: :class:`str`
        Language code: zh_cmn
    Marathi: :class:`str`
        Language code: mr
    Polish: :class:`str`
        Language code: pl
    Portuguese: :class:`str`
        Language code: pt
    Punjabi: :class:`str`
        Language code: pa
    Romanian: :class:`str`
        Language code: ro
    Russian: :class:`str`
        Language code: ru
    Serbian: :class:`str`
        Language code: sr
    Sinhalese: :class:`str`
        Language code: si
    Slovak: :class:`str`
        Language code: sk
    Spanish: :class:`str`
        Language code: es
    Swedish: :class:`str`
        Language code: sv
    Tamil: :class:`str`
        Language code: ta
    Telugu: :class:`str`
        Language code: te
    Turkish: :class:`str`
        Language code: tr
    Ukrainian: :class:`str`
        Language code: uk
    Urdu: :class:`str`
        Language code: ur
    Vietnamese: :class:`str`
        Language code: vi
    WuShanghainese: :class:`str`
        Language code: zh_wuu
    Xiang: :class:`str`
        Language code: zh_hsn
    YueCantonese: :class:`str`
        Language code: zh_yue
    Zulu: :class:`str`
        Language code: zu
    """
    Arabic: str = "ar"
    Bengali: str = "bn"
    Bulgarian: str = "bg"
    ChineseSimplified: str = "zh"
    ChineseTraditional: str = "zh_tw"
    Czech: str = "cs"
    Danish: str = "da"
    Dutch: str = "nl"
    Finnish: str = "fi"
    French: str = "fr"
    German: str = "de"
    Greek: str = "el"
    Hindi: str = "hi"
    Hungarian: str = "hu"
    Italian: str = "it"
    Japanese: str = "ja"
    Javanese: str = "jv"
    Korean: str = "ko"
    Mandarin: str = "zh_cmn"
    Marathi: str = "mr"
    Polish: str = "pl"
    Portuguese: str = "pt"
    Punjabi: str = "pa"
    Romanian: str = "ro"
    Russian: str = "ru"
    Serbian: str = "sr"
    Sinhalese: str = "si"
    Slovak: str = "sk"
    Spanish: str = "es"
    Swedish: str = "sv"
    Tamil: str = "ta"
    Telugu: str = "te"
    Turkish: str =	"tr"
    Ukrainian: str = "uk"
    Urdu: str = "ur"
    Vietnamese: str = "vi"
    WuShanghainese: str = "zh_wuu"
    Xiang: str = "zh_hsn"
    YueCantonese: str =	"zh_yue"
    Zulu: str = "zu"
