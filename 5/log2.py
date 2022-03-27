import logging
import graypy

loger = logging.getLogger("BIS_PK")
loger.setLevel(logging.DEBUG)

handler = graypy.GELFTLSHandler('dione', 12201)
loger.addHandler(handler)

try:
    cos()
except NameError:
    loger.error("Błąd - brakuje nam funkcji do wywołania")