import matplotlib.pyplot as plt

class Solution:
    def cartesian_coordinate_points(self, points):
        x_coordinate = [p[0] for p in points]
        y_coordinate = [p[1] for p in points]

        plt.figure(figsize=(6, 6))

        
        plt.scatter(x_coordinate, y_coordinate, color='blue', label='Points')

         
        plt.plot(x_coordinate, y_coordinate, color='red', linestyle='-', linewidth=2, label='Connecting Line')

        
        for (x, y) in points:
            plt.text(x + 0.1, y + 0.1, f"({x}, {y})", fontsize=10)

         
        plt.axhline(0, color='black', linewidth=1)
        plt.axvline(0, color='black', linewidth=1)

        plt.grid(True)
        plt.title("Cartesian Coordinates in 2D with Line")
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.xlim(min(x_coordinate) - 2, max(x_coordinate) + 2)
        plt.ylim(min(y_coordinate) - 2, max(y_coordinate) + 2)
        plt.gca().set_aspect('equal', adjustable='box')
        plt.legend()
        plt.show()

if __name__ == '__main__':
    sol = Solution()
    points = [(1, 2), (3, 4), (5, 6), (7, 8)]
    ans = sol.cartesian_coordinate_points(points)
    print(ans)
