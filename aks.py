import networkx as nx
import numpy as np

def AKS (bi):
    cardinality = 0
    left_nodes = set(n for n,d in bi.nodes(data=True) if d['bipartite']==0)
    right_nodes = set(n for n,d in bi.nodes(data=True) if d['bipartite']==1)
    count = 0
    while (len(bi.edges())!=0):
        count+=1
        sum_not_one = 0;
        ##Searching the left side for min degree node
        min_left_node, min_left_degree = min(bi.degree(left_nodes).items(), key=lambda x: x[1])
        
		##Removing node if degree is zero
        if (min_left_degree==0):
            bi.remove_node(min_left_node)
            left_nodes.remove(min_left_node)
        
        else:
			##Find the connected node on the right side
            connected_right_node = bi.edges(min_left_node)[0][1]
			##Remove both nodes
            bi.remove_node(min_left_node)
            bi.remove_node(connected_right_node)
            
            left_nodes.remove(min_left_node)
            right_nodes.remove(connected_right_node)
			##Update matching
            cardinality+=1
			##Update time spent on nodes with deg>1
            if (min_left_degree>1):
                sum_not_one+=1
        
        if (len(bi.edges())!=0):
            ##Searching the left side for min degree node            
            min_right_node, min_right_degree = min(bi.degree(right_nodes).items(), key=lambda x: x[1])
            ##Removing node if degree is zero
            if (min_right_degree==0):
                bi.remove_node(min_right_node)
                right_nodes.remove(min_right_node)
            
            else:
                ##Find the connected node on the left side
				connected_left_node = bi.edges(min_right_node)[0][1]
                ##Remove both nodes
                bi.remove_node(min_right_node)
                bi.remove_node(connected_left_node)
    
                left_nodes.remove(connected_left_node)
                right_nodes.remove(min_right_node)
                ##Update matching
                cardinality +=1
				##Update time spent on nodes with deg>1
                if (min_right_degree>1):
                    sum_not_one+=1          
    print cardinality, sum_not_one
    return cardinality, sum_not_one
