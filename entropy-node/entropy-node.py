import numpy as np

def entropy_node(y):
    y=np.asarray(y)
    if y.size==0:
        return 0.0
    _,counts=np.unique(y,return_counts=True)
    p=counts/counts.sum()
    mask=p>0
    p=p[mask]
    return float(-np.sum(p*np.log2(p)))