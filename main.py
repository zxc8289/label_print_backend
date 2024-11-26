from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],  # 모든 HTTP 메서드 허용
    allow_headers=["*"],  # 모든 헤더 허용
)


# 데이터 모델 정의
class DataModel(BaseModel):
    lotNo: str
    manufactureDate: str
    weight: str
    qrData: str

@app.post("/receive-data")
async def receive_data(data: DataModel):
    # 데이터 처리
    print(f"Lot No: {data.lotNo}")
    print(f"Manufacture Date: {data.manufactureDate}")
    print(f"Weight: {data.weight}")
    print(f"QR Code: {data.qrData}")

    return {"status": "success", "received_data": data}

# 실행 명령
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
