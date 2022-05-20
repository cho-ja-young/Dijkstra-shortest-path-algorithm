import heapq  
# 우선 순위 큐 구현을 위해 import 하였다. 
# heapq 모듈 사용 

'''
Dijkstra‘s shortest path 알고리즘 설명에도 적었지만, 
초기의 구현에선 O(V^2)의 시간복잡도를 가졌지만
우선 순위 큐를 적용하여 “O((V+E) log V)”의 시간복잡도를 가지게 되었다.

'''
# dictionary 객체를 이용해서 그래프를 표현


'''
# test-case 1
# 노드 : 6개, 간선 : 9개

graph = {
    'A': {'B': 1, 'D': 3, 'E': 5},
    'B': {'C': 2},
    'C': {'F': 7},
    'D': {'C': 2, 'F': 4},
    'E': {'D': 6},
    'F': {'E': 2}
}

'''


'''
# test-case 2
# 노드 : 6개, 간선 : 8개

graph = {
    'A': {'B': 6, 'E': 8},
    'B': {},
    'C': {'B': 3},
    'D': {'B': 2, 'C': 3},
    'E': {'D': 1, 'F': 2},
    'F': {'C': 4}
}

'''



# test-case 3
# 노드 : 7개, 간선 : 10개

graph = {
    'A': {'B': 3, 'D': 2, 'G': 7},
    'B': {'C': 2},
    'C': {'G': 1},
    'D': {'G': 2, 'E': 3},
    'E': {'F': 4},
    'F': {'C': 6},
    'G': {'F': 5}
}


def dijkstra(graph, node_start):
    # 큐 생성 
    queue = []
    # start로 부터 거리가 얼마나 되는지 저장하기 위한 딕셔너리 생성 
    dis_from_start = {node: float('inf') for node in graph} # inf는 무한대를 나타낸다. 
    # 시작하는 노드의 값은 0으로 설정한다. 
    dis_from_start[node_start] = 0
    # queue에 시작하는 노드 추가 
    heapq.heappush(queue, [dis_from_start[node_start], node_start]) 
    # heapq 모듈의 heappush() 함수 사용
    # 첫번째 인자는 원소 추가 대상 리스트이고. 두번째 인자는 추가할 원소이다.
    # 위에서는 딕셔너리를 구성하고 있으므로 [dis_from_start[node_start], node_start] 
    # => 이렇게 key와 value값으로 구성되어 있다. 

    while queue: 
        # 알고리즘 진행 과정에 따라,
        # 도착 노드가 미방문 노드 집합에서 벗어나면,
        # 즉, 아래의 코드에서는 queue에 남아 있는 노드가 없으면,
        # 알고리즘 실행을 종료하고 결과를 보여준다.
        current_distance, current_dest_node = heapq.heappop(queue)
        # heapq 모듈의 heappop() 함수 사용
        # 넣어준 인자는 원소를 삭제할 대상 리스트이며 가장 작은 원소를 삭제하고 그 값을 리턴한다.
        # 위에서는 가장 작은 원소 즉, 현재 탐색할 노드와 시작 노드와의 거리를 가져오는 것을 알 수 있다.  

        if dis_from_start[current_dest_node] < current_distance:
            # 만약, 현재 탐색 노드의 거리가
            # 기존에 가지고 있던 시작 노드와의 거리보다 길다면,
            # 갱신할 필요성이 없어지기 때문에 아래의 코드를 실행하지 않고
            # 바로 건너뛰어 다음의 경우를 실행한다. 
            continue  
    
        for new_dest_node, new_distance in graph[current_dest_node].items():
            # items()를 통해 딕셔너리의 key-value 쌍을 구한다. 
            # key : 탐색할 노드
            # value : 거리 
            accumulated_distance = current_distance + new_distance
            # 원래의 거리와 탐색된 노드의 거리의 합
            # 거쳐간 노드를 계산하는 부분. 
            if accumulated_distance < dis_from_start[new_dest_node]:
                # 최소 거리 탐색을 위해 
                # 알고 있던 거리보다 새롭게 위에서 계산한 거리가 작으면,
                # 아래의 코드를 통해 곧바로 갱신한다. 
                dis_from_start[new_dest_node] = accumulated_distance
                heapq.heappush(queue, [accumulated_distance, new_dest_node])
                # 첫번째 인자는 원소 추가 대상 리스트이고. 두번째 인자는 추가할 원소이다.
                # 계산한 거리와 탐색 노드를 바로 큐에 삽입한다. 
                # 다음 거리 계산을 위한 준비. 
    
    return dis_from_start


print("<< test-case 실행 결과 >>")
# 시작하는 노드는 편의상 다 A로 설정 
for key in dijkstra(graph, 'A'):
    print('{} 노드 방문시 최소 거리 : {}'.format(key, dijkstra(graph, 'A')[key]))