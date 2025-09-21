import os
import argparse
import random


def main(args):
    random.seed(123)
    n = args.n
    input_dir = args.input_dir

    dirs = os.listdir(input_dir)
    print(f"a total of {len(dirs)} folder for templated sqls")

    output_dir = input_dir  + f'_{n}'
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    # __import__('ipdb').set_trace()
    contents = []
    for d in dirs:  # e.g., 2c
        qd = os.path.join(input_dir, d)
        assert os.path.isdir(qd), f'{qd} is not a path'
        new_d = os.path.join(output_dir, d)
        if not os.path.exists(new_d):
            os.mkdir(new_d)
        fn_selected = os.listdir(qd)[0: n]

        sqls =  []

        fp_n = os.path.join(new_d, f'{d}_{n}.sql')
        for fn in fn_selected:
            fp =  os.path.join(qd, fn)
            with open(fp, 'r') as f:
                sql = f.read().replace('\n', ' ').strip() + ';'
                sqls.append(sql)

        with open(fp_n, 'w') as f:
            content = '\n'.join(sqls)
            contents.append(content)
            f.write(content)
    # __import__('ipdb').set_trace()
    if args.to1:
        sql_fn = os.path.join(output_dir, 'concat.sql')
        with open(sql_fn, 'w') as f:
            all_sqls =  '\n'.join(contents)
            f.write(all_sqls)



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_dir', type=str, default='./imdb-sqls')
    parser.add_argument('--n', type=int, default=3)
    parser.add_argument('--to1', type=bool, default=False)
    args = parser.parse_args()
    main(args)
