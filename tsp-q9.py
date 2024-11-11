import itertools

def traveling_salesman(dist_matrix):
    return min(
        (sum(dist_matrix[route[i]][route[i + 1]] for i in range(len(route) - 1)) + dist_matrix[route[-1]][route[0]], route)
        for route in itertools.permutations(range(len(dist_matrix)))
    )

def main():
    num_cities = int(input("Enter the number of cities: "))
    dist_matrix = [list(map(int, input(f"Enter distances from city {i} to others: ").split())) for i in range(num_cities)]
    min_distance, shortest_route = traveling_salesman(dist_matrix)
    print(f"Shortest route: {shortest_route}\nMinimum distance: {min_distance}")

if __name__ == "__main__":
    main()
