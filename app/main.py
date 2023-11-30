import utils

data = [
        {
            'Country': 'Colombia',
            'Population': 500
        },
        {
            'Country': 'Bolivia',
            'Population': 300
        }
    ]
def run():
    keys, values = utils.get_population()
    print(keys, values)

    # print(utils.a)

    country = input('type country: ')

    result = utils.population_by_country(data, country)
    print(result)

#esto hace  que el script se pueda ejecutar  por si mismo y al mismo tiemp
# siendo llaamado por si mismo
if __name__ == '__main__':
    run()