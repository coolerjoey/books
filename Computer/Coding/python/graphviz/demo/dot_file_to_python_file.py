from graphviz import Digraph
grap_g = Digraph("G",format="pdf")


sub_g0 = Digraph(comment="process1",graph_attr={"style":'filled',"color":'lightgrey'},node_attr={"style":"filled","color":"red"})
sub_g0.node("a0","a0")
sub_g0.node("a1","a1")
sub_g0.node("a2","a2")
sub_g0.node("a3","a3")
sub_g0.edge("a0","a1")
sub_g0.edge("a1","a2")
sub_g0.edge("a2","a3")

sub_g0.edge("a3", "a0")

sub_g1 = Digraph(comment="process1",graph_attr={"style":'filled'})
sub_g1.node("B","b0")
sub_g1.node("C","b1")
sub_g1.node("D","b2")
sub_g1.node("E","b3")
sub_g1.edges(["BC","CD","DE"])

grap_g.node(
"start", label="start",shape="Mdiamond")
grap_g.node(
"end", label="end", shape="Mdiamond")

grap_g.subgraph(sub_g0)
grap_g.subgraph(sub_g1)
grap_g.edge("start","a0")
grap_g.edge("start","B")

grap_g.edge("a1","E")
grap_g.edge("D","a3")

grap_g.edge("a3","end")
grap_g.edge("E","end")

print(Digraph.source) 
