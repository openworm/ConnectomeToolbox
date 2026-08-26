from cect import print_

from cect.Neurotransmitters import GENERIC_CHEM_SYN_CLASS, GENERIC_ELEC_SYN_CLASS
from cect.Utils import get_connectome_dataset
from cect import __version__ as cect_version
from cect.Cells import is_known_cell
from cect.Comparison import get_improved_reader_name

import modelspec
from modelspec import field, instance_of
from modelspec.base_types import Base
from typing import List
from datetime import date
import yaml
import sys
import numpy as np
import importlib

import unittest


def _latexify(text):
    """
    Convert a string to a LaTeX-friendly format by escaping special characters and replacing certain substrings.
    """
    return (
        text.replace("{", "\\{")
        .replace("}", "\\}")
        .replace("_C. elegans_", "\\celegans{}")
        .replace("C. elegans", "\\celegans{}")
        .replace("_", "\\_")
        .replace("&", "\\&")
        .replace("%", "\\%")
        .replace("$", "\\$")
        .replace("Δ", "\\Delta{}")
        .replace("<sup>", "$^")
        .replace("</sup>", "$")
        .replace("<sub>", "$_")
        .replace("</sub>", "$")
        .replace("#", "\\#")
        .replace("~", "\\textasciitilde{}")
    )


