import argparse
import numpy as np
import joblib




def main():
    parser = argparse.ArgumentParser(
        description='ML:prediction of the vacancy formation energy of metallic vanadium.')
    parser.add_argument('--number', dest='number', type=str, required=True,
                        help='The number of atoms missing from the vacancy.')
    parser.add_argument('--surface_area', dest='surface_area', type=str, required=True,
                        help='Wiger-Seitz primary cell surface area.')
    parser.add_argument('--output', dest='outputfile', type=str, required=False,
                        help='The file of save the prediction results.')
    args = parser.parse_args()

    number = args.number
    surface_area = args.surface_area
    outputfile = args.outputfile

    outputfile_original = outputfile
    if outputfile_original == None:
        outputfile = 'output.txt'

    number_original = number
    surface_area_original = surface_area

    number_float = float(number_original)
    surface_area_float = float(surface_area_original)

    number_numpy = np.array(number_float)
    surface_area_numpy = np.array(surface_area_float)

    x = np.array([number_numpy, surface_area_numpy])
    x = np.array([x])

    model = joblib.load('ML.m')

    y = model.predict(x)

    print('number: ' + str(number_numpy) + ', surface_area: ' + str(surface_area))
    print('vacancy formation energy: ' + str(y))

    with open(outputfile, 'w') as f:
        f.write('number: '+str(number_numpy)+', surface_area: '+str(surface_area)+'\n')
        f.write('vacancy formation energy: '+str(y)+'\n')
    print('output are saved in ' + outputfile)


if __name__ == "__main__":
    main()