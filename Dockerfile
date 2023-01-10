FROM continuumio/miniconda3:4.10.3p1

WORKDIR /ICE-CREAM-REVIEWS

COPY README.md /ICE-CREAM-REVIEWS
COPY data /ICE-CREAM-REVIEWS/data
COPY images /ICE-CREAM-REVIEWS/images
COPY notebooks /ICE-CREAM-REVIEWS/notebooks

RUN conda install \
    numpy \
    pandas \
    matplotlib \
    jupyterlab
CMD ["jupyter-lab","--ip=0.0.0.0","--no-browser","--allow-root"]