# -*- coding: utf-8 -*-
import re
import os

p = re.compile(r'ret_dict = task(\d+)')


def test():
    d = os.path.abspath(os.path.join(os.path.abspath(__file__), '../../handlers'))
    fs = os.listdir(d)
    # print fs
    for f in fs:
        if f.endswith('py'):
            path = os.path.join(d, f)
            # print path
            files = []
            with open(path, 'r') as p_f:
                # print p_f.name
                for line in p_f.readlines():
                    # if re.match()
                    if p.search(line):
                        # print line
                        task_n = p.search(line).groups()[0]
                        # print task_n
                        new_l = '    ret_dict = copy.deepcopy(task%s)\n' % task_n
                        print new_l
                        files.append(new_l)
                        continue
                    files.append(line)
            with open(path, 'w') as w_f:
                w_f.writelines(files)


if __name__ == '__main__':
    test()