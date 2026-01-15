import networkx as nx
from database.dao import DAO


class Model:
    def __init__(self):
        self.anni = []
        self.squadre = []
        self._G = nx.Graph()


    def cerca_anni(self):
        self.anni =DAO.load_anni()

    def cerca_squadre(self,anno):
        self.squadre = DAO.load_squadre(anno)

    def build_graph(self):
        for sq1 in self.squadre:
            for sq2 in self.squadre:
                if sq1 != sq2:
                    self._G.add_edge(sq1, sq2, weight = float(sq1.salary)+float(sq2.salary))



