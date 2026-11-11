from rich import print
from rich.panel import Panel

class ControleRemoto:
    canal_min:int = 1
    canal_max:int = 6
    volume_min:int = 1
    volume_max:int = 5

    def __init__(self, canal = 1, volume = 2):
        self.canal_atual:int = canal
        self.volume_atual:int = volume
        self.ligado:bool = False

    def liga_desliga(self):
        self.ligado = not self.ligado

    def canal_mais(self):
        if self.ligado:
            if self.canal_atual == self.canal_max:
                self.canal_atual = self.canal_min
            else:
                self.canal_atual += 1

    def canal_menos(self):
        if self.ligado:
            if self.canal_atual == self.canal_min:
                self.canal_atual = self.canal_max
            else:
                self.canal_atual -= 1

    def volume_mais(self):
        if self.ligado:
            if self.volume_atual != self.volume_max:
                self.volume_atual += 1

    def volume_menos(self):
        if self.ligado:
            if self.volume_atual != self.volume_min:
                self.volume_atual -= 1
                

    def mostrar_tv(self):
        conteudo = ''
        if not self.ligado:
            conteudo = f":prohibited: A tv está desligada"
        else:
            conteudo = f"CANAL = "
            for canal in range(self.canal_min, self.canal_max + 1):
                if canal == self.canal_atual:
                    conteudo += f"[yellow on yellow] {canal} [/yellow on yellow] "
                else:
                    conteudo += f" {canal} "

            conteudo += f'\n VOLUME = '
            for volume in range(self.volume_min, self.volume_max + 1):
                if volume <= self.volume_atual:
                    conteudo += f"[green on green].[/green on green]"
                else:
                    conteudo += f"[white on white].[/white on white]"
             
            
        tv = Panel(conteudo, title="[ TV ]", width=30)
        print(tv)

tv1 = ControleRemoto()
while True:
    tv1.mostrar_tv()
    comando = str(input(f"< CH{tv1.canal_atual} >  - VOL{tv1.volume_atual} + "))
    match comando:
        case '@':
            tv1.liga_desliga()
        case '<':
            tv1.canal_menos()
        case '>':
            tv1.canal_mais()
        case '-':
            tv1.volume_menos()
        case '+':
            tv1.volume_mais()
        case '0':
            break


    