def cal_corr(list1, list2, option=0):
    if len(list1) == len(list2):
        i = -1
        prod_list = []
        min_sqr1 = []
        min_sqr2 = []
        for val in list1:
            i += 1
            prod_list.append(list1[i] * list2[i])
            min_sqr1.append(list1[i] ** 2)
            min_sqr2.append(list2[i] ** 2)

        numerator = ((len(list1) * sum(prod_list)) - (sum(list1) * sum(list2)))
        denominator = (sqrt(len(list1) * sum(min_sqr1) - sum(list1) ** 2) * sqrt(len(list2) * sum(min_sqr2) - sum(list2) ** 2))
        denominator = denominator.real
        correlation = numerator / denominator
        if option == 0:
            return (correlation)
        elif option == 1:
            return (sum(list1), sum(list2), sum(prod_list), sum(min_sqr1), len(list1))
    else:
        print('ERROR LISTS ARE NOT THE SAME LENGTH CANT COMPUTE')
        return False

def LSC(list1, list2):
    x_sum, y_sum, prod_sum, xsqr_sum, list_len = cal_corr(list1, list2, 1)
    matrix1 = [[xsqr_sum, x_sum], [x_sum, list_len]]
    matrix2 = [prod_sum, y_sum]
    matrix1 = np.array(matrix1)
    matrix2 = np.array(matrix2)
    inv_mat1 = np.linalg.inv(matrix1)
    solution = np.dot(inv_mat1, matrix2)
    # a = slope b = y int
    a = solution[0]
    b = solution[1]
    return(a, b)

def comp_residual(x, y):
    a, b = LSC(x, y)
    val_list = []
    r_list = []
    for val in x:
        val_list.append(val*a + b)
    for i in range(len(y)):
        r_list.append(y[i] - val_list[i])
    r_mean = mean(r_list)
    r_std = stand_dev(r_list)
    return(r_list, r_mean, r_std, a, b)

def scatter_plot_residual(data1, data2, name,x_name, y_name, slope, y_int, n_dev, r_mean, r_std):
    y_vals = []
    l_bound = []
    u_bound = []
    x_data = [min(data1), max(data1)]
    for val in range(2):
        ans = (slope * x_data[val]) + y_int
        y_vals.append(ans)
    for val in range(2):
        l_bound.append((slope * x_data[val]) + y_int - (n_dev*r_std))
    for val in range(2):
        u_bound.append((slope * x_data[val]) + y_int + (n_dev*r_std))
    plt.text(x_data[len(x_data) - 2], y_vals[-1] + .1, f'Y={round(slope, 3)}*X+{round(y_int, 3)}', color='g', fontsize=10)
    plt.plot(x_data, y_vals, '-r')
    plt.plot(x_data, l_bound, '--r')
    plt.plot(x_data, u_bound, '--r')
    plt.scatter(data1, data2)
    plt.title(f'{name}')
    plt.xlabel(f'{x_name}')
    plt.ylabel(f'{y_name}')
    plt.show()

def calc_RSME(res_list):
    new_list = []
    res_len = len(res_list)
    for val in res_list:
        new_list.append(val**2)
    RSME = (sqrt(sum(new_list) / res_len)).real
    return(RSME)

def delete_outliers(list1, list2, slope, y_int, ndev, r_std):
    for val in range(len(list1)):
        y1 = ((slope * list1[val - 1]) + y_int - (ndev*r_std))
        y2 = ((slope * list1[val - 1]) + y_int + (ndev*r_std))
        if list2[val - 1] > y2 or list2[val - 1] < y1:
            list2.pop(val - 1)
            list1.pop(val - 1)
    return(list1, list2)

