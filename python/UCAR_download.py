import os
import argparse
import subprocess
import pandas as pd
import concurrent.futures

parser = argparse.ArgumentParser()
parser.add_argument("-yys", type=int, required=True)
parser.add_argument("-yye", type=int, required=True)
parser.add_argument("-w", type=int, required=True)
args = parser.parse_args()

yys = args.yys
yye = args.yye
num_workers = args.w

dir_out = "/home/arturo/Downloads/UCAR"

# Región de Sudamérica
lat_min, lat_max, lon_min, lon_max = -50, 13, -85, -45

# Lista de fechas diarias a las 12:00
dates_list = pd.date_range(
    start=f"{yys}-01-01 12:00:00",
    end=f"{yye}-12-31 12:00:00",
    freq="D"
).strftime("%Y-%m-%d %H:%M:%S").tolist()

def download_litte_r_for_date(date_str):
    filename = f'SURFACE_OBS:{date_str.split(" ")[0].replace("-", "")}12.csv'
    filename_dir = os.path.join(dir_out, filename)
    if os.path.isfile(filename_dir) and os.path.getsize(filename_dir) > 0:
        print(f"File {filename} already exists and is not empty. Skipping download.")
        # pass
    else:
        subprocess.run([
            "python",
            "./function/download_litte_r.py",
            "-t", date_str,
            "-o", dir_out,
            "-lat_min", str(lat_min),
            "-lat_max", str(lat_max),
            "-lon_min", str(lon_min),
            "-lon_max", str(lon_max)
        ])

with concurrent.futures.ThreadPoolExecutor(max_workers=num_workers) as executor:
    executor.map(download_litte_r_for_date, dates_list)
