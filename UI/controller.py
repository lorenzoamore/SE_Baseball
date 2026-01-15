import flet as ft
from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model
        self.selezione = ""
        self.best_percorso = []
        self.best_peso = 0

    def handle_crea_grafo(self, e):
        """ Handler per gestire creazione del grafo """""
        # TODO
        self._model.build_graph()

    def handle_dettagli(self, e):
        """ Handler per gestire i dettagli """""
        # TODO
        vicini = []
        selezionato = self._view.dd_squadra.value
        for s in self._model.squadre:
            if self._view.dd_squadra.value == s.team_code:
                selezionato = s
                self.selezione = s
                vicini = list(self._model._G.neighbors(s))
        vicini.sort(key=lambda v: self._model._G[selezionato][v]['weight'], reverse=True)
        self._view.txt_risultato.clean()
        for v in vicini:
            self._view.txt_risultato.controls.append(
                ft.Text(f"{v.team_code} ({v.name}) - peso {self._model._G[selezionato][v]['weight']}"))
        self._view.update()

    def handle_percorso(self, e):
        """ Handler per gestire il problema ricorsivo di ricerca del percorso """""
        # TODO
        vicini = list(self._model._G.neighbors(self.selezione))
        vicini.sort(key=lambda v: self._model._G[self.selezione][v]['weight'], reverse=True)
        self._ricorsione(self.selezione,
                         [[self.selezione,vicini[0],self._model._G[self.selezione][vicini[0]]['weight']]],
                         [self.selezione],
                         vicini[0],
                         self._model._G[self.selezione][vicini[0]]['weight'])
        result = []
        for e in self.best_percorso:
            stringa = (f"{e[0].team_code} ({e[0].name}) -> {e[1].team_code} ({e[1].name}) - peso {e[2]}")
            result.append(stringa)
        result.append(f"Peso totale: {self.best_peso}")
        self._view.txt_risultato.clean()
        for a in result:
            self._view.txt_risultato.controls.append(ft.Text(a))
        self._view.update()
    def _ricorsione(self,selezione,percorso,archi_usati,ultimo,peso_corrente):
        if peso_corrente > self.best_peso:
            self.best_peso = peso_corrente
            self.best_percorso = percorso.copy()


        vicini = list(self._model._G.neighbors(ultimo))
        vicini.sort(key=lambda v: self._model._G[ultimo][v]['weight'], reverse=True)
        for v in vicini:
            if self._model._G[selezione][ultimo]['weight'] > self._model._G[ultimo][v]['weight']:
                if v not in archi_usati:
                    self._ricorsione(ultimo,percorso + [[ultimo,v,self._model._G[ultimo][v]['weight']]],archi_usati + [ultimo],v,peso_corrente + self._model._G[ultimo][v]['weight'])



    """ Altri possibili metodi per gestire di dd_anno """""
    # TODO
    def handle_popola_dd_anno(self):
        self._model.cerca_anni()
        for anno in self._model.anni:
            self._view.dd_anno.options.append(ft.dropdown.Option(text = str(anno)))
        self._view.update()

    def handle_squadre(self,e):
        self._model.cerca_squadre(self._view.dd_anno.value)
        numero_squadre = len(self._model.squadre)
        self._view.txt_out_squadre.clean()
        self._view.txt_out_squadre.controls.append(ft.Text(f"Numero di squadre: {numero_squadre}"))
        for sq in self._model.squadre:
            self._view.txt_out_squadre.controls.append(ft.Text(f"{sq.team_code} ({sq.name})"))
        self.handle_popola_dd_squadre()
        self._view.update()

    def handle_popola_dd_squadre(self):
        for sq in self._model.squadre:
            self._view.dd_squadra.options.append(ft.dropdown.Option(key = sq.team_code,text=str(f"{sq.team_code}({sq.name})")))


