from variance import get_average, get_variance

def covariance(xs, ys):
    avg_x = get_average(xs)
    avg_y = get_average(ys)
    product_sums = 0
    for x, y in zip(xs, ys):
        product_sums += (x-avg_x)*(y-avg_y)
    return product_sums/(len(product_sums)-1)

if __name__=="__main__":
    #https://www.statisticshowto.com/probability-and-statistics/statistics-definitions/covariance/
    a = [2.1, 2.5, 3.6, 4.0]
    b = [8,   10,  12,  14 ]
    print(covariance(a,b))
