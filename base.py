

###统计某个列表中每个元素出现的次数
def all_list(list1):
    result = {}
    for i in set(list1):
        result[i]=list1.count(i)
    return result


###绘制分颜色和形状的散点图
def mscatter(x,y,ax=None, m=None, **kw):
    import matplotlib.pyplot as plt
    import matplotlib.markers as mmarkers
    if not ax: ax=plt.gca()
    sc = ax.scatter(x,y,**kw)
    if (m is not None) and (len(m)==len(x)):
        paths = []
        for marker in m:
            if isinstance(marker, mmarkers.MarkerStyle):
                marker_obj = marker
            else:
                marker_obj = mmarkers.MarkerStyle(marker)
            path = marker_obj.get_path().transformed(
                        marker_obj.get_transform())
            paths.append(path)
        sc.set_paths(paths)
    return sc
