class NDAG():
    def __init__(self):
        self.vertex_list = []
        self.edge_dict = {}

    def vertex_exist(self, v):
        return v in self.vertex_list
    
    def edge_exist(self, v1, v2):
        if not self.vertex_exist(v1) or not self.vertex_exist(v2):
            return False
        else:
            return v1 in self.edge_dict[v2] and v2 in self.edge_dict[v1]

    def add_vertex(self, v):
        if not self.vertex_exist(v):
            self.vertex_list.append(v)
            self.edge_dict[v] = []
        else:
            return False
            
    def add_edge(self, v1, v2):
        if not self.edge_exist(v1, v2):
            self.edge_dict[v1].append(v2)
            self.edge_dict[v2].append(v1)
        else:
            return  'edge exists error'

            
    def rm_vertex(self, v):
        if self.vertex_exist(v):
            self.vertex_list.pop(self.vertex_list.index(v))
            self.edge_dict.pop(v)
        else:
            return  'edge exists error'
            
            
    def rm_edge(self, v1, v2):
        if self.edge_exist(v1, v2):
            self.edge_dict[v1].pop(self.edge_dict[v1].index(v2))
            self.edge_dict[v2].pop(self.edge_dict[v2].index(v1))
        else:
            return 'edge exists error'
        

    def adj_vertex(self, v):
        if self.vertex_exist(v):
            return self.edge_dict[v]
        else:
            return 'vertex exists error'
            
            
    def degree(self, v):
        if self.vertex_exist(v):
            return len(self.edge_dict[v])
        else:
            return 'vertex exists error'
        
        
    def show(self):
        print(self.vertex_list)
        print(self.edge_dict)




class DAG():
    def __init__(self):
        self.vertex_list = []
        self.edge_dict = {}


    def vertex_exist(self, v):
        return v in self.vertex_list


    def edge_exist(self, vs, vg):
        if not self.vertex_exist(vs) or not self.vertex_exist(vg):
            return False
        else:
            return vg in self.edge_dict[vs]


    def add_vertex(self, v):
        if not self.vertex_exist(v):
            self.vertex_list.append(v)
            self.edge_dict[v] = []
        else:
            return 'node exists error'


    def add_edge(self, vs, vg):
        if not self.edge_exist(vs, vg):
            self.edge_dict[vs].append(vg)
        else:
            return 'edge exists error'


    def rm_vertex(self, v):
        if self.vertex_exist(v):
            self.vertex_list.pop(self.vertex_list.index(v))
            self.edge_dict.pop(v)            
        else:
            return  'edge exists error'


    def rm_edge(self, vs, vg):
        if self.edge_exist(vs, vg):
            self.edge_dict[vs].pop(self.edge_dict[vs].index(vg))
        else:
            return 'edge exists error'


    def adj_vertex(self, v):
        if self.vertex_exist(v):
            return self.edge_dict.pop(v)
        else:
            return 'vertex exists error'


    def degree(self, v):
        if self.vertex_exist(v):
            return len(self.edge_dict[v])
        else:
            return 'vertex exists error'


    def show(self):
        print(self.vertex_list)
        print(self.edge_dict)




class WDAG():
    def __init__(self):
        self.vertex_list = []
        self.edge_dict = {}


    def vertex_exist(self, v):
        return v in self.vertex_list


    def edge_exist(self, vs, vg):
        if not self.vertex_exist(vs) or not self.vertex_exist(vg):
            return 'vertex exists error'
        else:
            return vg in [v for v, w in self.edge_dict[vs]]


    def add_vertex(self, v):
        if not self.vertex_exist(v):
            self.vertex_list.append(v)
            self.edge_dict[v] = []
        else:
            return 'vertex exists error


    def add_edge(self, vs, vg, w):
        if not self.edge_exist(vs, vg):
            self.edge_dict[vs].append([vg, w])
        else:
            return 'edge exists error'


    def rm_vertex(self, v):
        if self.vertex_exist(v):
            self.vertex_list.pop(self.vertex_list.index(v))
            self.edge_dict.pop(v)            
        else:
            return 'given vertex dose not exist'


    def rm_edge(self, vs, vg):
        if self.edge_exist(vs, vg):
            self.edge_dict[vs].pop([v for v, w in self.edge_dict[vs]].index(vg))
        else:
            return 'given edge does not exist'


    def adj_vertex(self, v):
        if self.vertex_exist(v):
            return self.edge_dict.pop(v)
        else:
            return 'vertex exists error'


    def degree(self, v):
        if self.vertex_exist(v):
            return len(self.edge_dict[v])
        else:
            return 'vertex exists error'


    def show(self):
        print(self.vertex_list)
        print(self.edge_dict)