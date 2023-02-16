# Hi these are all the functions you have used in your entirer life WHATTTTT

def weight_avg_fil(f_list, f_len, w_list):
    output = []
    for i in range(len(f_list)):
        if i <= len(f_list) - f_len:
            min_list = []
            min_list2 = []
            for j in range(f_len):
                min_list.append(f_list[i + j])

            for k in range(len(min_list)):
                min_list2.append(min_list[k] * w_list[k])

            output.append(sum(min_list2)/sum(w_list))

    return(output)


def fade_avg_fil(f_list, w_list):
    output = []
    w1, w2 = w_list[0], w_list[1]
    if sum(w_list) == 1:
        for i in range(len(f_list)):
            if i == 0:
                output.append(f_list[i])
            else:
                output.append( (w1 * output[i-1]) + (w2 * f_list[i]) )

    return(output)