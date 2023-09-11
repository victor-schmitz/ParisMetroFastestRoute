def f(g, h, n): # Função f(n) = g(n) + h(n)
    return g[n] + h[n] # O custo do caminho para o nó n é o custo do caminho para o nó n + o custo do caminho para o nó objetivo

def update(remover, adicionar, m): # Função para atualizar a lista de nós explorados e a lista de nós a serem explorados
    remover.remove(m) # Remove o nó m da lista de nós a serem explorados
    adicionar.append(m) # Adiciona o nó m à lista de nós explorados

def a_estrela(custo, heurística, partida, objetos): # Função para encontrar o caminho mais curto entre o nó inicial e um dos nós objetivo
    listaCaminhos = [] # Lista de caminhos

    listaAberta = [partida] # Lista de nós a serem explorados
    listaFechada = [] # Lista de nós já explorados

    caminhoLen = {} # Dicionário para armazenar o custo do caminho
    caminhoLen[partida] = 0 # O custo do caminho para o nó inicial é 0

    paisNodes = {} # Dicionário para armazenar os nós pais
    paisNodes[partida] = partida # O nó inicial não tem pai

    while len(listaAberta) > 0: # Enquanto o openList não for vazio
        node = None # Inicializa o nó atual como None

        for n in listaAberta: # Para cada nó na openList
            if node == None or f(caminhoLen, heurística, n) < f(caminhoLen, heurística, node): # Se o nó atual for None ou o custo do caminho para o nó atual for menor que o custo do caminho para o nó atual
                node = n

        if node == None: # Se o nó atual for None, não há caminho possível
            break

        if node in objetos: # Se o nó atual for um dos nós objetivo
            fv_n = f(caminhoLen, heurística, node) # O custo do caminho para o nó atual é o custo do caminho para o nó atual + o custo do caminho para o nó objetivo. 
            reconstruir = [] # Lista para reconstruir o caminho

            aux = node # Inicializa o nó auxiliar como o nó atual
            while paisNodes[aux] != aux: # Enquanto o nó auxiliar não for o nó inicial 
                reconstruir.append(aux) # Adiciona o nó auxiliar à lista de nós para reconstruir o caminho
                aux = paisNodes[aux] # O nó auxiliar passa a ser o nó pai do nó auxiliar

            reconstruir.append(aux) # Adiciona o nó atual à lista de nós para reconstruir o caminho
            reconstruir.reverse() # Inverte a lista de nós para obter o caminho

            listaCaminhos.append((reconstruir, fv_n)) # Adiciona o caminho à lista de caminhos           

            update(listaAberta, listaFechada, node) # Remove o nó atual da openList e adiciona à closedList 
            continue


        caminhoCusto = custo[node] # O custo do caminho para o nó atual é o custo do caminho para o nó atual    

        for index in range(0, len(caminhoCusto)): # Para cada nó no grafo
            peso = caminhoCusto[index] # O peso é o custo do caminho para o nó atual

            if peso > 0: # Se o peso for maior que 0
                if index not in listaAberta and index not in listaFechada: # Se o nó atual não estiver na openList e não estiver na closedList 
                    listaAberta.append(index) # Adiciona o nó atual à openList
                    paisNodes[index] = node # O nó pai do nó atual é o nó atual
                    caminhoLen[index] = caminhoLen[node] + peso # O custo do caminho para o nó atual é o custo do caminho para o nó atual + o peso
                else:
                    if caminhoLen[index] > caminhoLen[node] + peso: # Se o custo do caminho para o nó atual for maior que o custo do caminho para o nó atual + o peso
                        caminhoLen[index] = caminhoLen[node] + peso # O custo do caminho para o nó atual é o custo do caminho para o nó atual + o peso
                        paisNodes[index] = node # O nó pai do nó atual é o nó atual

                        if index in listaFechada: # Se o nó atual estiver na closedList
                            update(listaFechada, listaAberta, index) # Remove o nó atual da closedList e adiciona à openList
        
        update(listaAberta, listaFechada, node) # Remove o nó atual da openList e adiciona à closedList

        if len(listaCaminhos) > 0: # Se a lista de caminhos não for vazia
            listaCaminhos = sorted(listaCaminhos, key=lambda x: x[1]) # Ordena a lista de caminhos pelo custo do caminho
            caminho = listaCaminhos[0][0] # O caminho é o primeiro caminho da lista de caminhos
        else:
            caminho = [] # O caminho é vazio

    return caminho 


                 