class TestExpectedConnections(unittest.TestCase):
    MISMATCH = "Mismatch"

    last_weight = None

    def test_all(self):

        validation_md = "# Validation status of Data Readers\n\n"

        latex_md = """\\footnotesize
\\begin{longtable}{>{\\raggedright\\arraybackslash}p{0.12\\textwidth}>{\\raggedright\\arraybackslash}p{0.16\\textwidth}>{\\raggedright\\arraybackslash}p{0.30\\textwidth}>{\\raggedright\\arraybackslash}p{0.30\\textwidth}}
  \\caption{List of all datasets in the \\celegans{} Connectome Toolbox}\\label{tab:dataset-table}\\\\
  \\toprule%
  \\textbf{Original publication} & \\textbf{Reference/links} & \\textbf{Description} & \\textbf{Weight} \\\\
  \\midrule%
  \\endfirsthead
  \\caption[]{(continued)}\\\\
  \\toprule%
  \\textbf{Original publication} & \\textbf{Reference/links} & \\textbf{Description} & \\textbf{Weight} \\\\
  \\midrule%
  \\endhead
  \\midrule
  \\multicolumn{4}{r}{\\footnotesize\\itshape Continued on next page}\\\\
  \\endfoot
  \\bottomrule
  \\endlastfoot
"""

        data_readers = {
            "WhiteEtAl1986": [
                "DurbinJSHDataReader",
                "DurbinN2UDataReader",
                "White_whole",
            ],
            "VarshneyEtAl2011": ["VarshneyDataReader"],
            "BentleyEtAl2016": [
                "Bentley2016MAReader",
                "Bentley2016PepReader",
            ],
            "CookEtAl2019": ["Cook2019HermReader", "Cook2019MaleReader"],
            "CookEtAl2020": ["Cook2020DataReader"],
            "Brittin2021": ["BrittinDataReader"],
            "WitvlietEtAl2021": [
                "WitvlietDataReader1",
                "WitvlietDataReader2",
                "WitvlietDataReader3",
                "WitvlietDataReader4",
                "WitvlietDataReader5",
                "WitvlietDataReader6",
                "WitvlietDataReader7",
                "WitvlietDataReader8",
            ],
            "RandiEtAl2023": ["WormNeuroAtlasFuncReader"],
            "RipollSanchezEtAl2023": [
                "RipollSanchezShortRangeReader",
                "RipollSanchezMidRangeReader",
                "RipollSanchezLongRangeReader",
            ],
            "YimEtAl2024": [
                "Yim2024NonNormDataReader",
                "Yim2024DataReader",
                "Yim2024ContactomeNonNormDataReader",
                "Yim2024ContactomeDataReader",
            ],
            "WangEtAl2024": ["Wang2024HermReader", "Wang2024MaleReader"],
        }
        """
        data_readers = {
            "RipollSanchezEtAl2023": [
                "RipollSanchezShortRangeReader",
            ]
        }
        data_readers = {
        "WitvlietEtAl2021": [
                "WitvlietDataReader1",
                "WitvlietDataReader2",
                "WitvlietDataReader3",
                "WitvlietDataReader4",
                "WitvlietDataReader5",
                "WitvlietDataReader6",
                "WitvlietDataReader7",
                "WitvlietDataReader8",
            ]
        }"""

        for data_set in data_readers:
            validation_md += f"## {data_set}\n\n"
            with open(__file__.replace("Validator.py", f"{data_set}.md"), "r") as f:
                validation_md += f.read() + "\n\n"

            pub = (
                data_set.replace("_", "")
                .replace("EtAl", "")
                .replace("GleesonModel", "Gleeson2018")
                .replace("OlivaresModel", "Olivares2021")
            )
            latex_md += "\n  \\multirow{%i}{\\linewidth}{\\cite{%s}}" % (
                len(data_readers[data_set]),
                pub,
            )

            for data_reader in data_readers[data_set]:
                print_(f"Validating reader: {data_reader}...")

                report, latex = self.load_and_check_expected_data(data_reader, data_set)
                validation_md += report + "\n\n"
                latex_md += latex

            latex_md += "  \\midrule%\n"

        val_md = __file__.replace("Validator.py", "../../docs/Validation.md")
        with open(val_md, "w") as f:
            f.write(validation_md)
            print_(f"Validation report written to {val_md}")

        tex_md = __file__.replace("Validator.py", "../../docs/dataset-table.tex")
        with open(tex_md, "w") as f:
            f.write(latex_md + "\\end{longtable}\n\\normalsize\n")
            print_(f"Latex table written to {tex_md}")

        assert self.MISMATCH not in validation_md and "False" not in validation_md, (
            "Validation failed for some connections. See Validation.md for details."
        )

    def load_and_check_expected_data(self, data_reader, data_set):

        report = ""
        latex = ""

        reader_module = importlib.import_module(f"cect.readers.{data_reader}")

        reader_ref = reader_module.NAME
        ref = get_improved_reader_name(reader_ref)

        description = "TODO"
        if hasattr(reader_module, "DATASET_DESCRIPTION"):
            description = reader_module.DATASET_DESCRIPTION
        weight = "TODO"
        if hasattr(reader_module, "WEIGHTS"):
            weight = _latexify(reader_module.WEIGHTS)

            if weight == self.last_weight:
                weight = "\\emph{(Same as above)}"
            else:
                self.last_weight = weight

        matrix_url = f"https://openworm.org/ConnectomeToolbox/{reader_ref}_data"
        val_ref = data_set.lower()
        if "etal" not in val_ref:
            val_ref = val_ref.replace("202", "etal202")
        validation_url = f"https://openworm.org/ConnectomeToolbox/Validation#{val_ref}"

        ref_url = f"{ref} \\newline \\href{{{matrix_url}}}{{Matrix}} | \\href{{{validation_url}}}{{Validation}} \\newline "

        latex += f"  & {ref_url} & {_latexify(description)} \\newline & "
        latex += f" {weight} \\\\\n"

        expected_data_folder = __file__.replace("Validator.py", "")
        expected_data_file = f"{expected_data_folder}/{data_reader}_expected_data.yaml"

        try:
            with open(expected_data_file, "r") as f:
                print_(
                    f"Loading expected data for {data_reader} from {expected_data_file}..."
                )
                expected_data = ReaderExpectedData.from_yaml(f)

            self.assertIsInstance(expected_data, ReaderExpectedData)
            self.assertEqual(expected_data.reader, data_reader)

            if len(sys.argv) > 1 and sys.argv[1] == "0":  # so not quick...
                from_cache = False
            else:
                from_cache = True
            print_(
                " --- Loading connectome dataset for reader %s with from_cache=%s... (%s)"
                % (reader_ref, from_cache, sys.argv)
            )

            ref = reader_ref

            report += f"\n### Validation tests for [{data_reader}]({ref}_data.md) \n\n"

            for conn_list in expected_data.connection_lists:
                syn_class = conn_list["synapse"]
                if syn_class == GENERIC_CHEM_SYN_CLASS:
                    syn_info = "Chemical synaptic"
                elif syn_class == GENERIC_ELEC_SYN_CLASS:
                    syn_info = "Electrical"
                else:
                    syn_info = f"{syn_class}"

                conn_dataset = get_connectome_dataset(reader_ref, from_cache=from_cache)

                view_info = ""
                if "view" in conn_list:
                    view_id = conn_list["view"]

                    from cect.ConnectomeView import get_view

                    view = get_view(view_id)
                    view_info = f"\n\n**Note:** only cells/connections in ConnectomeView: **{view_id}** included ({view.description})"

                    conn_dataset = conn_dataset.get_connectome_view(view)

                print_(conn_dataset.summary())

                print_(
                    f"Checking connection list: {conn_list}, {syn_info} {view_info}..."
                )

                report += f"\n#### {syn_info} connections{view_info}\n\n"

                report += "| Pre      | Post | Expected weight | Match |\n|----------|------|-----------------|-------|\n"

                for conn in conn_list["connections"]:
                    print_(f"Checking connection: {conn}...")
                    w = conn_dataset.get_connection_weight(
                        conn["pre"], conn["post"], synclass=conn_list["synapse"]
                    )
                    self.assertIsNotNone(
                        w, f"Connection weight for {conn} should not be None"
                    )
                    match_info = (
                        "Yes" if w == conn["weight"] else f"{self.MISMATCH}: {w}"
                    )
                    print_(match_info)
                    report += f"| {conn['pre']} | {conn['post']} | {conn['weight']} | {match_info} |\n"

                if syn_class == GENERIC_ELEC_SYN_CLASS:
                    arr = conn_dataset.connections[syn_class]
                    arrT = arr.T
                    symm = np.array_equal(arr, arrT)
                    asymm = ""
                    if not symm:
                        asymm = ", %s" % (
                            "; ".join(
                                conn_dataset.get_asymmetric_connections_info(syn_class)
                            )
                        )
                    report += f"\nElectrical synapse. Symmetric connectivity matrix: **{symm}**{asymm}\n"

                for node in conn_dataset.nodes:
                    if not is_known_cell(node, allow_modelled_neurons=True):
                        report += f"\nError: Cell {node} is not in the list of known cells (from Cook et al. 2019)!\n"

                if "total_nonzero_conns" in conn_list:
                    num_nz = conn_list["total_nonzero_conns"]
                    cdarr = conn_dataset.connections[syn_class]
                    num_nz_cd = np.count_nonzero(cdarr)
                    match_info = (
                        "matches"
                        if num_nz == num_nz_cd
                        else f"{self.MISMATCH}: **{num_nz_cd}**"
                    )
                    report += (
                        "\nExpected number of nonzero connection weights: **%i** (%s)\n"
                        % (num_nz, match_info)
                    )
                else:
                    report += "\nTODO: add total num nonzero connections\n"

                if "total_weight" in conn_list:
                    total_w = conn_list["total_weight"]
                    cdarr = conn_dataset.connections[syn_class]
                    total_w_cd = np.sum(cdarr)
                    match_info = (
                        "matches"
                        if total_w == total_w_cd
                        else f"{self.MISMATCH}: **{total_w_cd}**"
                    )
                    report += (
                        "\nExpected total weight of connections: **%g** (%s)\n"
                        % (
                            total_w,
                            match_info,
                        )
                    )

                if "num_cells" in conn_list:
                    num_cells = conn_list["num_cells"]
                    cdarr = conn_dataset.connections[syn_class]
                    num_cells_cd = cdarr.shape[
                        0
                    ]  # number of rows in the connectivity matrix
                    match_info = (
                        "matches"
                        if num_cells == num_cells_cd
                        else f"{self.MISMATCH}: **{num_cells_cd}**"
                    )
                    report += "\nExpected number of cells: **%i** (%s)\n" % (
                        num_cells,
                        match_info,
                    )

            report += f"\n_Validation **{'PASSED' if self.MISMATCH not in report else 'FAILED'}** on {date.today().isoformat()} with cect v{cect_version}_\n\n"

        except Exception as e:
            if "No such file" in str(e):
                print_(f"Error loading expected data for {data_reader}: {e}")
                report += (
                    f"\n**TODO: add expected data file: {expected_data_file}**: {e}\n\n"
                )
            else:
                raise Exception(
                    f"Error loading or checking expected data for {data_reader}: {e}"
                )

        return report, latex


