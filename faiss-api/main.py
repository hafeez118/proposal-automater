from fastapi import FastAPI, Request
from proposal_generator import generate_proposal
import uvicorn

app = FastAPI()

@app.post("/generate")
async def generate(req: Request):
    data = await req.json()
    input_text = data.get("prompt", "")
    response = generate_proposal(input_text)
    return {"proposal": response}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)