class Node:
  def __init__(self, parent, value):
    self.value = value
    self.parent = parent
    self.right_child = None
    self.left_child = None

  def add_right(self, Nodo):
    self.right_child = Nodo

  def add_left(self, Nodo):
    self.left_child = Nodo

  def get_childs(self):
    return self.left_child, self.right_child

class Tree:
  def __init__(self, root_value = None):
    self.numero_hojas = 0
    self.lista_vertices = []
    self.vertices = {}
    if root_value != None:
      self.root = Node(None,root_value)
      self.numero_hojas = 1
      self.lista_vertices.append(root_value)
      self.vertices[root_value] = []

  def get_root(self):
    return self.root

  def byArray(self, array):
    self.numero_hojas = 0
    self.lista_vertices = []
    self.vertices = {}

    self.root = Node(None, array[0])
    self.numero_hojas += 1
    self.lista_vertices.append(array[0])
    self.vertices[array[0]] = [] #{value:[Node, Node]}

    del array[0]
    current = self.root #Node type

    for numero in array:
      self.vertices[numero] = []
      self.lista_vertices.append(numero)
      self.numero_hojas += 1
      agregado = False
      while not agregado:
        if numero > current.value and current.right_child == None:
          print("a", numero)
          new_node = Node(current, numero)
          current.add_right(new_node)
          self.vertices[current.value].append(new_node)
          agregado = True
        elif numero > current.value and current.right_child != None:
          print("c", numero)
          current = current.right_child
        elif numero < current.value and current.left_child == None:
          print("b", numero)
          new_node = Node(current, numero)
          current.add_left(new_node)
          self.vertices[current.value].append(new_node)
          agregado = True
        elif numero < current.value and current.left_child != None:
          print("d", numero)
          current = current.left_child
          
  def dfs(self, node, visited = []):
    if node not in visited:
      visited.append(node)
      for child in self.vertices[node]:
          self.dfs(child.value, visited)
    return visited


  def search_node(self, value, root):
    if root is None:
      return False
    else:
      if(value == root.value):
        return True
      else:
        if(value > root.value):
          self.search_node(value, root.right_child)
        else:
          self.search_node(value, root.left_child)



  def childs(self, node_value):
    node = self.search_node(node_value, self.root)
    if node == False:
      return "No existe este nodo"
    return node.left_child.value, node.right_child.value

  def add_node(self, value, root):
    if self.search_node(value, root):
      return "Duplicated value"
    if root is None:
      self.root = Node(None, value)
    else:
      if value > root.value:
        if root.right_child:
          self.add_node(value, root.right_child)
        else:
          root.right_child = Node(root, value)
      else:
        if root.left_child:
          self.add_node(value, root.left_child)
        else:
          root.left_child = Node(root, value)
    
  def in_order(self, root):
    if root:
      self.in_order(root.left_child)#Recorrer subarbol izquierdo
      print(root.value)
      self.in_order(root.right_child)#Recorrer subarbol derecho
    else:
      return "Empty"
      
  def pre_order(self):
    if root:
      print(root.value)
      self.in_order(root.left_child)#Recorrer subarbol izquierdo
      self.in_order(root.right_child)#Recorrer subarbol derecho
    else:
      return "Empty"

  def post_order(self):
    if root:
      self.in_order(root.left_child)#Recorrer subarbol izquierdo
      self.in_order(root.right_child)#Recorrer subarbol derecho
      print(root.value)
    else:
      return "Empty"

  def buscar_hojas(self, current, lista_hojas = []):
    if current:
      if (current.left_child is None) and (current. right_child is None):
        lista_hojas.append(current.value)
      else:
        if current.left_child:
          self.buscar_hojas(current.left_child, lista_hojas)
        if current.right_child:
          self.buscar_hojas(current.right_child, lista_hojas)
      return lista_hojas
         
      


arbol = Tree()
array = [1, 5, 2, 6, 8, 4, 7]
arbol.byArray(array)

arbol.buscar_hojas(arbol.get_root())