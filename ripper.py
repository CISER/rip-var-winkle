from typing import NamedTuple

import pyreadstat


class Variable(NamedTuple):
    name: str
    label: str
    values: list


class Result(NamedTuple):
    variables: list
    variable_count: int


def parse_metadata(meta):
    names = meta.column_names
    labels = meta.column_labels
    values = meta.variable_value_labels

    has_labels = 0 < len(labels) == len(names)

    variables = []

    for i, n in enumerate(names):
        name = n.strip()
        label = ""
        if has_labels and type(labels[i]) is str:
            label = labels[i].strip()
        value = values[n] if n in values else []

        variables.append(Variable(name, label, value)._asdict())

    return Result(variables, meta.number_columns)._asdict()


def parse_file(filename):
    if "sav" in filename.lower():
        df, meta = pyreadstat.read_sav(filename, apply_value_formats=True, metadataonly=True)
        return df, meta, False
    elif "por" in filename.lower():
        df, meta = pyreadstat.read_por(filename, apply_value_formats=True, metadataonly=True)
        return df, meta, False
    elif "sas7bdat" in filename.lower():
        df, meta = pyreadstat.read_sas7bdat(filename, metadataonly=True)
        return df, meta, False
    elif "xpt" in filename.lower():
        df, meta = pyreadstat.read_xport(filename, metadataonly=True)
        return df, meta, False
    elif "dta" in filename.lower():
        df, meta = pyreadstat.read_dta(filename, apply_value_formats=True, metadataonly=True)
        return df, meta, False
    else:
        return None, None, True
