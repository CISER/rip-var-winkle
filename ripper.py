from typing import NamedTuple

import pyreadstat


class Variable(NamedTuple):
    name: str
    label: str
    value_labels: list


class Result(NamedTuple):
    variables: list
    variable_count: int


def parse_metadata(meta):
    names = meta.column_names
    labels = meta.column_labels
    value_labels = meta.variable_value_labels

    has_labels = 0 < len(labels) == len(names)

    variables = []

    for i, n in enumerate(names):
        name = n.strip()
        label = ""
        if has_labels and type(labels[i]) is str:
            label = labels[i].strip()
        value_label = value_labels[n] if n in value_labels else []

        variables.append(Variable(name, label, value_label)._asdict())

    return Result(variables, meta.number_columns)._asdict()


def parse_file(filename):
    if "sav" in filename.lower():
        return pyreadstat.read_sav(filename, apply_value_formats=True, metadataonly=True)
    elif "por" in filename.lower():
        return pyreadstat.read_por(filename, apply_value_formats=True, metadataonly=True)
    elif "sas7bdat" in filename.lower():
        return pyreadstat.read_sas7bdat(filename, metadataonly=True)
    elif "dta" in filename.lower():
        return pyreadstat.read_dta(filename, apply_value_formats=True, metadataonly=True)
    else:
        raise SystemExit("Supplied file is not a supported type.")
