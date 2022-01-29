import os
import sys
import warnings
import skl2onnx
import pydata_sphinx_theme

sys.path.append(os.path.abspath('exts'))
from github_link import make_linkcode_resolve  # noqa


# -- Project information -----------------------------------------------------

project = 'Introduction to ONNX'
copyright = '2022'
author = '?'
version = "0.1"
release = version

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.imgmath',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    "sphinx.ext.autodoc",
    'sphinx.ext.githubpages',
    "sphinx_gallery.gen_gallery",
    'sphinx.ext.autodoc',
    'sphinx.ext.graphviz',
    'matplotlib.sphinxext.plot_directive',
    'pyquickhelper.sphinxext.sphinx_cmdref_extension',
    'pyquickhelper.sphinxext.sphinx_collapse_extension',
    'pyquickhelper.sphinxext.sphinx_docassert_extension',
    'pyquickhelper.sphinxext.sphinx_epkg_extension',
    'pyquickhelper.sphinxext.sphinx_exref_extension',
    'pyquickhelper.sphinxext.sphinx_faqref_extension',
    'pyquickhelper.sphinxext.sphinx_gdot_extension',
    'pyquickhelper.sphinxext.sphinx_runpython_extension',
    "sphinxcontrib.blockdiag",
]

templates_path = ['_templates']
source_suffix = ['.rst']

master_doc = 'index'
language = "en"
exclude_patterns = []
pygments_style = 'default'

# -- Options for HTML output -------------------------------------------------

html_theme = "sphinx_mo"
html_static_path = ['_static']
html_theme = "pydata_sphinx_theme"
html_theme_path = pydata_sphinx_theme.get_html_theme_path()
html_logo = "logo_main.png"

# -- Options for graphviz ----------------------------------------------------

graphviz_output_format = "svg"

# -- Options for intersphinx extension ---------------------------------------

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'https://docs.python.org/': None}

# -- Options for Sphinx Gallery ----------------------------------------------

sphinx_gallery_conf = {
    'examples_dirs': ['examples'],
    'gallery_dirs': ['auto_examples', 'auto_tutorial'],
    'capture_repr': ('_repr_html_', '__repr__'),
    'ignore_repr_types': r'matplotlib.text|matplotlib.axes',
    'binder': {
        'org': 'onnx',
        'repo': '.',
        'notebooks_dir': 'auto_examples',
        'binderhub_url': 'https://mybinder.org',
        'branch': 'master',
        'dependencies': './requirements.txt'
    },
}

epkg_dictionary = {
    'C': 'https://en.wikipedia.org/wiki/C_(programming_language)',
    'C++': 'https://en.wikipedia.org/wiki/C%2B%2B',
    'cython': 'https://cython.org/',
    'DOT': 'https://www.graphviz.org/doc/info/lang.html',
    'ImageNet': 'http://www.image-net.org/',
    'LightGBM': 'https://lightgbm.readthedocs.io/en/latest/',
    'lightgbm': 'https://lightgbm.readthedocs.io/en/latest/',
    'mlprodict':
        'http://www.xavierdupre.fr/app/mlprodict/helpsphinx/index.html',
    'NMF':
        'https://scikit-learn.org/stable/modules/generated/'
        'sklearn.decomposition.NMF.html',
    'numpy': 'https://numpy.org/',
    'onnx': 'https://github.com/onnx/onnx',
    'ONNX': 'https://onnx.ai/',
    'ONNX operators':
        'https://github.com/onnx/onnx/blob/master/docs/Operators.md',
    'ONNX ML operators':
        'https://github.com/onnx/onnx/blob/master/docs/Operators-ml.md',
    'onnxmltools': 'https://github.com/onnx/onnxmltools',
    'OnnxPipeline':
        'http://www.xavierdupre.fr/app/mlprodict/helpsphinx/mlprodict/'
        'sklapi/onnx_pipeline.html?highlight=onnxpipeline',
    'onnxruntime': 'https://microsoft.github.io/onnxruntime/',
    'openmp': 'https://en.wikipedia.org/wiki/OpenMP',
    'pyinstrument': 'https://github.com/joerick/pyinstrument',
    'python': 'https://www.python.org/',
    'pytorch': 'https://pytorch.org/',
    'scikit-learn': 'https://scikit-learn.org/stable/',
    'skorch': 'https://skorch.readthedocs.io/en/stable/',
    'sklearn-onnx': 'https://github.com/onnx/sklearn-onnx',
    'sphinx-gallery': 'https://github.com/sphinx-gallery/sphinx-gallery',
    'xgboost': 'https://xgboost.readthedocs.io/en/latest/',
    'XGBoost': 'https://xgboost.readthedocs.io/en/latest/',
}

