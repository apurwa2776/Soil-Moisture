!pip install pandas rasterio netCDF4 rioxarray
import os
import re
import sys
import random
from pathlib import Path

import requests
import json
import xml.etree.ElementTree as ET
import certifi

import pandas as pd
import numpy as np

import rasterio
import matplotlib.pyplot as plt
import matplotlib.image
from rasterio.windows import Window

import netCDF4 as nc

import rioxarray
from rasterio.control import GroundControlPoint