def scale(strng, k, n):
    result = []
    if strng == "":
        return ""
    else:
        data = strng.split("\n")
        for line in data:
            new_line = ''
            for char in line:
                new_line += char * k
            result.append([new_line] * n)
        flattened_list = [item for sublist in result for item in sublist]
        final_result = "\n".join(flattened_list)
        return final_result


scale("33er\nrrtr", 2, 3)