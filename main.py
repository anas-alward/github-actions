def add(a, b):
    return a + b


if __name__ == "__main__":
    result = add(2, 3)
    print(f"Result: {result}")

    # Generate an artifact file
    with open("result.txt", "w") as f:
        f.write(f"The result of 2 + 3 is: {result}\n")
    print("Result saved to result.txt")
