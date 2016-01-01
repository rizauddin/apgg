# Anti-Plagiarism Graph Generator

## Introduction
In programming assignments, students tend to copy from one another as they are given the same set of questions. This conduct should not be allowed as it is an individual assignment and each student must complete on his own. The existing program is available to detect plagiarism through source code similitude. However, it is hard to detect similarity in source code especially if the number of students is high. Furthermore, it is better to prevent plagiarism before it is committed. 

The “Anti-Plagiarism Graph Generator” program is developed to prevent plagiarism in Graph Theory course programming assignments. The prevention is done at the very beginning before the students start to do their programming assignments. This is possible as students will get a different set of question based on their students’ identification number. Students will generate their own graph by using this program. Later, students will use their unique graph to complete the programming assignment.

## Usage Example
To generate a graph:
```python
import APGG
G = APGG.generate_graph(2020638162)
APGG.draw(G)
```

To generate a network flow:
```python
import APGG
L = APGG.generate_flow(2020638162)
APGG.draw(L, weight='capacity')
```

