import os
from typing import List
import argparse


def transform2rbr(sql_fn: str, num_rounds: int, round_size: int) -> List[str]:
    rearranged_sqls = []
    # __import__('ipdb').set_trace()
    repeat_num = 0
    with open(sql_fn, 'r') as f:
        sqls = f.readlines()
        assert len(sqls) >= num_rounds * round_size, f"the needed {num_rounds*round_size} is beyond {len(sqls)} input sqls"
        repeat_num = int(len(sqls)/round_size)
    for r in range(num_rounds):
        round_sqls = [sqls[repeat_num*i + r] for i in range(round_size)]  # round_size
        rearranged_sqls.extend(round_sqls)

    return rearranged_sqls

def save_sqls(sqls: List[str], output_fn: str) -> None:
    with open(output_fn, 'w') as f:
        contents = ''.join(sqls)
        f.write((contents))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str, default='./imdb-sqls_2/concat.sql')
    parser.add_argument('--num_rounds', type=int, default=2)
    parser.add_argument('--round_size', type=int, default=16)
    parser.add_argument('--type', type=int, default=1)
    args = parser.parse_args()

    t_type = args.type
    fp = args.input
    # __import__('ipdb').set_trace()
    res = fp.split('/')
    dir = '/'.join(res[:-1])
    fn = res[-1]
    base_name, ext = fn.split('.')
    output_fn = os.path.join(dir, f'{base_name}_type{t_type}.{ext}')
    n = args.num_rounds
    round_size = args.round_size

    if t_type == 1:  # rounds by rounds
        sqls = transform2rbr(fp, n, round_size)
        save_sqls(sqls, output_fn)
    else:
        raise ValueError(f"{t_type} not supported yet")

if __name__ == "__main__":
    main()
