w,h=map(int,input().strip().split())
codeup = [
    " ****  ***  ***   ***** *   * ****",
    "*     *   * *  *  *     *   * *   *",
    "*     *   * *   * *     *   * *   *",
    "*     *   * *   * ****  *   * ****",
    "*     *   * *   * *     *   * *",
    "*     *   * *  *  *     *   * *",
    " ****  ***  ***   *****  ***  *"
]

for j in range(len(codeup)):
    for _ in range(h):
        for k in range(len(codeup[j])):
            for _ in range(w):
                print(codeup[j][k],end="")
        print()