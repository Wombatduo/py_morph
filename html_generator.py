def generate_html():
    result = "<HTML><HEAD></HEAD><BODY>"
    result = result + "<TABLE border='1'>"

    result = add_rows(result, 20)
    return result + "</TR></TABLE></BODY></HTML>"


def add_rows(result, r):
    for r in range(1, r):
        result += "<TR>"
        result = add_columns(result, 20)
        result += "</TR>"
    return result


def add_columns(result, i):
    for c in range(1, i):
        result += "<TD>" + str(c) + "</TD>"
    return result
