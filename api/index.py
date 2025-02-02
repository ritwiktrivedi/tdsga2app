from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware

# Sample data
students_data = [
    {"name": "RS", "marks": 95},
    {"name": "Fj", "marks": 40},
    {"name": "RIMVj27Lve", "marks": 31},
    {"name": "ndHQzCWL", "marks": 90},
    {"name": "xu", "marks": 61},
    {"name": "WJ7fQ", "marks": 93},
    {"name": "Bygmm", "marks": 64},
    {"name": "m4ypyWl", "marks": 79},
    {"name": "hh", "marks": 99},
    {"name": "8eqU0", "marks": 50},
    {"name": "Ikl2fEmdBv", "marks": 27},
    {"name": "tHeXq", "marks": 84},
    {"name": "BhPi", "marks": 65},
    {"name": "Y", "marks": 95},
    {"name": "HNMXL7Yvu", "marks": 64},
    {"name": "xYqxQBWxB", "marks": 13},
    {"name": "rGN", "marks": 29},
    {"name": "R6lEJB", "marks": 10},
    {"name": "gtpZ5uwN", "marks": 62},
    {"name": "gX", "marks": 62},
    {"name": "cJh873", "marks": 44},
    {"name": "5qEUo1wdzn", "marks": 42},
    {"name": "eef1mBq", "marks": 18},
    {"name": "i", "marks": 42},
    {"name": "i9GrYemNU", "marks": 19},
    {"name": "sZHNK9yV", "marks": 38},
    {"name": "cjK", "marks": 36},
    {"name": "I", "marks": 53},
    {"name": "9BkWIkw", "marks": 37},
    {"name": "dp", "marks": 24},
    {"name": "fhl0K", "marks": 65},
    {"name": "c", "marks": 7},
    {"name": "8Scz0qRMj", "marks": 82},
    {"name": "Ha1sXq", "marks": 1},
    {"name": "6B6", "marks": 87},
    {"name": "3rnwh79", "marks": 5},
    {"name": "Ga", "marks": 91},
    {"name": "83JMb", "marks": 30},
    {"name": "f", "marks": 66},
    {"name": "lI0N3xQE", "marks": 5},
    {"name": "DD", "marks": 80},
    {"name": "8", "marks": 19},
    {"name": "CYJ", "marks": 2},
    {"name": "Fbrcg9", "marks": 40},
    {"name": "nO34XNVl", "marks": 67},
    {"name": "rgHNI7N8g", "marks": 61},
    {"name": "ICHP", "marks": 6},
    {"name": "qBUaHnAK3", "marks": 60},
    {"name": "UgHNXT", "marks": 2},
    {"name": "fMp", "marks": 5},
    {"name": "MqcyEFMMzM", "marks": 56},
    {"name": "YXoeaEt99o", "marks": 76},
    {"name": "ZgSml0lxeJ", "marks": 3},
    {"name": "cmdw3", "marks": 63},
    {"name": "iKOaGSz", "marks": 86},
    {"name": "YzoJ", "marks": 24},
    {"name": "FGYp8gAEEI", "marks": 63},
    {"name": "F", "marks": 72},
    {"name": "W", "marks": 18},
    {"name": "1MIWmdJXzA", "marks": 0},
    {"name": "lLaLF2k0", "marks": 17},
    {"name": "ZRfa", "marks": 10},
    {"name": "Lsj", "marks": 99},
    {"name": "UXDPZE", "marks": 33},
    {"name": "h", "marks": 88},
    {"name": "Sz0v", "marks": 24},
    {"name": "5Ub4Ux", "marks": 32},
    {"name": "t3zX", "marks": 71},
    {"name": "RCrsQokF", "marks": 80},
    {"name": "6rCdq3Z", "marks": 26},
    {"name": "Jg", "marks": 79},
    {"name": "1s", "marks": 47},
    {"name": "DA1uNoQdc", "marks": 8},
    {"name": "g", "marks": 79},
    {"name": "UeX9wv0o", "marks": 93},
    {"name": "d", "marks": 58},
    {"name": "fKtVRPYne", "marks": 86},
    {"name": "j2UsBZW", "marks": 24},
    {"name": "UfQit8OYT", "marks": 79},
    {"name": "oaG", "marks": 72},
    {"name": "SFfJUC", "marks": 26},
    {"name": "j1gW9RW", "marks": 66},
    {"name": "XxE", "marks": 85},
    {"name": "J1ub69", "marks": 77},
    {"name": "AUqV9wyO", "marks": 59},
    {"name": "v8JEv6", "marks": 2},
    {"name": "UaNk", "marks": 7},
    {"name": "N", "marks": 27},
    {"name": "i52CMcR", "marks": 86},
    {"name": "p2G9", "marks": 94},
    {"name": "EQbmuU4", "marks": 69},
    {"name": "oBYA", "marks": 25},
    {"name": "zBVdNN5", "marks": 90},
    {"name": "Q", "marks": 1},
    {"name": "C3uKvg", "marks": 66},
    {"name": "sjSBD3uWM", "marks": 70},
    {"name": "p1VfYK", "marks": 57},
    {"name": "q6", "marks": 12},
    {"name": "ezAeXYp", "marks": 23},
    {"name": "9L", "marks": 69}
]

# ... (your student data and DataFrame creation remain the same)

app = FastAPI()

origins = ["*"]  # Restrict in production!

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api")
# Use Query for query parameters
async def get_marks(name: list[str] = Query(None)):
    results = []
    for n in name:
        found = False
        for student in students_data:  # Or use the dictionary lookup if you prefer
            if student["name"] == n:
                results.append(student["marks"])
                found = True
                break

        if not found:
            pass

    return {"marks": results}
