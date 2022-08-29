#导入dot文件
#https://stackoverflow.com/questions/41942109/plotting-the-digraph-with-graphviz-in-python-from-dot-file#
#方法一
from graphviz import Source

# # setup流程图
# setup_path = 'F:/专业资料/编程+教程/python/graphviz/ardusub流程图/gv_files/setup.gv'
# setup = Source.from_file(setup_path)
# setup.view()

#fast_loop()流程图
fastloop_path = 'F:/专业资料/编程+教程/python/graphviz/ardusub流程图/gv_files/fast_loop.gv'
fastloop = Source.from_file(fastloop_path)
fastloop.view()

# #FMU启动过程流程图
# FMUstart_path = 'F:/专业资料/编程+教程/python/graphviz/ardusub流程图/gv_files/FMU启动过程.gv'
# FMUstart = Source.from_file(FMUstart_path)
# FMUstart.view()

# # ArduSub_stable总流程图
# ArduSub_stable_path = 'F:/专业资料/编程/python/graphviz/ardusub流程图/gv_files/ArduSub-stable.gv'
# ArduSub_stable = Source.from_file(ArduSub_stable_path)
# ArduSub_stable.view()

# #rcs启动过程流程图
# RCSstart_path = 'F:/专业资料/编程+教程/python/graphviz/ardusub流程图/gv_files/rcs.gv'
# RCSstart = Source.from_file(RCSstart_path)
# RCSstart.view()