warnings.filterwarnings("ignore", category=FutureWarning)

# -- Setup actions -----------------------------------------------------------


def setup(app):
    # Placeholder to initialize the folder before
    # generating the documentation.
    return app

extensions.extend([
    "sphinxcontrib.blockdiag",
])

html_theme_options = {
    "github_user": "sdpython",
    "github_repo": "onnxcustom",
    "github_version": "master",
    "collapse_navigation": True,
    "show_nav_level": 2,
}

blog_root = "http://www.xavierdupre.fr/app/onnxcustom/helpsphinx/"

html_css_files = ['my-styles.css']

html_logo = "phdoc_static/project_ico.png"
html_sidebars = {}
language = "en"

mathdef_link_only = True

custom_preamble = """\n
\\newcommand{\\vecteur}[2]{\\pa{#1,\\dots,#2}}
\\newcommand{\\N}[0]{\\mathbb{N}}
\\newcommand{\\indicatrice}[1]{\\mathbf{1\\!\\!1}_{\\acc{#1}}}
\\newcommand{\\infegal}[0]{\\leqslant}
\\newcommand{\\supegal}[0]{\\geqslant}
\\newcommand{\\ensemble}[2]{\\acc{#1,\\dots,#2}}
\\newcommand{\\fleche}[1]{\\overrightarrow{ #1 }}
\\newcommand{\\intervalle}[2]{\\left\\{#1,\\cdots,#2\\right\\}}
\\newcommand{\\loinormale}[2]{{\\cal N}\\pa{#1,#2}}
\\newcommand{\\independant}[0]{\\;\\makebox[3ex]
{\\makebox[0ex]{\\rule[-0.2ex]{3ex}{.1ex}}\\!\\!\\!\\!\\makebox[.5ex][l]
{\\rule[-.2ex]{.1ex}{2ex}}\\makebox[.5ex][l]{\\rule[-.2ex]{.1ex}{2ex}}} \\,\\,}
\\newcommand{\\esp}{\\mathbb{E}}
\\newcommand{\\pr}[1]{\\mathbb{P}\\pa{#1}}
\\newcommand{\\loi}[0]{{\\cal L}}
\\newcommand{\\vecteurno}[2]{#1,\\dots,#2}
\\newcommand{\\norm}[1]{\\left\\Vert#1\\right\\Vert}
\\newcommand{\\dans}[0]{\\rightarrow}
\\newcommand{\\partialfrac}[2]{\\frac{\\partial #1}{\\partial #2}}
\\newcommand{\\partialdfrac}[2]{\\dfrac{\\partial #1}{\\partial #2}}
\\newcommand{\\loimultinomiale}[1]{{\\cal M}\\pa{#1}}
\\newcommand{\\trace}[1]{tr\\pa{#1}}
\\newcommand{\\abs}[1]{\\left|#1\\right|}
"""

# \\usepackage{eepic}
imgmath_latex_preamble = custom_preamble
latex_elements = {
    'preamble': custom_preamble
}

