def solution(lst):
    if not lst:
        return ""

    result = []
    start = lst[0]
    end = start

    for n in lst[1:]:
        if n == end + 1:
            end = n
        else:
            if end - start >= 2:
                result.append(f"{start}-{end}")
            else:
                result.extend([str(start)] if start == end else [str(start), str(end)])
            start = end = n

    if end - start >= 2:
        result.append(f"{start}-{end}")
    else:
        result.extend([str(start)] if start == end else [str(start), str(end)])

    return ",".join(result)
