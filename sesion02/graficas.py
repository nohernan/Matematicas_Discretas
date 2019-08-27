from vertice import Vertice

##############################
v_a = Vertice("a")
v_b = Vertice("b")
v_c = Vertice("c")
v_d = Vertice("d")
v_e = Vertice("e")
v_f = Vertice("f")

vertices = [v_a, v_b, v_c, v_d, v_e, v_f]
    
g = { "a" : [v_d],
      "b" : [v_c],
      "c" : [v_b, v_c, v_d, v_e],
      "d" : [v_a, v_c],
      "e" : [v_c],
      "f" : []
}

##############################
bfs_r = Vertice("r")
bfs_s = Vertice("s")
bfs_t = Vertice("t")
bfs_u = Vertice("u")
bfs_v = Vertice("v")
bfs_w = Vertice("w")
bfs_x = Vertice("x")
bfs_y = Vertice("y")

vertices_bfs = [bfs_r,bfs_s,bfs_t,bfs_u,bfs_v,bfs_w,bfs_x,bfs_y]
    
g_bfs = { "r" : [bfs_s,bfs_v],
          "s" : [bfs_r,bfs_w],
          "t" : [bfs_u,bfs_w,bfs_x],
          "u" : [bfs_t,bfs_x,bfs_y],
          "v" : [bfs_r],
          "w" : [bfs_s,bfs_t,bfs_x],
          "x" : [bfs_t,bfs_u,bfs_w,bfs_y],
          "y" : [bfs_u,bfs_x]
}

##############################
dfs_u = Vertice("u")
dfs_v = Vertice("v")
dfs_w = Vertice("w")
dfs_x = Vertice("x")
dfs_y = Vertice("y")
dfs_z = Vertice("z")

vertices_dfs = [dfs_u,dfs_v,dfs_w,dfs_x,dfs_y,dfs_z]
    
g_dfs = { "u" : [dfs_v,dfs_x],
          "v" : [dfs_y],
          "w" : [dfs_y,dfs_z],
          "x" : [dfs_y],
          "y" : [dfs_x],
          "z" : [dfs_z]
}

