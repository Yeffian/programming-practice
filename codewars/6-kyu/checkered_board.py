def checkered_board(n):
    first = "□" if n % 2 == 0 else "■"
    second = "■" if first == "□" else "□"
    out = ""

    for i in range(n):
        result = ""
        for j in range(n):
            if (i + j) % 2 == 0:
                result += first
            else:
                result += second
            if j < n - 1:
                result += " "
        if i < n - 1:
            result += "\n"
        out += result

    return out