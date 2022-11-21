from typing import Any, Dict, Tuple

import matplotlib as mpl
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


def nudge(pos: Dict[int, np.ndarray], x_shift: float, y_shift: float):
    """Nudge position to position attributes"""
    return {n: (x + x_shift, y + y_shift) for n, (x, y) in pos.items()}


def draw_graph_with_attributes(
    G: nx.Graph,
    props: Dict[int, Any] = None,
    pos: Dict[int, np.ndarray] = None,
    figsize: Tuple[int, int] = (8, 8),
    x_nudge: float = 0.0,
    y_nudge: float = 0.07,
    ax: mpl.axes.Axes = None,
    font_color: str = "darkgreen",
):
    """Draw a graph with node labels and attributes"""
    if ax is None:
        fig, ax = plt.subplots(1, 1, figsize=figsize)

    if pos is None:
        pos = nx.spring_layout(G)

    nx.draw_networkx(G, pos=pos, with_labels=True, ax=ax)
    pos_nudged = nudge(pos, x_nudge, y_nudge)
    if props is None:
        props = nx.get_node_attributes(G, "x")
        props = {
            node_id: np.array2string(np.array(x), precision=2, separator=",")
            for node_id, x in props.items()
        }
    nx.draw_networkx_labels(
        G, pos=pos_nudged, labels=props, ax=ax, font_color=font_color
    )
    ax.set_ylim(tuple(i * 1.1 for i in ax.get_ylim()))
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["left"].set_visible(False)
