import gcp_module
import numpy as np

# Create adjacency matrix
adj_matrix = np.zeros((5, 5))
adj_matrix[0, 1] = adj_matrix[1, 0] = 1.0
adj_matrix[0, 3] = adj_matrix[3, 0] = 1.0
adj_matrix[1, 4] = adj_matrix[4, 1] = 1.0
adj_matrix[2, 3] = adj_matrix[3, 2] = 1.0

# Convert to list of lists format
adj_matrix_list = adj_matrix.tolist()

# Call the function with all arguments in order
result = gcp_module.gcp_solver(
    adj_matrix_list,  # adj_matrix
    2,                # num_colors
    100,              # R = 100 runs
    20000,            # max_iter = 20000
    0.05,             # dt = 0.05
    1.0,              # A = 1.0
    0.5,              # alpha_init = 0.5
    0.999             # alpha_scale = 0.999
)

# Unpack the result
best_coloring, energy_history = result

print(energy_history[-1])