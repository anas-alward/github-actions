import os

def add(a, b):
    return a + b


if __name__ == "__main__":
    app_env = os.getenv("APP_ENV", "local")
    api_key = os.getenv("API_KEY", "NOT_SET")
    
    print(f"Running in environment: {app_env}")
    result = add(2, 3)
    print(f"Result: {result}")

    # Generate an artifact file
    with open("result.txt", "w") as f:
        f.write(f"Environment: {app_env}\n")
        f.write(f"API Key Status: {'Present' if api_key != 'NOT_SET' else 'Missing'}\n")
        f.write(f"The result of 2 + 3 is: {result}\n")
    print("Result saved to result.txt")
