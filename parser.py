import xml.etree.ElementTree as ET


def parse_from_string(data, save_file):
    root = ET.fromstring(data)

    # column and row hints are saved as 9th and 10th element of puzzle XML
    cols = root[1][9]
    rows = root[1][10]

    row_hints = []
    col_hints = []

    # save row hints to dedicated array
    for row in rows:
        row_hints.append([])
        for num in row:
            row_hints[-1].append(int(num.text))

    # save column hints to dedicated array
    for col in cols:
        col_hints.append([])
        for num in col:
            col_hints[-1].append(int(num.text))

    # format data and save them to given file
    f = open(save_file, 'w')
    f.write('{} '.format(len(row_hints)))
    f.write('{}\n'.format(len(col_hints)))
    f.write('{}\n'.format(row_hints))
    f.write('{}\n'.format(col_hints))
    f.close()


