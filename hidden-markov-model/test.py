# -*- coding:utf-8 -*-
import numpy as np

import hmm

"""
村子里的人只有两种病情：要么健康，要么发烧。
但村民不确定自己到底是哪种状态，只能回答你感觉正常、头晕或冷。
有位村民是诊所的常客，他的病历卡上完整地记录了这三天的身体特征(正常、头晕或冷)，
他想利用医疗大数据”得出这三天的诊断结果(健康或发烧)。
"""

def generate_index_map(lables):
    """
    打上标签{0,1,2...}

    return:
        {0 : value1, 1 : value2, 2 : value3 }
        {value1 : 0, value2 : 1, value3 : 2 }
    """
    index_label = {}
    label_index = {}
    i = 0
    for l in lables:
        index_label[i] = l
        label_index[l] = i
        i += 1
    return label_index, index_label

def convert_observations_to_index(observations, label_index):
    list = []
    for o in observations:
        list.append(label_index[o])
    return list

def convert_map_to_vector(map, label_index):
    v = np.empty(len(map), dtype=float)
    for e in map:
        v[label_index[e]] = map[e]
    return v

def convert_map_to_matrix(map, label_index1, label_index2):
    """
    字典->numpy矩阵
    """
    m = np.empty((len(label_index1), len(label_index2)), dtype=float)
    for line in map:
        for col in map[line]:
            m[label_index1[line]][label_index2[col]] = map[line][col]
    return m

def main():
    # 感冒这种病，只跟病人前一天的病情有关，并且当天的病情决定当天的身体感觉。
    states = ('Healthy', 'Fever') # 病情
    observations = ('normal', 'cold', 'dizzy') # 最近三天观察到的身体感受
    start_probability = {'Healthy': 0.6, 'Fever': 0.4} # 病情的分布

    transition_probability = {
        'Healthy': {'Healthy': 0.7, 'Fever': 0.3},
        'Fever': {'Healthy': 0.4, 'Fever': 0.6},
    }   # 病情到病情的转移概率

    emission_probability = {
        'Healthy': {'normal': 0.5, 'cold': 0.4, 'dizzy': 0.1},
        'Fever': {'normal': 0.1, 'cold': 0.3, 'dizzy': 0.6},
    }   # 病情表现出身体状况的发射概率

    # 将源数据的map形式转为NumPy的矩阵形式
    states_label_index, states_index_label = generate_index_map(states)
    observations_label_index, observations_index_label = generate_index_map(observations)
    A = convert_map_to_matrix(transition_probability, states_label_index, states_label_index)
    B = convert_map_to_matrix(emission_probability, states_label_index, observations_label_index)
    observations_index = convert_observations_to_index(observations, observations_label_index)
    pi = convert_map_to_vector(start_probability, states_label_index)

    h = hmm.HMM(A, B, pi)
    V, p = h.viterbi(observations_index)
    print(" " * 7, " ".join(("%10s" % observations_index_label[i]) for i in observations_index))
    
    for s in range(0, 2):
        print("%7s: " % states_index_label[s] + " ".join("%10s" % ("%f" % v) for v in V[s]))
    print('\nThe most possible states and probability are:')
    p, ss = h.state_path(observations_index)
    for s in ss:
        print(states_index_label[s])
    print(p)

    return h

def test():
    h = main()
    # run a baum_welch_train
    observations_data, states_data = h.simulate(100)

    guess = hmm.HMM(np.array([[0.5, 0.5],
                            [0.5, 0.5]]),
                    np.array([[0.3, 0.3, 0.3],
                            [0.3, 0.3, 0.3]]),
                    np.array([0.5, 0.5])
                    )
    guess.baum_welch_train(observations_data)
    states_out = guess.state_path(observations_data)[1]
    p = 0.0
    for s in states_data:
        if next(states_out) == s: p += 1

    print(p / len(states_data))

if __name__ == "__main__":
    main()
