tag_input = ["TT-80-2000", "TTT-80-2000", "TTTT-80-2000", "TTTTT-80-2000", "TT-80"]


def generate_valid_tagname(tag_input, pre_fix="", suf_fix=""): 
    result = ""
    try: 
        tmp_list = tag_input.split("-")
        current_begin = tmp_list[0]
        current_mid = tmp_list[1]
        current_end = tmp_list[2]

        if len(current_begin) <= 2:
            result = pre_fix + current_begin + "  -" + current_mid + "-"+ current_end + suf_fix
        elif len(current_begin) == 3:
            result = pre_fix +current_begin + " -" + current_mid + "-"+ current_end + suf_fix
        elif len(current_begin) == 4:
            result = pre_fix +current_begin + "-" + current_mid + "-"+ current_end + suf_fix
        else:
            result = pre_fix +current_begin + "-" + current_mid + "-"+ current_end + suf_fix
    except IndexError as e:
        print(e, str(tmp_list))
    
    return result

for tag in tag_input:
    print(generate_valid_tagname(tag, pre_fix="LIMX-", suf_fix=".IT"))