from fastapi import Body
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

# Sample data
students_data = [
    {"name": "RS", "marks": 15},
    {"name": "j", "marks": 98},
    {"name": "IMV", "marks": 57},
    {"name": "7LvesndHQ", "marks": 82},
    {"name": "W", "marks": 18},
    {"name": "xu", "marks": 47},
    {"name": "J7fQ", "marks": 49},
    {"name": "y", "marks": 52},
    {"name": "mlm4ypy", "marks": 36},
    {"name": "Ihhc8eq", "marks": 32},
    {"name": "4Ikl2fEmd", "marks": 2},
    {"name": "ZtHeXqYB", "marks": 54},
    {"name": "iBY", "marks": 89},
    {"name": "NM", "marks": 37},
    {"name": "7Y", "marks": 75},
    {"name": "2xYqxQBW", "marks": 79},
    {"name": "R", "marks": 70},
    {"name": "Nh", "marks": 28},
    {"name": "lEJBsgtpZ5", "marks": 75},
    {"name": "NLgXlcJh", "marks": 97},
    {"name": "355qEUo1wd", "marks": 83},
    {"name": "peef1mB", "marks": 68},
    {"name": "i", "marks": 87},
    {"name": "9GrYem", "marks": 22},
    {"name": "vsZH", "marks": 22},
    {"name": "9y", "marks": 35},
    {"name": "cjK", "marks": 3},
    {"name": "m9", "marks": 1},
    {"name": "WIkwId", "marks": 67},
    {"name": "fhl0K", "marks": 3},
    {"name": "y8Scz", "marks": 83},
    {"name": "RMjiHa1", "marks": 72},
    {"name": "qR6B", "marks": 93},
    {"name": "3rnwh79", "marks": 19},
    {"name": "aa", "marks": 97},
    {"name": "JMbAfvlI0N", "marks": 90},
    {"name": "QEHDDF8OC", "marks": 38},
    {"name": "kF", "marks": 44},
    {"name": "cg9unO34", "marks": 38},
    {"name": "Vl1", "marks": 69},
    {"name": "HNI7N8", "marks": 52},
    {"name": "ICHP", "marks": 2},
    {"name": "3qBUa", "marks": 12},
    {"name": "AK3iUgH", "marks": 21},
    {"name": "TOfM", "marks": 66},
    {"name": "MqcyEFMMzM", "marks": 91},
    {"name": "Xoea", "marks": 7},
    {"name": "99o5ZgSm", "marks": 59},
    {"name": "lxeJacmdw", "marks": 90},
    {"name": "iKOaGSz", "marks": 30},
    {"name": "zoJ4", "marks": 8},
    {"name": "Yp", "marks": 97},
    {"name": "AEEIAF", "marks": 3},
    {"name": "31MI", "marks": 36},
    {"name": "dJXzAsl", "marks": 19},
    {"name": "LF2k0", "marks": 37},
    {"name": "RfaNL", "marks": 72},
    {"name": "jUXDPZ", "marks": 6},
    {"name": "h", "marks": 30},
    {"name": "z0vi", "marks": 93},
    {"name": "b4Ux", "marks": 30},
    {"name": "3zXtRCrs", "marks": 26},
    {"name": "kFp6rCd", "marks": 69},
    {"name": "ZBWIJgK1s", "marks": 86},
    {"name": "A", "marks": 86},
    {"name": "NoQdcAgu", "marks": 32},
    {"name": "X9wv0", "marks": 65},
    {"name": "d", "marks": 84},
    {"name": "KtVRPY", "marks": 64},
    {"name": "mj2Us", "marks": 2},
    {"name": "WzUfQ", "marks": 56},
    {"name": "8OYTQoaG", "marks": 51},
    {"name": "FfJU", "marks": 3},
    {"name": "j1gW9RW", "marks": 23},
    {"name": "xEkJ", "marks": 86},
    {"name": "b69tAUqV", "marks": 98},
    {"name": "yOiv8JEv", "marks": 94},
    {"name": "UaNk", "marks": 7},
    {"name": "pi5", "marks": 87},
    {"name": "M", "marks": 46},
    {"name": "Wp2", "marks": 10},
    {"name": "lEQbmuU4So", "marks": 1},
    {"name": "AqzB", "marks": 34},
    {"name": "NN5AQ", "marks": 56},
    {"name": "3", "marks": 74},
    {"name": "vg", "marks": 83},
    {"name": "jSBD3uWM", "marks": 57},
    {"name": "1VfYKHq", "marks": 94},
    {"name": "ezAeXYp", "marks": 16},
    {"name": "L7ZT4l5nx9", "marks": 50},
    {"name": "0o7", "marks": 64},
    {"name": "SG", "marks": 62},
    {"name": "baLaLXW", "marks": 53},
    {"name": "OoEz", "marks": 1},
    {"name": "D4SoDxMBZ", "marks": 67},
    {"name": "DlBDivC", "marks": 63},
    {"name": "PntLAKG9U", "marks": 88},
    {"name": "Usx", "marks": 26},
    {"name": "dFx5k1Px", "marks": 72},
    {"name": "p0w", "marks": 59}
]

# Convert to Pandas DataFrame
df = pd.DataFrame(students_data)

# Initialize FastAPI
app = FastAPI()

# Enable CORS for frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def get_marks(names: list[str] = Body(...)):
    result = df[df["name"].isin(names)][["name", "marks"]].to_dict(
        orient="records")
    return result
