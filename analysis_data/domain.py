"""仅核对输入形状，不生成分析结果。"""
from .io import unique,integer
def summarize(v,root):
    if not v['years'] or v['years']!=sorted(set(v['years'])):raise ValueError('年度不严格递增')
    for t in v['years']:integer(t,1)
    unique(v['stock_observations'],'id');unique(v['queries'],'id')
    return {'years':len(v['years']),'regions':len(v['regions']),'observations':len(v['stock_observations'])}