intersphinx_mapping.update({
    'torch': ('https://pytorch.org/docs/stable/', None),
    'mlprodict':
        ('http://www.xavierdupre.fr/app/mlprodict/helpsphinx/', None),
    'numpy': ('https://docs.scipy.org/doc/numpy/', None),
    'onnxcustom':
        ('http://www.xavierdupre.fr/app/onnxcustom/helpsphinx/', None),
    'pandas': ('https://pandas.pydata.org/pandas-docs/stable/', None),
    'pandas_streaming':
        ('http://www.xavierdupre.fr/app/pyquickhelper/helpsphinx/', None),
    'pyquickhelper':
        ('http://www.xavierdupre.fr/app/pyquickhelper/helpsphinx/', None),
    'python': (
        'https://docs.python.org/{.major}'.format(sys.version_info),
        None),
    'scikit-learn': ('https://scikit-learn.org/stable/', None),
    'scipy': ('https://docs.scipy.org/doc/scipy/reference', None),
    'sklearn': ('https://scikit-learn.org/stable/', None)
})


epkg_dictionary.update({
    'C': 'https://en.wikipedia.org/wiki/C_(programming_language)',
    'C++': 'https://en.wikipedia.org/wiki/C%2B%2B',
    'chrome-tracing':
        'https://www.chromium.org/developers/how-tos/trace-event-profiling-tool',
    'cmake': 'https://cmake.org/',
    'COO': 'https://en.wikipedia.org/wiki/Sparse_matrix#Coordinate_list_(COO)',
    'CSR':
        'https://en.wikipedia.org/wiki/Sparse_matrix'
        '#Compressed_sparse_row_(CSR,_CRS_or_Yale_format)',
    'cudnn': 'https://developer.nvidia.com/cudnn',
    'cython': 'https://cython.org/',
    'DLPack': 'https://github.com/dmlc/dlpack',
    'docker': 'https://en.wikipedia.org/wiki/Docker_(software)',
    'DOT': 'https://www.graphviz.org/doc/info/lang.html',
    'ImageNet': 'http://www.image-net.org/',
    'LightGBM': 'https://lightgbm.readthedocs.io/en/latest/',
    'lightgbm': 'https://lightgbm.readthedocs.io/en/latest/',
    'mlprodict':
        'http://www.xavierdupre.fr/app/mlprodict/helpsphinx/index.html',
    'myst-parser': 'https://myst-parser.readthedocs.io/en/latest/',
    'nccl': 'https://developer.nvidia.com/nccl',
    'netron': 'https://github.com/lutzroeder/netron',
    'NMF':
        'https://scikit-learn.org/stable/modules/generated/'
        'sklearn.decomposition.NMF.html',
    'numpy': 'https://numpy.org/',
    'nvprof': 'https://docs.nvidia.com/cuda/profiler-users-guide/index.html',
    'onnx': 'https://github.com/onnx/onnx',
    'ONNX': 'https://onnx.ai/',
    'ONNX operators':
        'https://github.com/onnx/onnx/blob/master/docs/Operators.md',
    'ONNX ML Operators':
        'https://github.com/onnx/onnx/blob/master/docs/Operators-ml.md',
    'ONNX Zoo': 'https://github.com/onnx/models',
    'onnxmltools': 'https://github.com/onnx/onnxmltools',
    'onnxruntime': 'https://microsoft.github.io/onnxruntime/',
    'onnxruntime-extensions':
        'https://github.com/microsoft/onnxruntime-extensions',
    'onnxruntime-training':
        'https://github.com/microsoft/onnxruntime/tree/master/orttraining',
    'openmp': 'https://en.wikipedia.org/wiki/OpenMP',
    'openmpi': 'https://www.open-mpi.org/',
    'pandas_streaming':
        'http://www.xavierdupre.fr/app/pandas_streaming/helpsphinx/index.html',
    'protobuf': 'https://developers.google.com/protocol-buffers',
    'py-spy': 'https://github.com/benfred/py-spy',
    'pyinstrument': 'https://github.com/joerick/pyinstrument',
    'pyspark': 'https://spark.apache.org/docs/latest/api/python/',
    'python': 'https://www.python.org/',
    'pytorch': 'https://pytorch.org/',
    'scikit-learn': 'https://scikit-learn.org/stable/',
    'skorch': 'https://skorch.readthedocs.io/en/stable/',
    'sklearn-onnx': 'https://github.com/onnx/sklearn-onnx',
    'sphinx-gallery': 'https://github.com/sphinx-gallery/sphinx-gallery',
    'sqlite3': 'https://docs.python.org/3/library/sqlite3.html',
    'Stochastic Gradient Descent':
        'https://en.wikipedia.org/wiki/Stochastic_gradient_descent',
    'Tensor': 'https://en.wikipedia.org/wiki/Tensor',
    'tensor': 'https://en.wikipedia.org/wiki/Tensor',
    'tensorflow': 'https://www.tensorflow.org/',
    'tensorflow-onnx': 'https://github.com/onnx/tensorflow-onnx',
    'tf2onnx': 'https://github.com/onnx/tensorflow-onnx',
    'torch': 'https://pytorch.org/',
    'tqdm': 'https://github.com/tqdm/tqdm',
    'xgboost': 'https://xgboost.readthedocs.io/en/latest/',
    'XGBoost': 'https://xgboost.readthedocs.io/en/latest/',
    'WSL': 'https://docs.microsoft.com/en-us/windows/wsl/install',
})

