# グラフのノード、エッジの定義
import collections
class Vertex(object):
    def __init__(self, id):
        self.id = id
        self.adjacent = {}
        # 開始点からの距離
        self.distance = -1
        # 前の点を記録し、最短経路を出力する時に使う
        self.previous = None
    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight
    
    def get_neighbors(self):
        return self.adjacent
    def get_connections(self):
        return self.adjacent.keys()  
    def get_vertex_id(self):
        return self.id
    def get_weight(self, neighbor):
        return self.adjacent[neighbor]
    
    def set_distance(self, distance):
        self.distance = distance
    def get_distance(self):
        return self.distance
    def set_previous(self, previous_vertex):
        self.previous = previous_vertex 
    
    def get_previous(self):
        return self.previous 

class Graph(object):
    def __init__(self):
        self.vertex_dict = {}
        self.num_vertex = 0
    
    def __iter__(self):
        return iter(self.vertex_dict.values())
    def add_vertex(self, id):
        self.num_vertex = self.num_vertex + 1
        new_vertex = Vertex(id)
        self.vertex_dict[id] = new_vertex
        return new_vertex
    def get_vertex(self, id):
        if id in self.vertex_dict:
            return self.vertex_dict[id]
        else:
            return None
    def add_edge(self, frm, to, weight=0):
        if frm not in self.vertex_dict:
            self.add_vertex(frm)
        if to not in self.vertex_dict:
            self.add_vertex(to)
        self.vertex_dict[frm].add_neighbor(self.vertex_dict[to], weight)
    def get_vertices(self):
        return self.vertex_dict.keys()
    def get_edges(self):
        edges = []
        for v in self.vertex_dict.values():
            for w in v.get_connections():
                vid = v.get_vertex_id()
                wid = w.get_vertex_id()
                edges.append((vid, wid, v.get_weight(w)))
        return edges