from classes import *
from rich import print, inspect
from rich.traceback import install
install()
finalizar_pagamento(Pix(),1500)
finalizar_pagamento(Credito(),9540.84)
finalizar_pagamento(Boleto(),439.23)