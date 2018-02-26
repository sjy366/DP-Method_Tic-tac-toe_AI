Tictactoe AI using TD Method
=====================

## Run

### Training

```
$ python Train.py
```

### Play games

```
$ python Play.py
```

## Agents

* agent_RL : ��ȭ�н��� ���� �� ������Ʈ
* agent_Base : ����/�̱�� ���� �δ� �񱳿� ������Ʈ
* agent_Human : input�� �޾Ƽ� ���� ���� ������Ʈ
* value(state) : state�� �޾Ƽ� current value�� ��ȯ�մϴ�.
* policy(state) : state�� �޾Ƽ� current policy�� ��ȯ�մϴ�.

## Environment

* Tictactoe ���� ȯ���Դϴ�.
* step(action) : action�� �޾Ƽ� �����ϰ� observation�� ��ȯ�մϴ�.
* render() : ���� ���¸� ȭ�鿡 ����մϴ�.
* init()/reset() : ȯ���� �ʱ�ȭ�մϴ�.

## Learning Algorithm

* Table�� �̿��� DP Method�� ����Ͽ����ϴ�.
* Policy Iteration (using iterative policy evaluation)�Դϴ�.
* Policy Evaluation�� Policy Improvement�� �ݺ��մϴ�. (GPI)
* 1���� Iteration���� agent_Base�� 100 Episode�� �׽�Ʈ�մϴ�.

### Policy Evaluation

* Deterministic�� ȯ���̹Ƿ� ��밪�� �ƴմϴ�.
```
��� Terminal state�� �ƴ� state S�� ���ؼ�,
V(S) = R + discount_factor * V(S')
```

###  Policy Improvement

* Deterministic�� ȯ���̹Ƿ� ��밪�� �ƴմϴ�.
```
��� Terminal state�� �ƴ� state S�� ���ؼ�,
Policy(S) = Argmax_a(R + discount_factor * V(S')) s.t step(S,a) = (S',R)
```

* Hyperparameter

```
1. discount_factor : 0.9
2. theta(Policy Evaluation) : 1e-9
```

## Conclusion

* agent_Base���� �������� �·��� 100%�� �����߽��ϴ�.
* ����� ����� ����(unbeatable)���� �н��� �Ǿ����ϴ�.
* Q-learning method(off-policy TD)���� ������ Optimal policy�� �����Ͽ����ϴ�.
* ȯ���� ���� ��Ȯ�ϰ� ������ �� �ְ�, state�� ������ ���� ��쿡 ����� �� �ֽ��ϴ�.

## Reference

* Richard S. Sutton and Andrew G. Barto. (2018). Reinforcement Learning : An Introduction. 
The MIT Press Cambridge, Massachusetts London, England
