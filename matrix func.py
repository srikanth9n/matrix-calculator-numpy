import numpy as np

def get_matrix(name):
    rows = int(input(f"Enter number of rows for {name}: "))
    cols = int(input(f"Enter number of columns for {name}: "))
    print(f"Enter elements row by row (space-separated):")

    matrix = []
    for i in range(rows):
        row = list(map(float, input(f"Row {i+1}: ").split()))
        matrix.append(row)

    return np.array(matrix)

def main():
    print(" Matrix Calculator Using NumPy")
    print("---------------------------------")
    print("1. Matrix Addition")
    print("2. Matrix Multiplication")
    print("3. Transpose")
    print("4. Inverse (only for square matrix)")
    print("5. Exit")

    choice = int(input("Enter your choice (1-5): "))

    if choice == 1:
        A = get_matrix("Matrix A")
        B = get_matrix("Matrix B")
        if A.shape == B.shape:
            print("Result:\n", A + B)
        else:
            print(" Shapes do not match for addition.")

    elif choice == 2:
        A = get_matrix("Matrix A")
        B = get_matrix("Matrix B")
        try:
            result = np.dot(A, B)
            print("Result:\n", result)
        except ValueError as e:
            print(" Multiplication not possible:", e)

    elif choice == 3:
        A = get_matrix("Matrix")
        print("Transpose:\n", A.T)

    elif choice == 4:
        A = get_matrix("Matrix")
        if A.shape[0] == A.shape[1]:
            try:
                print("Inverse:\n", np.linalg.inv(A))
            except np.linalg.LinAlgError:
                print(" Matrix is not invertible.")
        else:
            print(" Inverse only for square matrices.")

    elif choice == 5:
        print("Exiting... ")
        exit()

    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
