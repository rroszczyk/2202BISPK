import logging
import graypy

loger = logging.getLogger("BIS_PK")
loger.setLevel(logging.DEBUG)

handler = graypy.GELFTLSHandler('dione', 12201)
loger.addHandler(handler)


loger.debug("To jest testowa wiadomość z naszego kodu programu")