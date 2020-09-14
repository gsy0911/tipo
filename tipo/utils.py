

def insert_str(base: str, addition: str, insert_pos: int):
    addition_len = len(addition)
    return f"{base[:insert_pos]}{addition}{base[addition_len+insert_pos:]}"


def insert_large_str(base: str, addition: str, insert_x: int, insert_y: int):
    base_list = base.split("\n")
    addition_list = addition.split("\n")
    addition_height = len(addition_list)
    addition_index = 0
    result_list = []
    for idx, b in enumerate(base_list):
        if insert_y <= idx < insert_y + addition_height:
            result = insert_str(b, addition_list[addition_index], insert_x)
            result_list.append(result)
            addition_index += 1
        else:
            result_list.append(b)
    return "\n".join(result_list)
