from typing import Annotated
from fastapi import FastAPI, Query

app = FastAPI()

# Case 1: Starred argument for default
# Should become: x: Annotated[int, Query(*[1])] (fallback)
# NOT: x: Annotated[int, Query()] = *[1] (Syntax Error)
@app.get("/f1")
def f1(
    x: int = Query(*[1])
):
    pass

# Case 2: **kwargs in Query
# Should become: x: Annotated[int, Query(**{"a": 1})] (fallback or preserve)
# Current bad behavior: x: Annotated[int, Query()] = 1 (if default found), kwargs dropped.
# With fix: fallback to Annotated[int, Query(1, **{"a": 1})] ?
@app.get("/f2")
def f2(
    x: int = Query(1, **{"a": 1})
):
    pass

# Case 3: Extra positional args
# Should become fallback.
@app.get("/f3")
def f3(
    x: int = Query(1, 2)
):
    pass
