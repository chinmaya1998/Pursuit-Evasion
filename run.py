import sys
import time
from networkx import nx
import random
import Agent as ag
import World as w
import random_actor as act

a = ag.Agent('chi','pursuer')
b = ag.Agent('nav','evader')

n = int(sys.argv[2])
m = int(sys.argv[3])
world = w.World(n, m, [a,b])
g = world.get_graph()
print(g.neighbors((10)))
temp = n + 1
temp = temp*(m/2 + 1)

if (sys.argv[1] == 'capture'):
	print('No. of nodes in the graph are ' + str(temp))
	start = time.time()
	n_steps = 0
	while(True):
		if len(nx.algorithms.shortest_paths.generic.shortest_path(world.get_graph(),a.get_location(),b.get_location())) -1 == 0:
			print('Captured at step ' +str(n_steps))
			break

		world.next_state()
		n_steps = n_steps + 1
    
	end = time.time()
	print(str(end-start) + ' seconds elapsed')



elif(sys.argv[1] =='setruns'):
	n_steps = int(sys.argv[4])

	for i in range(0,n_steps):
		print(a.get_location(),
		b.get_location(),
          	len(nx.algorithms.shortest_paths.generic.shortest_path(
                                                  world.get_graph(),
                                                  a.get_location(),
                                                  b.get_location()))-1)
		if len(nx.algorithms.shortest_paths.generic.shortest_path(world.get_graph(),a.get_location(),b.get_location())) -1 == 0:
			print('Captured')
			break
		world.next_state()