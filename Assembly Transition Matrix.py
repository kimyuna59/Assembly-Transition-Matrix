# INPUT
import numpy as np
import pandas as pd
N = int(input("행 또는 열의 개수를 입력하세요: "))
print("행렬 요소를 공백으로 구분하여 한 줄로 입력하세요: ")   # 입력 예시 : (N=4일때) 0 1 1 0 1 0 1 0 1 1 0 1 0 0 1 0 / 0 1 0 0 1 0 1 0 0 1 0 1 0 0 1 0 / 0 1 0 1 1 0 1 0 0 1 0 1 1 0 1 0
matrix_elements = list(map(int,input().split()))   # 입력 예시 : (N=3일때) 0 1 0 1 0 1 0 1 0 (N=5일때) 0 1 1 0 0 1 0 1 0 0 1 1 0 1 1 0 0 1 0 1 0 0 1 1 0
numpy_array = np.array(matrix_elements)   # 1차원 배열을
ar = numpy_array.reshape(N,N)   # 2차원 배열로
df = pd.DataFrame(ar,index=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')[:N],columns=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')[:N])   # N=3이면 A,B,C N=4이면 A,B,C,D N=5이면 A,B,C,D,E 출력
print("input: \n")
print(df)

# ASSEMBLY
# 새로운 리스트 생성 함수 정의
def new_list(list,df):
  for i in range(len(df.index)):
      for j in range(len(df.columns)):
          if df.iloc[i, j] == 1:   # 값이 1인 원소들에 대해
              s = ''.join(sorted(df.index[i] + df.columns[j]))   # 각 행과 열의 문자를 추출 & 정렬 후 같은 문자열로 취급
              if s not in list:   # 문자열이 printed에 있는지 확인
                  list.append(s)
  print('\n',list,'\n',"-"*50)

# 새로운 데이터프레임 함수 정의
def new_df(new_list,new_df):
  # 배열 0으로 초기화
  new_array = np.zeros((len(new_list), len(level1_list)))

  # 배열 0 또는 1로 채우기
  for i in range(len(new_list)):
    for j in range(len(level1_list)):
        if level1_list[j] in new_list[i]:
            new_array[i][j] = 0   # level1_list의 j번째 요소가 new_list의 i번째 요소에 포함되어 있다면 0을 할당
        else:
            flag = False   # 새로운 리스트의 i번째 요소에 대해 level1_list의 j번째 column에 1을 할당해야 하는지를 결정
            for k in range(len(new_list[i])):
                if df.loc[new_list[i][k], level1_list[j]] == 1:
                    new_array[i][j] = 1   # new_list[i][k]가 level1_list[j]와 관련된 데이터프레임의 요소(1 또는 0)인지 확인, 1이라면 new_array[i][j]에 1을 할당
                    flag = True
                    break
            if not flag:
                new_array[i][j] = 0
  # 새로운 데이터프레임에 배열 할당
  new_df.loc[:, :] = new_array
  print(new_df.round(0).astype(int))

# 추가로 다른 문자열을 붙여주는 함수 정의
def list_with_extra(list,state):
  for s in list:
    s_with_extra = s
    for c in df.columns:
      if c not in s:
        s_with_extra += '/' + c
    state.append(s_with_extra)
  print(state)

# level1_list 생성
level1_list = list(df.columns)   # df의 열 인덱스를 리스트 형태로 추출
print("\n", level1_list)

# level2_list 생성
level2_list = []
new_list(level2_list,df)

# 새로운 데이터프레임 생성
df2 = pd.DataFrame(index=level2_list, columns=level1_list)

# 새로운 데이터프레임 함수 사용
new_df(level2_list,df2)

# level3_list 생성
level3_list = []
new_list(level3_list,df2)

# 새로운 데이터프레임 생성
df3 = pd.DataFrame(index=level3_list, columns=level1_list)

# 새로운 데이터프레임 함수 사용
new_df(level3_list,df3)

# level4_list 생성
level4_list = []
new_list(level4_list,df3)

# 새로운 데이터프레임 생성
df4 = pd.DataFrame(index=level4_list, columns=level1_list)

# 새로운 데이터프레임 함수 사용
new_df(level4_list,df4)

# level5_list 생성
level5_list = []
new_list(level5_list,df4)

# 처음 파트 상태
first_state = []
first_state.append('/'.join(level1_list))
print(first_state)

# 두 번째 파트 상태
second_state = []
list_with_extra(level2_list,second_state)

# 세 번째 파트 상태
third_state = []
list_with_extra(level3_list,third_state)

# 네 번째 파트 상태
fourth_state = []
list_with_extra(level4_list,fourth_state)

# 다섯 번째 파트 상태
fifth_state = []
list_with_extra(level5_list,fifth_state)

import itertools
# 노드 리스트 만들기
node_list = list(itertools.chain(first_state, second_state, third_state, fourth_state, fifth_state))
print(node_list)

# 엣지 리스트 만들기
edge_list = []

# first_state와 second_state의 순서쌍 만들기
for first in first_state:
    for second in second_state:
        edge_list.append((first, second))

# second_state와 third_state의 순서쌍 만들기
for second in second_state:
    for third in third_state:
        if all(char in third.split('/')[0] for char in second.split('/')[0]):
            edge_list.append((second, third))

# third_state와 fourth_state의 순서쌍 만들기
for third in third_state:
    for fourth in fourth_state:
        if all(char in fourth.split('/')[0] for char in third.split('/')[0]):
            edge_list.append((third, fourth))

# fourth_state와 fifth_state의 순서쌍 만들기
for fourth in fourth_state:
    for fifth in fifth_state:
        if all(char in fifth.split('/')[0] for char in fourth.split('/')[0]):
            edge_list.append((fourth, fifth))

print(edge_list)

# OUTPUT
# 노드의 인덱스 딕셔너리 생성
index_dict = {node_list[i]: i for i in range(len(node_list))}

# 인접행렬 생성
adj_matrix = np.zeros((len(node_list), len(node_list)))
for edge in edge_list:
    start = index_dict[edge[0]]
    end = index_dict[edge[1]]
    adj_matrix[start][end] = 1

# pandas DataFrame으로 변환하여 인덱스 지정
final_df = pd.DataFrame(adj_matrix, index=node_list, columns=node_list).round(0).astype(int)

print(final_df)