@modelspec.define
class Connection(Base):
    """
    A single connection between two cells.

    Args:
        pre: The pre-synaptic cell
        post: The post-synaptic cell
        weight: The weight of the connection, which could be the number of synapses or a normalized value.
    """

    pre: str = field(validator=instance_of(str))
    post: str = field(validator=instance_of(str))
    weight: float = field(validator=instance_of(float))


@modelspec.define
class ConnectionList(Base):
    """
    A model of a list of connections of a specific synapse type.

    Args:
        synapse: The type of synapse
        total_nonzero_conns: Total nonzero connections
        total_weight: Total weight of connections (optional)
        num_cells: Number of cells (optional)
        view: An optional string specifying a ConnectomeView to use, e.g. Neurons, Pharynx, etc. Numbers of conns will be checked inside that view
        comment: A comment about how the data was found, e.g. taken from a spreadsheet
        connections: The list of connections of this type
    """

    synapse: str = field(validator=instance_of(str))
    total_nonzero_conns: int = field(validator=instance_of(int))
    total_weight: float = field(validator=instance_of(float))
    num_cells: int = field(validator=instance_of(int))
    view: str = field(validator=instance_of(str))
    comment: str = field(validator=instance_of(str))
    connections: List[Connection] = field(factory=list)


@modelspec.define
class ReaderExpectedData(Base):
    """
    A model of expected data for a specific reader.

    Args:
        reader: The name of the reader
        connection_lists: The list of connection lists for this reader
    """

    reader: str = field(validator=instance_of(str))
    connection_lists: List[ConnectionList] = field(factory=list)

    def get_connection_list_by_synapse(self, synapse_type):
        """
        Get the connection list for a specific synapse type.

        Args:
            synapse_type: The type of synapse to get the connection list for


        Returns:            The connection list for the specified synapse type, or None if not found.
        """
        for conn_list in self.connection_lists:
            if (
                isinstance(conn_list, dict)
                and "synapse" in conn_list
                and conn_list["synapse"] == synapse_type
            ):
                return conn_list
            if conn_list.synapse == synapse_type:
                return conn_list
        return None


