import pytest
import weatherly

@pytest.mark.parametrize(
    ('value', 'expected', 'lang_as_object'),
    [
        ('ar', weatherly.Languages.Arabic, True),
        ('PL', weatherly.Languages.Polish, True),
        ('It', "it", False),
        (weatherly.Languages.Bengali, 'bn', False),
        ('CzECh', 'cs', False),
        ('Dutch', weatherly.Languages.Dutch, True),
        ('notAlang', None, False),
        ('weatherly', None, True)
    ]
)
def test_languages(value, expected, lang_as_object):
    assert weatherly.utils.find_language(value, asobj=lang_as_object) == expected