# APIs, links which should be replaced.

epkg_dictionary.update({
    'C_OrtDevice':
        'http://www.xavierdupre.fr/app/onnxcustom/helpsphinx/api/'
        'onnxruntime_python/helpers.html#c-class-ortdevice',
    'C_OrtValue':
        'http://www.xavierdupre.fr/app/onnxcustom/helpsphinx/'
        'onnxmd/onnxruntime_python/ortvalue.html#c-class-ortvaluevector',
    'C_SparseTensor':
        'http://www.xavierdupre.fr/app/onnxruntime_training/'
        'helpsphinx/api/tensors.html#sparsetensor',
    'Contrib Operators':
        'http://www.xavierdupre.fr/app/onnxcustom/helpsphinx/onnxmd/'
        'onnxruntime_docs/ContribOperators.html',
    'Gemm':
        'http://www.xavierdupre.fr/app/onnxcustom/helpsphinx/onnxmd/'
        'onnx_docs/Operators.html#a-name-gemm-a-a-name-gemm-gemm-a',
    'If':
        'http://www.xavierdupre.fr/app/onnxcustom/helpsphinx/onnxmd/'
        'onnx_docs/Operators.html#a-name-if-a-a-name-if-if-a',
    'InferenceSession':
        'http://www.xavierdupre.fr/app/onnxcustom/helpsphinx/onnxmd/'
        'onnxruntime_python/inference.html'
        '#python-wrapper-for-inferencesession',
    'IOBinding':
        'http://www.xavierdupre.fr/app/onnxruntime_training/'
        'helpsphinx/api/tensors.html#iobinding',
    'IR':
        'http://www.xavierdupre.fr/app/onnxcustom/helpsphinx/onnxmd/'
        'onnx_docs/IR.html',
    'Loop':
        'http://www.xavierdupre.fr/app/onnxcustom/helpsphinx/onnxmd/'
        'onnx_docs/Operators.html#a-name-loop-a-a-name-loop-loop-a',
    'OnnxPipeline':
        'http://www.xavierdupre.fr/app/mlprodict/helpsphinx/mlprodict/'
        'sklapi/onnx_pipeline.html',
    'OneHotEncoder':
        'http://www.xavierdupre.fr/app/onnxcustom/helpsphinx/onnxmd/'
        'onnx_docs/Operators-ml.html?highlight=onehotencoding'
        '#a-name-ai-onnx-ml-onehotencoder-a-a-name-ai-onnx-'
        'ml-onehotencoder-ai-onnx-ml-onehotencoder-a',
    'ORTModule':
        'http://www.xavierdupre.fr/app/onnxcustom/helpsphinx/'
        'api/onnxruntime_python/training_torch.html#ortmodule',
    'OrtModuleGraphBuilder':
        'http://www.xavierdupre.fr/app/onnxcustom/helpsphinx/onnxmd/'
        'onnxruntime_python/training_partial.html'
        "#ortmodulegraphbuilder",
    'OrtModuleGraphBuilderConfiguration':
        'http://www.xavierdupre.fr/app/onnxcustom/helpsphinx/onnxmd/'
        'onnxruntime_python/training_partial.html'
        "#ortmodulegraphbuilderconfiguration",
    'OrtDevice':
        'http://www.xavierdupre.fr/app/onnxruntime_training/'
        'helpsphinx/api/tensors.html#ortdevice',
    'OrtValue':
        'http://www.xavierdupre.fr/app/onnxruntime_training/'
        'helpsphinx/api/tensors.html#ortvalue',
    'OrtValueCache':
        'http://www.xavierdupre.fr/app/onnxcustom/helpsphinx/onnxmd/'
        'onnxruntime_python/training_partial.html#ortvaluecache',
    'OrtValueVector':
        'http://www.xavierdupre.fr/app/onnxruntime_training/'
        'helpsphinx/api/training_session.html#ortvaluevector',
    'PartialGraphExecutionState':
        'http://www.xavierdupre.fr/app/onnxcustom/helpsphinx/onnxmd/'
        'onnxruntime_python/training_partial.html'
        "#partialgraphexecutionstate",
    'RunOptions':
        'http://www.xavierdupre.fr/app/onnxcustom/helpsphinx/onnxmd/'
        'onnxruntime_python/inference.html#runoptions',
    'Scan':
        'http://www.xavierdupre.fr/app/onnxcustom/helpsphinx/onnxmd/'
        'onnx_docs/Operators.html#a-name-scan-a-a-name-scan-scan-a',
    'SessionIOBinding':
        'http://www.xavierdupre.fr/app/onnxcustom/helpsphinx/api/'
        'onnxruntime_python/inference.html#'
        'onnxruntime.capi._pybind_state.SessionIOBinding',
    'SessionOptions':
        'http://www.xavierdupre.fr/app/onnxcustom/helpsphinx/onnxmd/'
        'onnxruntime_python/inference.html#sessionoptions',
    'SparseTensor':
        'http://www.xavierdupre.fr/app/onnxruntime_training/'
        'helpsphinx/api/tensors.html#sparsetensor',
    'TfIdfVectorizer':
        'http://www.xavierdupre.fr/app/onnxcustom/helpsphinx/onnxmd/'
        'onnx_docs/Operators.html#'
        'a-name-tfidfvectorizer-a-a-name-tfidfvectorizer-tfidfvectorizer-a',
    'TopK':
        'http://www.xavierdupre.fr/app/onnxcustom/helpsphinx/onnxmd/'
        'onnx_docs/Operators.html#a-name-topk-a-a-name-topk-topk-a',
    'TrainingAgent':
        'http://www.xavierdupre.fr/app/onnxcustom/helpsphinx/onnxmd/'
        'onnxruntime_python/training_partial.html'
        "#trainingagent",
    'TrainingParameters':
        'http://www.xavierdupre.fr/app/onnxcustom/helpsphinx/api/'
        'onnxruntime_python/training.html#trainingparameters',
    'TrainingSession':
        'http://www.xavierdupre.fr/app/onnxcustom/helpsphinx/api/'
        'onnxruntime_python/training.html#onnxruntime.TrainingSession',
    'Transpose':
        'http://www.xavierdupre.fr/app/onnxcustom/helpsphinx/onnxmd/'
        'onnx_docs/Operators.html'
        '#a-name-transpose-a-a-name-transpose-transpose-a',
    'TreeEnsembleRegressor':
        'https://github.com/onnx/onnx/blob/master/docs/Operators-ml.md'
        '#ai.onnx.ml.TreeEnsembleRegressor',
})


nblinks = {
    'alter_pipeline_for_debugging':
        'http://www.xavierdupre.fr/app/onnxcustom/helpsphinx/'
        'onnxcustom/helpers/pipeline.html'
        '#onnxcustom.helpers.pipeline.alter_pipeline_for_debugging',
}

warnings.filterwarnings("ignore", category=FutureWarning)