def generate_reader_exp_data_obj(reader_name, source_files, additional_comment=""):
    """
    A function to generate a ReaderExpectedData object which will list expected data as visually extracted from a source file, e.g. an Excel spreadsheet.

    Args:
        reader_name: The name of the reader
        source_files: A dict of syn types vs paths to the source files

    Returns:
        A ReaderExpectedData object with the expected data for the reader.
    """
    # This is a placeholder implementation. In a real implementation, you would read the source files and extract the expected data.
    expected_data = ReaderExpectedData(reader=reader_name)

    for syn_class, source_file in source_files.items():
        chem_conns = ConnectionList(
            synapse=syn_class,
            comment=f"Data visually read in from {source_file}. {additional_comment}",
            total_nonzero_conns=-1,
        )

    expected_data.connection_lists.append(chem_conns)

    return expected_data


if __name__ == "__main__":
    if "-test" in sys.argv:
        expected_data_folder = __file__.replace("Validator.py", "")

        yim_data = generate_reader_exp_data_obj(
            reader_name="Yim2024DataReader",
            source_files={GENERIC_CHEM_SYN_CLASS: "41467_2024_45943_MOESM6_ESM.xlsx"},
        )

        chem_conns = yim_data.get_connection_list_by_synapse(GENERIC_CHEM_SYN_CLASS)

        chem_conns.connections.append(
            Connection(pre="ADFR", post="AFDR", weight=0.428024049927915)
        )
        chem_conns.connections.append(
            Connection(pre="SMBDL", post="RMED", weight=6.01978135910464)
        )
        chem_conns.connections.append(
            Connection(pre="ASHL", post="RIPL", weight=1.20804164634321)
        )
        chem_conns.total_nonzero_conns = 2198

        exp_data_file = f"{expected_data_folder}/{yim_data.reader}_expected_data.yaml"
        with open(exp_data_file, "w") as f:
            yaml.dump(yim_data.to_dict(), f, default_flow_style=False)

        print_(f"Expected data for YIM reader written to {exp_data_file}")

    else:
        print_(" --- Running validator tests...")
        # Don't let unittest parse our cache flag (e.g. the "0"/"1" arg);
        # it would try to interpret it as a test name. Pass only argv[0].
        unittest.main(argv=[sys.argv[0]])

        sys.exit(0)
