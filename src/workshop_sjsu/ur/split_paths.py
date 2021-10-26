import argparse
import io
import json
import math
import os
import compas

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Split paths')
    parser.add_argument(
        'file', type=str, help='json file to split paths')
    parser.add_argument(
        '--path-index', type=str, help='Path index to split, defaults to 0', default=0)
    parser.add_argument(
        '--segments', type=int, help='Numbr of segments to divide the path into, defaults to 2', default=2)

    args = parser.parse_args()

    print()
    print('Split paths')
    print()

    with io.open(args.file, 'r') as fp:
        data = json.load(fp)

    if args.path_index:
        pass
    
    for k in data.keys():
        l = data[k][args.path_index][:]
        n = math.ceil(len(l) / args.segments)
        print(f'Splitting {k} in {args.segments} segments of {n} items')
        output = [l[i:i + n] for i in range(0, len(l), n)]
        data[k] = output

    compas.json_dump(data, args.file + '-split.json', pretty=True)
