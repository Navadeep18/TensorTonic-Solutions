def precision_recall_at_k(recommended, relevant, k):
    relevant=set(relevant)
    top_k=recommended[:k]
    hits=sum(item in relevant for item in top_k)
    precision=hits/k
    recall=hits/len(relevant) if len(relevant)>0 else 0.0
    return [precision,recall]