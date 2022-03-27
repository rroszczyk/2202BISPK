import pytest
from covertable import make

def get_orientation(phoneWidthPixels, phoneHeightPixels, operatingSystem):
  if phoneWidthPixels >= 320 and phoneWidthPixels <= 640 and phoneHeightPixels <= 1136:
    if operatingSystem == "android" or operatingSystem == "fuchsia":
        return "landscape"
    elif operatingSystem == "ios":
        return "portrait"
  elif phoneWidthPixels > 640 and phoneWidthPixels < 1242 and phoneHeightPixels > 1136 and phoneHeightPixels < 2208:
    if operatingSystem == "android" or operatingSystem == "fuchsia":
        return "portrait"
    elif operatingSystem == "ios":
        return "landscape"
  else:
    return "portrait"


## Testing

@pytest.mark.parametrize(["phoneWidthPixels", "phoneHeightPixels", "operatingSystem"],
    make([[160, 320, 480, 640, 1280], [160, 320, 480, 640, 1280], ["android", "fuchsia", "ios"]], length=3),        # length - liczba parametrów które mają być uwzględniane w iloczynie
)

def test_get_orientation(phoneWidthPixels, phoneHeightPixels, operatingSystem):
    get_orientation(phoneWidthPixels, phoneHeightPixels, operatingSystem)