import utils_2
import read_csv
import charts


def run():
    data = read_csv.read_csv('./data.csv')
    country = input('type country: ')
    result = utils_2.population_by_country(data, country)

    if len(result) > 0:
        country = result[0]
        labels, values = utils_2.get_population(country)
        charts.generate_bar_chart(country['Country'], labels, values)


    print(result)

#esto hace  que el script se pueda ejecutar  por si mismo y al mismo tiemp
# siendo llaamado por si mismo
if __name__ == '__main__':
    run()