import numpy as np
from cosbr import gcp_solver

# Create an adjacency matrix for the graph
adj_matrix = np.zeros((5, 5))
adj_matrix[0, 1] = adj_matrix[1, 0] = 1.0  # Edge between vertices 0 and 1
adj_matrix[0, 3] = adj_matrix[3, 0] = 1.0  # Edge between vertices 0 and 3
adj_matrix[1, 4] = adj_matrix[4, 1] = 1.0  # Edge between vertices 1 and 4
adj_matrix[2, 3] = adj_matrix[3, 2] = 1.0  # Edge between vertices 2 and 3

# Convert to list of lists format (required input format)
adj_matrix_list = adj_matrix.tolist()

# Solve the graph coloring problem with 2 colors
result = gcp_solver(
    adj_matrix_list,  # adjacency matrix
    2,                # number of colors
    100,              # R = 100 runs
    20000,            # max_iter = 20000
    0.05,             # dt = 0.05
    1.0,              # A = 1.0
    0.5,              # alpha_init = 0.5
    0.999             # alpha_scale = 0.999
)

# Unpack the result
best_coloring, energy_history = result

# Print the final energy (0 means a valid coloring was found)
print(f"Final energy: {energy_history[-1]}")

# Print the coloring
for i, vertex_colors in enumerate(best_coloring):
    color = next((c for c, is_colored in enumerate(vertex_colors) if is_colored), None)
    print(f"Vertex {i}: Color {color}")