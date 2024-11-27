from fastapi import APIRouter

test_router = APIRouter(
    prefix="/test",
    tags=["test"],
)


@test_router.get(path="")
def get_test() -> str:
    return "ok"
